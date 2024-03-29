# Coding UTF-8
from email.policy import strict
from turtle import width
import PySimpleGUI as sg
from check_token import check_token_expiration
from addschedules import add_schedules
from windowlayout import makewindow, makewindow_notoken
from multipleinputcalendar import *
from exchangeformat import *
from voicetotext import voicetotext
from does_a_exist_in import does_a_exist_in
from take_month_and_date_from_text import take_month_and_date_from_text
import webbrowser
import json
import os


def main():
    import theme_list
    # tiken.pickleが作成から一週間経過したら削除
    check_token_expiration()

    # テーマ一覧を取得
    theme_lineup = sg.theme_list()
    theme_list = theme_list.theme_list

    # 設定ファイルの読み込み
    config = sg.UserSettings(
        './settings.ini', use_config_file=True, convert_bools_and_none=True)

    # かれんだーIDがテスト用であればID変更を提案。
    if config['CALENDAR']['calendarid'] == 'ke37d1obkoa9ihbjghnc52ui54@group.calendar.google.com':
        print('カレンダーIDがデフォルトのままです')
        layout = [[sg.Text('カレンダーIDがデフォルトのままなので変更してください', background_color='#FFFFFF', text_color='#000000')],
                  [sg.Text('カレンダーIDの取得方法はこちら', enable_events=True, key='How To', font=(
                      '', 8, 'underline'), text_color='#0067C0', background_color='#FFFFFF')],
                  [sg.Text('カレンダーIDを入力', background_color='#FFFFFF',
                           text_color='#000000')],
                  [sg.InputText()],
                  [sg.Button('登録', key=('registration')), sg.Button('無視して続行', button_color=('#FF0000'), key=('ignore'))]]
        changecalidwindow = sg.Window('CalendarIDを変更してください', layout, background_color='#FFFFFF',
                                      resizable=True, size=(450, 160))
        # 設定を書き込み
        while True:
            event, values = changecalidwindow.read()
            if event == 'registration':
                print(values)
                if values[0] == '':
                    break
                config['CALENDAR']['calendarid'] = values[0]
                break

            if event == sg.WIN_CLOSED or event == 'ignore':
                print('無視して続行します')
                break

            if event == 'How To':
                webbrowser.open('http://gcc.ryou.jp/howto.html')

        changecalidwindow.close()

    # SCOPESを定義
    SCOPES = []
    SCOPES.append(config['USER SETTING']['scope'])

    path = './ScheduleTemps.json'
    if os.path.exists(path):
        pass
    else:
        json_temp = {
            'scheduletemps': {}
        }
        with open(path, 'w', encoding='utf-8') as j:
            json.dump(json_temp, j, indent=4)

    with open(path, 'r', encoding='utf-8') as j:
        temps = json.load(j, strict=False)
    tempkeys = []

    for i in temps['scheduletemps'].keys():
        tempkeys.append(i)
    print(f'Registrated temps = {tempkeys}')

    # GUIWindowを出力
    # window = sg.Window('GCalendarClient',
    #                    windowlayout.windowlayout, resizable=True)
    if os.path.exists('./token.pickle'):
        window = makewindow()
    else:
        window = makewindow_notoken()
    # イベント待機状態へ移行
    while True:
        event, values = window.read()
        # windowが閉じられたり、キャンセルボタンが押されたときプログラムを終了
        if event == sg.WIN_CLOSED or event == 'Cancell' or event == 'Exit':
            break

        if event == 'Multiplecalendar':
            dates = get_dates()
            print(f'Selected dates = {dates}')
            years, months, dates = exchangeFormat(dates)
            window['startYear'].update(years)
            window['endYear'].update(years)
            window['startMonth'].update(months)
            window['endMonth'].update(months)
            window['startDate'].update(dates)
            window['endDate'].update(dates)

        # 登録ボタンが押された時の処理
        if event == 'Submit':
            add_schedules(values)
            window['summary'].update('')
            window['location'].update('')
            window['description'].update('')
            window['result'].update('予定の追加が完了しました')

        if event in theme_lineup:
            print(f'Selected theme = {event}')
            config['USER SETTING']['theme'] = event
            window.close()
            window = makewindow()

        if event == 'ThemePreview':
            sg.theme_previewer()

        if event == 'GitHub':
            webbrowser.open('https://github.com/ryoupr/GCalendarClient')

        if event == 'How To':
            webbrowser.open('http://gcc.ryou.jp/howto.html')

        if event == 'テンプレートとして登録':
            # jsonファイルに今の予定内容を書き込み
            if values['summary'] != '':
                scheduleinfo = {}
                scheduleinfo['summary'] = values['summary']
                scheduleinfo['location'] = values['location']
                scheduleinfo['description'] = values['description']
                scheduleinfo['starthour'] = values['startHour']
                scheduleinfo['startminute'] = values['startMinute']
                scheduleinfo['endhour'] = values['endHour']
                scheduleinfo['endminute'] = values['endMinute']
                scheduleinfo['allday'] = str(values['allDay'])
                temps['scheduletemps'][values['summary']] = scheduleinfo

                with open('./ScheduleTemps.json', 'w', encoding='utf-8') as j:
                    json.dump(temps, j, indent=4)

        if values['buttonmenu'] in tempkeys:
            temp = temps['scheduletemps'][values['buttonmenu']]
            window['summary'].update(temp['summary'])
            window['location'].update(temp['location'])
            window['description'].update(temp['description'])
            window['startHour'].update(temp['starthour'])
            window['startMinute'].update(temp['startminute'])
            window['endHour'].update(temp['endhour'])
            window['endMinute'].update(temp['endminute'])
            if temp['allday'] == 'True':
                window['allDay'].update(True)
            else:
                window['allDay'].update(False)

        if event == '設定ファイルを編集':
            setting = r'settings.ini'
            os.startfile(setting)

        if event == 'テンプレートファイルを編集':
            template = r'ScheduleTemps.json'
            os.startfile(template)

        if event == 'voiceInput':
            # 音声入力から情報を抽出してGCALへ登録する。
            # VoiceInputから文字列へ返還
            reqtext = voicetotext()
            # 音声認識失敗時にエスケープ
            if reqtext == 'Error':
                window['result'].update('音声の認識に失敗しました')
            else:
                print('入力された音声の文字お越し：' + reqtext)
                # テンプレートのサマリーリストを作成してDoes a exist in？に文字起こししたテキストと一緒に渡す。
                print(tempkeys)
                # exit_in [0]にはTrueかFalse[1]発見したテンプレートのSummaryが入っている
                exist_in = does_a_exist_in(reqtext, tempkeys)
                print(exist_in)
                if exist_in[0]:
                    print('一致するテンプレート情報を見つけました')
                    temp = temps['scheduletemps'][exist_in[1]]
                    window['summary'].update(temp['summary'])
                    window['location'].update(temp['location'])
                    window['description'].update(temp['description'])
                    window['startHour'].update(temp['starthour'])
                    window['startMinute'].update(temp['startminute'])
                    window['endHour'].update(temp['endhour'])
                    window['endMinute'].update(temp['endminute'])
                    if temp['allday'] == 'True':
                        window['allDay'].update(True)
                    else:
                        window['allDay'].update(False)

                    #月と日付情報の抽出（リターンは辞書型　{'month': '11', 'date': ['1', '3']}で帰ってきます）
                    eventdate = take_month_and_date_from_text(reqtext)
                    print(eventdate)
                    window['startMonth'].update(eventdate['month'])
                    window['endMonth'].update(eventdate['month'])
                    date = ''
                    for i in eventdate['date']:
                        date +=i+','
                    date = date[:-1]
                    print(date)
                    window['startDate'].update(date)
                    window['endDate'].update(date)
                    #年情報の更新
                    window['startYear'].update(eventdate['year'])
                    window['endYear'].update(eventdate['year'])
                else:
                    print('音声認識失敗')
                    window['result'].update('音声の認識に失敗しました')

    window.close()


if __name__ == '__main__':
    main()
