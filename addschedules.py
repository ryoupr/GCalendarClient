from audioop import add
from operator import le
from stringprep import in_table_c9
from tracemalloc import start
from http.client import OK
from xmlrpc.client import DateTime
import PySimpleGUI as sg
import os
from tracemalloc import start
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
from generate_datetime import *
from datetime_master import *
from verify_format import verify_all_day_event
import PySimpleGUI as sg


def add_schedules(values):
    #　終日イベントかどうか検証
    # 終日イベント追加
    if values['allDay'] or values['startHour'] == '':
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
        startyears = values['startYear'].split(',')
        endyears = values['endYear'].split(',')
        startmonths = values['startMonth'].split(',')
        endmonths = values['endMonth'].split(',')
        startdates = values['startDate'].split(',')
        enddates = values['endDate'].split(',')
        print('--------------------送信する各要素----------------------------')
        print(f'startyears = {startyears}')
        print(f'endyears  = {endyears} ')
        print(f'startmonths = {startmonths}')
        print(f'endmonths  = {endmonths} ')
        print(f'startdates = {startdates}')
        print(f'enddates  = {enddates} ')
        print('------------------------------------------------------------')

        # 開始日・終了日の要素数が違ったら終了日を開始日と同一とする
        if len(startdates) != len(enddates):
            enddates = startdates
            
        print('追加する予定数 = '+str(len(startdates)))
        if len(startdates) == 1:
            print('要素数１のイベント用追加処理')
            values['startYear'] = startyears[0]
            values['endYear'] = endyears[0]
            values['startMonth'] = startmonths[0]
            values['endMonth'] = endmonths[0]
            values['startDate'] = startdates[0]
            values['endDate'] = enddates[0]
            print(f'Values = {values}')

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
                print(f'calendarEvent={calendarEvent}')
                registration(calendarEvent)
            else:
                print('Syntax error(values) addschedules.py')


        else:
            print('追加する予定数 = '+str(len(startdates)))
            for i in range(0, len(startdates)):
                print(f'i = {i}')
                print('join for ')
                values['startYear'] = startyears[i]
                values['endYear'] = endyears[i]
                values['startMonth'] = startmonths[i]
                values['endMonth'] = endmonths[i]
                values['startDate'] = startdates[i]
                values['endDate'] = enddates[i]

                print(f'Values = {values}')

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
                    print(f'calendarEvent={calendarEvent}')
                    registration(calendarEvent)
                else:
                        print('Syntax error(values) addschedules.py L82')
# -----------終日イベント追加終了------------------------------------------------------------------------

    else:
        # 非終日イベント
        # 以下は日終日イベント追加処理
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
        startyears = values['startYear'].split(',')
        endyears = values['endYear'].split(',')
        startmonths = values['startMonth'].split(',')
        endmonths = values['endMonth'].split(',')
        startdates = values['startDate'].split(',')
        enddates = values['endDate'].split(',')
        starthours = values['startHour'].split(',')
        startminutes = values['startMinute'].split(',')
        endhours = values['endHour'].split(',')
        endminutes = values['endMinute'].split(',')
        print(f'startyears = {startyears}')
        print(f'endyears  = {endyears} ')
        print(f'startmonths = {startmonths}')
        print(f'endmonths  = {endmonths} ')
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
                values['startYear'] = startyears[i]
                values['endYear'] = endyears[i]
                values['startMonth'] = startmonths[i]
                values['endMonth'] = endmonths[i]
                values['startDate'] = startdates[i]
                values['endDate'] = enddates[i]
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
                values['startYear'] = startyears[i]
                values['endYear'] = endyears[i]
                values['startMonth'] = startmonths[i]
                values['endMonth'] = endmonths[i]
                values['startDate'] = startdates[i]
                values['endDate'] = enddates[i]

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
                values['startYear'] = startyears[i]
                values['endYear'] = endyears[i]
                values['startMonth'] = startmonths[i]
                values['endMonth'] = endmonths[i]
                values['startDate'] = startdates[i]
                values['endDate'] = enddates[i]

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
    config = sg.UserSettings(
        './settings.ini', use_config_file=True,  convert_bools_and_none=True)
    SCOPES = []
    SCOPES.append(str(config['USER SETTING']['scope']))
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
    print(calendarEvent)
    print('予定追加開始')
    calendarEvent = service.events().insert(
        calendarId=config['CALENDAR']['calendarid'], body=calendarEvent).execute()
    print('予定追加完了')


if __name__ == '__main__':
    # add_schedules(values)
    pass
