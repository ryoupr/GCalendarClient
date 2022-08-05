from datetime_master import *
import PySimpleGUI as sg
import configparser


config = configparser.ConfigParser()
config.read('./setting/setting.ini')
sg.theme(config['DEFAULT']['theme'])

INPUTBOX = 9
BUTTONWIDTH = 50
BUTTONHAIGHT = 2
DATETIMEBOX = 4
# PySimpleGUIレイアウト設定
windowlayout = [[sg.MenubarCustom([['File', ['Test',['Test2'],'Exit']], ['Edit', ['Test']]])],
                [sg.Text('概要', size=(INPUTBOX)),
                 sg.InputText('', size=(98), key='summary')],
                [sg.Text('場所', size=(INPUTBOX)), sg.InputText(
                    '', size=(98), key='location')],
                [sg.Text('説明', size=(INPUTBOX)), sg.InputText(
                    '', size=(98), key=('description'))],
                [sg.Text('開始年月日', size=(INPUTBOX)), sg.InputText(this_year(), size=(DATETIMEBOX), key='startYear'), sg.Text('年'),
                 sg.InputText(this_month(), size=(DATETIMEBOX), key=('startMonth')), sg.Text('月'), sg.InputText(today(), size=(DATETIMEBOX), key=('startDate')), sg.Text('日'), sg.Button('カレンダーから選択', key='Multiplecalendar', size=(15, 1))],
                [sg.Text('開始時間', size=(INPUTBOX)),
                 sg.InputText('', size=(DATETIMEBOX), key=('startHour')),
                 sg.Text('時'),
                 sg.InputText('', size=(DATETIMEBOX), key=('startMinute')),
                 sg.Text('分'),
                 sg.Checkbox('終日', key='allDay')
                 ],
                [sg.Text('', size=(INPUTBOX)), sg.Text('↓↓↓')],
                [sg.Text('終了年月日', size=(INPUTBOX)), sg.InputText(this_year(), size=(DATETIMEBOX), key='endYear'), sg.Text(
                    '年', ), sg.InputText(this_month(), size=(DATETIMEBOX), key=('endMonth')), sg.Text('月', ), sg.InputText(today(), size=(DATETIMEBOX), key=('endDate')), sg.Text('日')],
                [sg.Text('終了時間', size=(INPUTBOX)), sg.InputText('', size=(DATETIMEBOX), key=('endHour')),
                 sg.Text('時'), sg.InputText('', size=(DATETIMEBOX), key='endMinute'), sg.Text('分')], [sg.Text(size=(98), key=('result'))],
                [sg.Button('登録', key='Submit', size=(BUTTONWIDTH, BUTTONHAIGHT)), sg.Button(
                    '取消', key='Cancell', size=(BUTTONWIDTH, BUTTONHAIGHT))]
                ]
