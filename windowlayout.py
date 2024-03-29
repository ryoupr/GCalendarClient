from datetime_master import *
import PySimpleGUI as sg
import json


def makewindow():
    import theme_list
    theme_list = theme_list.theme_list

    with open('./ScheduleTemps.json', 'r', encoding='utf-8') as j:
        temps = json.load(j)
    tempkeys = []
    for i in temps['scheduletemps'].keys():
        tempkeys.append(i)

    config = sg.UserSettings(
        './settings.ini',
        use_config_file=True,
        convert_bools_and_none=True)

    sg.theme(config['USER SETTING']['theme'])

    INPUTBOX = 9
    BUTTONWIDTH = 25
    BUTTONHAIGHT = 2
    DATETIMEBOX = 4
    SUMPLADIS = 55
    
    # PySimpleGUIレイアウト設定
    windowlayout = [
        [sg.MenubarCustom(
            [
                ['File', ['テンプレートとして登録', '&Exit']],
                ['Edit', ['Theme', [theme_list], 'ThemePreview',
                          '設定ファイルを編集', 'テンプレートファイルを編集']],
                ['Help', ['How To', 'GitHub']]
            ]
        )],
        [
            sg.Text('', size=INPUTBOX),
            sg.ButtonMenu(
                'テンプレートから選択',
                [
                    'dummy', tempkeys
                ],
                key='buttonmenu'
            ),
            sg.Button(key='voiceInput',
                      image_filename='./img/mikeIcon.png'),

        ],
        [
            sg.Text('概要', size=(INPUTBOX)),
            sg.InputText('', size=(SUMPLADIS), key='summary')],
        [
            sg.Text(
                '場所',
                size=(INPUTBOX)
            ),
            sg.InputText(
                '',
                size=(SUMPLADIS),
                key='location'
            )
        ],
        [
            sg.Text(
                '説明',
                size=(INPUTBOX)
            ),
            sg.InputText(
                '',
                size=(SUMPLADIS),
                key=('description')
            )
        ],
        [
            sg.Text(
                '開始日時',
                size=(INPUTBOX)
            ),
            sg.InputText(
                this_year(),
                size=(DATETIMEBOX),
                key='startYear'
            ),
            sg.Text('/'),
            sg.InputText(
                this_month(),
                size=(DATETIMEBOX),
                key=('startMonth')
            ),
            sg.Text('/'),
            sg.InputText(
                today(),
                size=(DATETIMEBOX),
                key=('startDate')
            ),
            sg.Button(
                'カレンダーから選択',
                key='Multiplecalendar',
                size=(15, 1)
            )
        ],
        [
            sg.Text(
                '',
                size=(INPUTBOX)
            ),
            sg.InputText(
                '',
                size=(DATETIMEBOX),
                key=('startHour')
            ),
            sg.Text(':'),
            sg.InputText('', size=(DATETIMEBOX), key=('startMinute')),
            sg.Checkbox('終日', key='allDay')
        ],
        [
            sg.Text('', size=(INPUTBOX)),
            sg.Text('↓↓↓')],
        [
            sg.Text('終了日時', size=(INPUTBOX)),
            sg.InputText(
                this_year(),
                size=(DATETIMEBOX),
                key='endYear'
            ),
            sg.Text('/', ),
            sg.InputText(
                this_month(),
                size=(DATETIMEBOX),
                key=('endMonth')
            ),
            sg.Text('/', ),
            sg.InputText(
                today(),
                size=(DATETIMEBOX),
                key=('endDate')
            )
        ],
        [
            sg.Text('', size=(INPUTBOX)),
            sg.InputText(
                '',
                size=(DATETIMEBOX),
                key=('endHour')
            ),
            sg.Text(':'),
            sg.InputText(
                '',
                size=(DATETIMEBOX),
                key='endMinute'
            )
        ],
        [sg.Text(size=(98), key=('result'))],
        [
            sg.Button(
                '登録',
                key='Submit',
                size=(BUTTONWIDTH, BUTTONHAIGHT)
            ),
            sg.Button(
                '取消',
                key='Cancell',
                size=(BUTTONWIDTH, BUTTONHAIGHT)
            )
        ]
    ]
    # トークンないバージョンもあるので注意
    window = sg.Window('GCalendarClient', windowlayout,
                       resizable=True, size=(450, 350))

    return window


