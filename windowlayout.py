from datetime_master import *
import PySimpleGUI as sg


def makewindow():
    import theme_list
    theme_list = theme_list.theme_list

    config = sg.UserSettings('./settings.ini', use_config_file=True,
                             convert_bools_and_none=True)
    sg.theme(config['USER SETTING']['theme'])

    INPUTBOX = 9
    BUTTONWIDTH = 50
    BUTTONHAIGHT = 2
    DATETIMEBOX = 4
    # PySimpleGUIレイアウト設定
    windowlayout = [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Theme', [theme_list], 'ThemePreview']], ['Help', ['How To']]])],
                    [sg.Text('概要', size=(INPUTBOX)),
                     sg.InputText('', size=(98), key='summary')],
                    [sg.Text('場所', size=(INPUTBOX)), sg.InputText(
                        '', size=(98), key='location')],
                    [sg.Text('説明', size=(INPUTBOX)), sg.InputText(
                        '', size=(98), key=('description'))],
                    [sg.Text('開始日時', size=(INPUTBOX)), sg.InputText(this_year(), size=(DATETIMEBOX), key='startYear'), sg.Text('/'),
                     sg.InputText(this_month(), size=(DATETIMEBOX), key=('startMonth')), sg.Text('/'), sg.InputText(today(), size=(DATETIMEBOX), key=('startDate')), sg.Button('カレンダーから選択', key='Multiplecalendar', size=(15, 1))],
                    [sg.Text('', size=(INPUTBOX)),
                     sg.InputText('', size=(DATETIMEBOX), key=('startHour')),
                     sg.Text(':'),
                     sg.InputText('', size=(DATETIMEBOX), key=('startMinute')),
                     sg.Checkbox('終日', key='allDay')
                     ],
                    [sg.Text('', size=(INPUTBOX)), sg.Text('↓↓↓')],
                    [sg.Text('終了日時', size=(INPUTBOX)), sg.InputText(this_year(), size=(DATETIMEBOX), key='endYear'), sg.Text(
                        '/', ), sg.InputText(this_month(), size=(DATETIMEBOX), key=('endMonth')), sg.Text('/', ), sg.InputText(today(), size=(DATETIMEBOX), key=('endDate'))],
                    [sg.Text('', size=(INPUTBOX)), sg.InputText('', size=(DATETIMEBOX), key=('endHour')),
                     sg.Text(':'), sg.InputText('', size=(DATETIMEBOX), key='endMinute')], [sg.Text(size=(98), key=('result'))],
                    [sg.Button('登録', key='Submit', size=(BUTTONWIDTH, BUTTONHAIGHT)), sg.Button(
                        '取消', key='Cancell', size=(BUTTONWIDTH, BUTTONHAIGHT))]
                    ]

    window = sg.Window('GCalendarClient', windowlayout, resizable=True)

    return window


if __name__ == '__main__':
    makewindow()
    print(makewindow)
