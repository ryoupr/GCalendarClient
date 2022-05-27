from xmlrpc.client import DateTime
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

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    # Theme = DarkAmber
    sg.theme("DarkAmber")
    # 項目名サイズ
    sizeTypeA = 9
    buttonWidth = 50
    buttonHaight = 2
    datetimeBoxSize = 4
    layout = [
        [sg.Text("概要", size=(sizeTypeA)),
         sg.InputText("", size=(98), key="summary")],
        [sg.Text("場所", size=(sizeTypeA)), sg.InputText(
            "", size=(98), key="location")],
        [sg.Text("説明", size=(sizeTypeA)), sg.InputText(
            "", size=(98), key=("description"))],
        [sg.Text("開始年月日", size=(sizeTypeA)), sg.InputText("", size=(datetimeBoxSize), key="startYear"), sg.Text("年"),
         sg.InputText("", size=(datetimeBoxSize), key=("startMonth")), sg.Text("月"), sg.InputText("", size=(datetimeBoxSize), key=("startDate")), sg.Text("日")],
        [sg.Text("開始時間", size=(sizeTypeA)),
         sg.InputText("", size=(datetimeBoxSize), key=("startHour")),
         sg.Text("時"),
         sg.InputText("", size=(datetimeBoxSize), key=("startMinute")),
         sg.Text("分"),
         sg.Checkbox("終日", key="allDay")
         ],
        [sg.Text("", size=(sizeTypeA)), sg.Text("↓↓↓")],
        [sg.Text("終了年月日", size=(sizeTypeA)), sg.InputText("", size=(datetimeBoxSize), key="endYear"), sg.Text(
            "年", ), sg.InputText("", size=(datetimeBoxSize), key=("endMonth")), sg.Text("月", ), sg.InputText("", size=(datetimeBoxSize), key=("endDate")), sg.Text("日")],
        [sg.Text("終了時間", size=(sizeTypeA)), sg.InputText("", size=(datetimeBoxSize), key=("endHour")),
         sg.Text("時"), sg.InputText("", size=(datetimeBoxSize), key="endMinute"), sg.Text("分")], [sg.Text(size=(98), key=("result"))],
        [sg.Button("登録", key="Submit", size=(buttonWidth, buttonHaight)), sg.Button(
            "取消", key="Cancell", size=(buttonWidth, buttonHaight))]
    ]

    window = sg.Window("GoogleCalendarに予定を追加", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancell":
            break

    if values["allDay"]:
        print("checked")


if __name__ == "__main__":
    main()
