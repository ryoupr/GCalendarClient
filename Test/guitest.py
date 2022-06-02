import PySimpleGUI as sg

sg.theme('SystemDefault')
layout = [[sg.Text('Windowアイコンサンプル')]]

window = sg.Window('アイコン', layout=layout,
                   icon='./calendarIcon.png')
# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
