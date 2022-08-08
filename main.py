# Coding UTF-8
import PySimpleGUI as sg

# Import user func
from check_token import check_token_expiration
from addschedules import add_schedules
from windowlayout import makewindow
from multipleinputcalendar import *
from exchangeformat import *
import theme_list
import webbrowser


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


def main():
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
            print(dates)
            years, months, dates = exchangeFormat(dates)
            window['startYear'].update(years)
            window['endYear'].update(years)
            window['startMonth'].update(months)
            window['endMonth'].update(months)
            window['startDate'].update(dates)
            window['endDate'].update(dates)
            print(values)

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

    window.close()


if __name__ == '__main__':
    main()
