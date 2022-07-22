from audioop import add
from operator import le
from stringprep import in_table_c9
from tracemalloc import start
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
from generate_datetime import *
from datetime_master import *
from verify_format import verify_all_day_event
import PySimpleGUI as sg


def include_conma(mat):
    for i in mat:
        if i == ',':
            return True
    else:
        return False


# テスト用values
values = {'summary': '0715', 'location': '日本工学院専門学校', 'description': '卒業制作製作過程でのテストです', 'startYear': '2022', 'startMonth': '07', 'startDate': '16,18,19', 'startHour': '',
          'startMinute': '', 'allDay': True, 'endYear': '2022', 'endMonth': '07', 'endDate': '16,18,19', 'endHour': '', 'endMinute': ''}


def add_schedules(values):
    #　終日イベントかどうか検証
    if values['allDay'] or values['startHour'] == '':
        print('終日イベント')
        # 終日イベント
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
        # カンマ区切りでリストを作成
        startdates = values['startDate'].split(',')
        enddates = values['endDate'].split(',')
        print(f'statdates are {startdates}')
        print(f'enddates  are {enddates} ')
        # 開始日・終了日の要素数が違ったら終了日を開始日と同一とする
        if len(startdates) != len(enddates):
            enddates = startdates
        # forで回しながら予定を追加
        for i in range(0, len(startdates)):
            values['startDate'] = startdates[i]
            values['endDate'] = enddates[i]
            # 書式があっているか検証
            if verify_all_day_event(values):
                calendarEvent['summary'] = values['summary']
                calendarEvent['location'] = values['location']
                calendarEvent['description'] = values['description']
                calendarEvent['start']['date'] = generate_date(
                    values['startYear'], values['startMonth'], values['startDate'])
                calendarEvent['end']['date'] = generate_date(
                    values['endYear'], values['endMonth'], values['endDate']
                )
                print(f'''
calendarEvent
{calendarEvent}
''')
                registration(calendarEvent)
    else:
        # 非終日イベント
        print('非終日イベント')
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
        # 開始日・終了日・開始時刻(時・分)・終了時刻のリスト作成
        startdates = values['startDate'].split(',')
        enddates = values['endDate'].split(',')
        starthours = values['startHour'].split(',')
        startminutes = values['startMinute'].split(',')
        endhours = values['endHour'].split(',')
        endminutes = values['endMinute'].split(',')
        print(f'statdates are {startdates}')
        print(f'enddates  are {enddates} ')
        print(f'starthours  are {starthours} ')
        print(f'startminutes  are {startminutes} ')
        print(f'endhours  are {endhours} ')
        print(f'endminutes are {endminutes} ')
        if len(startdates) != len(enddates):
            enddates = startdates
        if len(startdates) == len(enddates) == len(starthours) == len(startminutes) == len(endhours) == len(endminutes):
            for i in range(0, len(startdates)):
                # todo valuesの内容検証を！！
                calendarEvent['summary'] = values['summary']
                calendarEvent['location'] = values['location']
                calendarEvent['description'] = values['description']
                calendarEvent['start']['dateTime'] = generate_datetime(
                    values['startYear'], values['startMonth'], startdates[i], starthours[i], startminutes[i])
                calendarEvent['end']['dateTime'] = generate_datetime(
                    values['endYear'], values['endMonth'], enddates[i], endhours[i], endminutes[i]
                )
                registration(calendarEvent)
        elif len(starthours) == 1 and len(startdates) >= 1:
            for i in range(0, len(startdates)):
                calendarEvent['summary'] = values['summary']
                calendarEvent['location'] = values['location']
                calendarEvent['description'] = values['description']
                calendarEvent['start']['dateTime'] = generate_datetime(
                    values['startYear'], values['startMonth'], startdates[i], values['startHour'], values['startMinute'])
                calendarEvent['end']['dateTime'] = generate_datetime(
                    values['endYear'], values['endMonth'], enddates[i], values['endHour'], values['endMinute']
                )
                registration(calendarEvent)
        elif len(startdates) == 1 and len(starthours) >= 1:
            for i in range(0, len(starthours)):
                calendarEvent['summary'] = values['summary']
                calendarEvent['location'] = values['location']
                calendarEvent['description'] = values['description']
                calendarEvent['start']['dateTime'] = generate_datetime(
                    values['startYear'], values['startMonth'], values['startDate'], starthours[i], startminutes[i])
                calendarEvent['end']['dateTime'] = generate_datetime(
                    values['endYear'], values['endMonth'], values['endDate'], endhours[i], endminutes[i]
                )
                registration(calendarEvent)
        else:
            return False
        # todo 終日イベントでないときも検証を行うように追加を
        # # insert calendar event
        # calendarEvent['summary'] = values['summary']
        # calendarEvent['location'] = values['location']
        # calendarEvent['description'] = values['description']
        # calendarEvent['start']['dateTime'] = generate_datetime(
        #     values['startYear'], values['startMonth'], values['startDate'], values['startHour'], values['startMinute'])
        # calendarEvent['end']['dateTime'] = generate_datetime(
        #     values['endYear'], values['endMonth'], values['endDate'], values['endHour'], values['endMinute']
        # )
        # registration(calendarEvent)


def registration(calendarEvent):
    print(f'''Func:registration
引数 = {calendarEvent}''')
    config = configparser.ConfigParser()
    config.read('./setting/setting.ini')
    SCOPES = []
    SCOPES.append(str(config['DEFAULT']['scope']))
    print(f'Scope = {SCOPES}')
    # トークン用変数初期化
    creds = None
    print('トークンの存在を確認中...')
    if os.path.exists('token.pickle'):
        print('確認できました')
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            print(f'creds = {creds}')
    else:
        print('トークンの存在を確認できませんでした')
        print('認証を行いトークンを生成してください')
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

            # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    print('予定追加開始')
    calendarEvent = service.events().insert(
        calendarId=config['CALENDAR']['calendarID'], body=calendarEvent).execute()
    print('予定追加完了')


if __name__ == '__main__':
    add_schedules(values)
