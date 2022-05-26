import PySimpleGUI as sg
import os
from tabnanny import check
from tracemalloc import start
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import datetime

# Import user func
from timeFormatCheck import timeFormatCheck
from dateFormatCheck import dateFormatCheck
from makeDateTime import makeDateTime

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    # Theme = DarkAmber
    sg.theme("DarkAmber")
    # 項目名サイズ
    sizeTypeA = 9
    buttonWidth = 50
    buttonHaight = 2
    layout = [
        [sg.Text("概要", size=(sizeTypeA)), sg.InputText(
            "", size=(98, 1), key="summary")],
        [sg.Text("場所", size=(sizeTypeA)), sg.InputText(
            "", size=(98, 1), key="location")],
        [sg.Text("説明", size=(sizeTypeA)), sg.InputText(
            "", size=(98, 1), key=("description"))],
        [sg.Text("開始年月日", size=(sizeTypeA)), sg.InputText("", size=(10, 1), key="startYear"), sg.Text("年"),
         sg.InputText("", size=(10, 1), key=("startMonth")), sg.Text("月"), sg.InputText("", size=(10, 1), key=("startDate")), sg.Text("日")],
        [sg.Text("開始時間", size=(sizeTypeA)), sg.InputText("", size=(10), key=("startHour")),
         sg.Text("時"), sg.InputText("", size=(10), key=("startMinute")), sg.Text("分")],
        [sg.Text("", size=(sizeTypeA)), sg.Text("↓↓↓")],
        [sg.Text("終了年月日", size=(sizeTypeA)), sg.InputText("", size=(10, 1), key="endYear"), sg.Text(
            "年", ), sg.InputText("", size=(10, 1), key=("endMonth")), sg.Text("月", ), sg.InputText("", size=(10, 1), key=("endDate")), sg.Text("日")],
        [sg.Text("終了時間", size=(sizeTypeA)), sg.InputText("", size=(10), key=("endHour")),
         sg.Text("時"), sg.InputText("", size=(10), key="endMinute"), sg.Text("分")],
        [sg.Button("登録", key="Submit", size=(buttonWidth, buttonHaight)), sg.Button(
            "取消", key="Cancell", size=(buttonWidth, buttonHaight))]
    ]

    window = sg.Window("GoogleCalendarに予定を追加", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancell":
            break

        if event == "Submit":
            print("送信ボタンが押されました")
            # CLI版のmain.pyの中身を移植
            calendarEvent = {
                'summary': "",
                'location': "",
                'description': "",
                'start': {
                    'dateTime': "",
                    'timeZone': 'Japan',
                },
                'end': {
                    'dateTime': "",
                    'timeZone': 'Japan',
                },
            }

        # insert calendar event
            calendarEvent["summary"] = values["summary"]
            calendarEvent["location"] = values["location"]
            calendarEvent['description'] = values["description"]
            # todo dateTime入力情報からを生成する式を作成し変更後挿入する
            #todo start datetime を生成する。
            break
    window.close()
    print(f'eventは{event}')
    print(f'valuesは{values}')


if __name__ == "__main__":
    main()
