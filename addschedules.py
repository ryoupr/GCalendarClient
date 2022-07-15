from audioop import add
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


def include_conma(mat):
    for i in mat:
        if i == ',':
            return True
    else:
        return False


# テスト用values
values = {'summary': '0715', 'location': '場所', 'description': '説明', 'startYear': '2022', 'startMonth': '07', 'startDate': '16,18,19', 'startHour': '',
          'startMinute': '', 'allDay': True, 'endYear': '2022', 'endMonth': '07', 'endDate': '16,18,19', 'endHour': '', 'endMinute': ''}


def add_schedules(values):
    # 全日イベント用カレンダーイベント
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
    #　終日イベントかどうかを検証
    if values['allDay']:
        # 終日イベント
        # カンマ区切りでリストを作成
        startdates = values['startDate'].split(',')
        enddates = values['endDate'].split(',')
        # forで回しながら予定を追加
        for i in range(0, len(startdates)):
            values['startDate'] = startdates[i]
            values['endDate'] = enddates[i]
            if verify_all_day_event(values):
                calendarEvent['summary'] = values['summary']
                calendarEvent['location'] = values['location']
                calendarEvent['description'] = values['description']
                calendarEvent['start']['date'] = generate_date(
                    values['startYear'], values['startMonth'], values['startDate'])
                calendarEvent['end']['date'] = generate_date(
                    values['endYear'], values['endMonth'], values['endDate']
                )
                registration(calendarEvent)
                print('予定'+str(i+1)+'追加完了')
    else:
        # 非終日イベント
        print('非終日イベント')
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


def registration(calendarEvent):
    config = configparser.ConfigParser()
    config.read('./setting/setting.ini')
    SCOPES = '[' + config['DEFAULT']['scope'] + ']'

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    creds = None
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
if __name__ == '__main__':
    add_schedules(values)
