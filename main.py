# Coding UTF-8
from http.client import OK
from unittest.mock import DEFAULT
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
from addschedules import add_schedules

# Import user func
from verify_format import *
from generate_datetime import *
from datetime_master import *
from check_token import check_token_expiration
import windowlayout

# tiken.pickleが作成から一週間経過したら削除
check_token_expiration()

# If modifying these scopes, delete the file token.pickle.
# 設定ファイルの読み込み
config = configparser.ConfigParser()
config.read('./setting/setting.ini')
SCOPES = []
SCOPES.append(config['DEFAULT']['scope'])

# SCOPES = '[' + config['DEFAULT']['scope'] + ']'


def main():
    # GUIWindowを出力
    window = sg.Window('GoogleCalendarに予定を追加',
                       windowlayout.windowlayout, resizable=True)
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
                print(values)
                add_schedules(values)
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
                # todo 終日イベントでないときも検証を行うように追加を
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
            # 検証結果がTrueならリクエストを送信
            if False:
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
                # APIと対話するためのResourceオブジェクトを構築
                service = build('calendar', 'v3', credentials=creds)

                calendarEvent = service.events().insert(
                    calendarId=config['CALENDAR']['calendarID'], body=calendarEvent).execute()
                print(values)
                window['result'].update('予定の追加は正常に終了しました！！')
                window['summary'].update('')
                window['location'].update('')
                window['description'].update('')
                print('is registered')
            else:
                # window['result'].update('予定の情報にエラーがあります')
                # print('Err')
                pass
    window.close()


if __name__ == '__main__':
    main()
