# Coding UTF-8
from http.client import OK
from xmlrpc.client import DateTime
import PySimpleGUI as sg
import os
from tabnanny import check
from tracemalloc import start
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import configparser
import datetime

# Import user func
from check_format import *
from generate_datetime import *
from datetime_master import *
from check_token import check_token_expiration

# tiken.pickleが作成から一週間経過したら削除
check_token_expiration()

# If modifying these scopes, delete the file token.pickle.
# 設定ファイルの読み込み
config = configparser.ConfigParser()
config.read('./setting/setting.ini')
SCOPES = '[' + config['DEFAULT']['scope'] + ']'

def main():
    # setting.iniからスキン情報を取得し適用
    sg.theme(config['DEFAULT']['theme'])
    # 項目名サイズ
    sizeTypeA = 9
    buttonWidth = 50
    buttonHaight = 2
    datetimeBoxSize = 4
    # PySimpleGUIレイアウト設定
    layout = [
        [sg.Text('概要', size=(sizeTypeA)),
         sg.InputText('', size=(98), key='summary')],
        [sg.Text('場所', size=(sizeTypeA)), sg.InputText(
            '', size=(98), key='location')],
        [sg.Text('説明', size=(sizeTypeA)), sg.InputText(
            '', size=(98), key=('description'))],
        [sg.Text('開始年月日', size=(sizeTypeA)), sg.InputText(this_year(), size=(datetimeBoxSize), key='startYear'), sg.Text('年'),
         sg.InputText(this_month(), size=(datetimeBoxSize), key=('startMonth')), sg.Text('月'), sg.InputText(today(), size=(datetimeBoxSize), key=('startDate')), sg.Text('日')],
        [sg.Text('開始時間', size=(sizeTypeA)),
         sg.InputText('', size=(datetimeBoxSize), key=('startHour')),
         sg.Text('時'),
         sg.InputText('', size=(datetimeBoxSize), key=('startMinute')),
         sg.Text('分'),
         sg.Checkbox('終日', key='allDay')
         ],
        [sg.Text('', size=(sizeTypeA)), sg.Text('↓↓↓')],
        [sg.Text('終了年月日', size=(sizeTypeA)), sg.InputText(this_year(), size=(datetimeBoxSize), key='endYear'), sg.Text(
            '年', ), sg.InputText(this_month(), size=(datetimeBoxSize), key=('endMonth')), sg.Text('月', ), sg.InputText(today(), size=(datetimeBoxSize), key=('endDate')), sg.Text('日')],
        [sg.Text('終了時間', size=(sizeTypeA)), sg.InputText('', size=(datetimeBoxSize), key=('endHour')),
         sg.Text('時'), sg.InputText('', size=(datetimeBoxSize), key='endMinute'), sg.Text('分')], [sg.Text(size=(98), key=('result'))],
        [sg.Button('登録', key='Submit', size=(buttonWidth, buttonHaight)), sg.Button(
            '取消', key='Cancell', size=(buttonWidth, buttonHaight))]
    ]

    # GUIWindowを出力
    window = sg.Window('GoogleCalendarに予定を追加', layout, resizable=True)
    # イベント待機状態へ移行
    while True:
        event, values = window.read()
        # windowが閉じられたり、キャンセルボタンが押されたときプログラムを終了
        if event == sg.WIN_CLOSED or event == 'Cancell':
            break
        # 登録ボタンが押された時の処理
        if event == 'Submit':
            # 終日チェックボックスにチェックがTrueの場合
            if values['allDay']:
                #終日用の送信辞書を定義
                calendarEvent = {
                    'summary': '',
                    'location': '',
                    'description': '',
                    'start': {
                        'date': '',
                        'timeZone': 'Japan',
                    },
                    'end': {
                        'date': '',
                        'timeZone': 'Japan',
                    },
                }
                #データがおかしくないか検証
                is_verify_ok = False
                verify_flags = {'SYFCFlag': '', 'SYFCFlag': '', 'SMFCFlag': '',
                           'SDFCFlag': '', 'EYFCFlag': '', 'EMFCFlag': ''}
                verify_flags['SYFCFlag'] = verify_year(values['startYear'])
                #検証用辞書の中にFalseが一つもなければ続行
                if False not in verify_flags.values():
                    verify_flags['SMFCFlag'] = verify_month(
                        values['startYear'], values['startMonth'])
                if False not in verify_flags.values():
                    verify_flags['SDFCFlag'] = verify_start_date(
                        values['startYear'], values['startMonth'], values['startDate'])
                if False not in verify_flags.values():
                    verify_flags['EYFCFlag'] = verify_end_year(
                        values['startYear'], values['endYear'])
                if False not in verify_flags.values():
                    verify_flags['EMFCFlag'] = verify_end_month(
                        values['startYear'], values['endYear'], values['startMonth'], values['endMonth'])
                if False not in verify_flags.values():
                    verify_flags['EDFCFlag'] = verify_end_date(values['startYear'], values['endYear'], values['startMonth'],
                                                    values['endMonth'], values['startDate'], values['endDate'])
                if False not in verify_flags.values():
                    is_verify_ok = True
                    calendarEvent['summary'] = values['summary']
                    calendarEvent['location'] = values['location']
                    calendarEvent['description'] = values['description']
                    calendarEvent['start']['date'] = generateDate(
                        values['startYear'], values['startMonth'], values['startDate'])
                    calendarEvent['end']['date'] = generateDate(
                        values['endYear'], values['endMonth'], values['endDate']
                )
            else:
                # 終日イベントでない場合
                calendarEvent = {
                    'summary': '',
                    'location': '',
                    'description': '',
                    'start': {
                        'dateTime': '',
                        'timeZone': 'Japan',
                    },
                    'end': {
                        'dateTime': '',
                        'timeZone': 'Japan',
                    },
                }
            # insert calendar event
                calendarEvent['summary'] = values['summary']
                calendarEvent['location'] = values['location']
                calendarEvent['description'] = values['description']
                calendarEvent['start']['dateTime'] = generate_datetime(
                    values['startYear'], values['startMonth'], values['startDate'], values['startHour'], values['startMinute'])
                calendarEvent['end']['dateTime'] = generate_datetime(
                    values['endYear'], values['endMonth'], values['endDate'], values['endHour'], values['endMinute']
                )
            creds = None
            #検証結果がTrue＝OKならリクエストを送信
            if is_verify_ok:
                # The file token.pickle stores the user's access and refresh tokens, and is
                # created automatically when the authorization flow completes for the first
                # time.
                if os.path.exists('token.pickle'):
                    with open('token.pickle', 'rb') as token:
                        creds = pickle.load(token)
                # If there are no (valid) credentials available, let the user log in.
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(
                            'credentials.json', SCOPES)
                        creds = flow.run_local_server(port=0)
                    # Save the credentials for the next run
                    with open('token.pickle', 'wb') as token:
                        pickle.dump(creds, token)

                service = build('calendar', 'v3', credentials=creds)

                calendarEvent = service.events().insert(
                    calendarId=config['CALENDAR']['calendarID'], body=calendarEvent).execute()
                # calendarEvent = service.events().insert(calendarId='ke37d1obkoa9ihbjghnc52ui54@group.calendar.google.com',body=calendarEvent).execute()
                window['result'].update('予定の追加は正常に終了しました！！')
                window['summary'].update('')
                window['location'].update('')
                window['description'].update('')
                print('is resistered')
            else:
                window['result'].update('予定の情報にエラーがあります')
                print('Err')
    window.close()


if __name__ == '__main__':
    main()
