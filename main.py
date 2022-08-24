# Coding UTF-8
from email.policy import strict
from turtle import width
import PySimpleGUI as sg
from check_token import check_token_expiration
from addschedules import add_schedules
from windowlayout import makewindow
from multipleinputcalendar import *
from exchangeformat import *
import webbrowser
import json
import os
import subprocess


def main():
    import theme_list
    # tiken.pickleが作成から一週間経過したら削除
    check_token_expiration()

    theme_lineup = sg.theme_list()
    theme_list = theme_list.theme_list

    # If modifying these scopes, delete the file token.pickle.
    # 設定ファイルの読み込み
    config = sg.UserSettings(
        './settings.ini', use_config_file=True, convert_bools_and_none=True)

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
    window = makewindow()
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

        if event == 'How To':
            webbrowser.open('https://github.com/ryoupr/GCalendarClient')

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

        if event == 'Setting.ini':
            setting = r'./setting.ini'
            subprocess.Popen(['start', setting], shell=True)


    window.close()


if __name__ == '__main__':
    main()