def makewindow_notoken():
    import theme_list
    theme_list = theme_list.theme_list

    with open('./ScheduleTemps.json', 'r', encoding='utf-8') as j:
        temps = json.load(j)
    tempkeys = []
    for i in temps['scheduletemps'].keys():
        tempkeys.append(i)

    config = sg.UserSettings(
        './settings.ini',
        use_config_file=True,
        convert_bools_and_none=True)

    sg.theme(config['USER SETTING']['theme'])

    INPUTBOX = 9
    BUTTONWIDTH = 50
    BUTTONHAIGHT = 2
    DATETIMEBOX = 4
    # PySimpleGUIレイアウト設定
    windowlayout = [
        [sg.MenubarCustom(
            [
                ['File', ['テンプレートとして登録', '&Exit']],
                ['Edit', ['Theme', [theme_list], 'ThemePreview',
                          '設定ファイルを編集', 'テンプレートファイルを編集']],
                ['Help', ['How To', 'GitHub']]
            ]
        )],
        [
            sg.Text('', size=INPUTBOX),
            sg.ButtonMenu(
                'テンプレートから選択',
                [
                    'dummy', tempkeys
                ],
                key='buttonmenu'
            ),
            sg.Button(key='voiceInput',
                      image_filename='./img/mikeIcon.png'),

        ],
        [
            sg.Text('概要', size=(INPUTBOX)),
            sg.InputText('', size=(98), key='summary')],
        [
            sg.Text(
                '場所',
                size=(INPUTBOX)
            ),
            sg.InputText(
                '',
                size=(98),
                key='location'
            )
        ],
        [
            sg.Text(
                '説明',
                size=(INPUTBOX)
            ),
            sg.InputText(
                '',
                size=(98),
                key=('description')
            )
        ],
        [
            sg.Text(
                '開始日時',
                size=(INPUTBOX)
            ),
            sg.InputText(
                this_year(),
                size=(DATETIMEBOX),
                key='startYear'
            ),
            sg.Text('/'),
            sg.InputText(
                this_month(),
                size=(DATETIMEBOX),
                key=('startMonth')
            ),
            sg.Text('/'),
            sg.InputText(
                today(),
                size=(DATETIMEBOX),
                key=('startDate')
            ),
            sg.Button(
                'カレンダーから選択',
                key='Multiplecalendar',
                size=(15, 1)
            )
        ],
        [
            sg.Text(
                '',
                size=(INPUTBOX)
            ),
            sg.InputText(
                '',
                size=(DATETIMEBOX),
                key=('startHour')
            ),
            sg.Text(':'),
            sg.InputText('', size=(DATETIMEBOX), key=('startMinute')),
            sg.Checkbox('終日', key='allDay')
        ],
        [
            sg.Text('', size=(INPUTBOX)),
            sg.Text('↓↓↓')],
        [
            sg.Text('終了日時', size=(INPUTBOX)),
            sg.InputText(
                this_year(),
                size=(DATETIMEBOX),
                key='endYear'
            ),
            sg.Text('/', ),
            sg.InputText(
                this_month(),
                size=(DATETIMEBOX),
                key=('endMonth')
            ),
            sg.Text('/', ),
            sg.InputText(
                today(),
                size=(DATETIMEBOX),
                key=('endDate')
            )
        ],
        [
            sg.Text('', size=(INPUTBOX)),
            sg.InputText(
                '',
                size=(DATETIMEBOX),
                key=('endHour')
            ),
            sg.Text(':'),
            sg.InputText(
                '',
                size=(DATETIMEBOX),
                key='endMinute'
            )
        ],
        [sg.Text(size=(98), key=('result'))],
        [
            sg.Button(
                image_filename='./img/btn_google_signin_dark_pressed_web.png',
                key='Submit',
                size=(BUTTONWIDTH, BUTTONHAIGHT)
            ),
            sg.Button(
                '取消',
                key='Cancell',
                size=(24, 2)
            )
        ]
    ]

    # トークンあるバージョンの行もあるので注意
    window = sg.Window('GCalendarClient', windowlayout,
                       resizable=True, size=(450, 350))

    return window


if __name__ == '__main__':
    makewindow()
