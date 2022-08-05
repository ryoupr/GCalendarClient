# Coding UTF-8
import PySimpleGUI as sg
import configparser
from addschedules import add_schedules

# Import user func
from check_token import check_token_expiration
import windowlayout
from multipleimputcalendar import *
from exchangeformat import *

# tiken.pickleが作成から一週間経過したら削除
check_token_expiration()

# If modifying these scopes, delete the file token.pickle.
# 設定ファイルの読み込み
config = configparser.ConfigParser()
config.read('./setting/setting.ini')
SCOPES = []
SCOPES.append(config['DEFAULT']['scope'])


def main():
    # GUIWindowを出力
    window = sg.Window('GCalendarClient',
                       windowlayout.windowlayout, resizable=True)
    # イベント待機状態へ移行
    while True:
        event, values = window.read()
        # windowが閉じられたり、キャンセルボタンが押されたときプログラムを終了
        if event == sg.WIN_CLOSED or event == 'Cancell':
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
        if event == 'Test':
            print('Pushed file/test button')
    window.close()


if __name__ == '__main__':
    main()
