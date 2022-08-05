import datetime
from calendar import Calendar
import PySimpleGUI as sg


def get_dates(selected=set()):

    sg.theme('DarkBlue3')
    sg.set_options(font=('Courier New', 12, 'bold'))

    def update_calendar(year, month, days):
        window['Month'].update(f'{months_in_year[month-1]}')
        window['Year'].update(f'{year}')
        for row in range(6):
            for col in range(7):
                m, d = days[row * 7 + col]
                window[('Date', row, col)].update(d, text_color=white if m == month else gray,
                                                  background_color='blue' if d != '' and (year, m, int(d)) in selected else sg.theme_background_color())
                window[('Date', row, col)
                       ].metadata = False if m == month else 'gray'

    months_in_year = ['１月', '２月', '３月', '４月', '５月', '６月', '７月',
                      '８月', '９月', '１０月', '１１月', '１２月']

    today = datetime.datetime.now()
    year, month, day = today.year, today.month, today.day

    calendar = Calendar(firstweekday=6)     # First week day is sunday
    days = [(d.month, f'{d.day:>2d}')
            for d in calendar.itermonthdates(year=year, month=month)]
    days += [(None, '')] * (42-len(days))

    white, gray = '#FFFFFF', '#8699AF'
    bg = [sg.theme_background_color(), 'blue']

    selected = set()

    layout = [
        [sg.Text(f'{year}', key='Year'),
         sg.Text(sg.SYMBOL_DOWN, size=3, justification='center',
                 background_color='green', enable_events=True, key='Year_DN'),
         sg.Text(sg.SYMBOL_UP, size=3, justification='center',
                 background_color='green', enable_events=True, key='Year_UP'),
         sg.Push(),
         sg.Text(f'{months_in_year[month-1]}', key='Month'),
         sg.Text(sg.SYMBOL_DOWN, size=3, justification='center',
                 background_color='green', enable_events=True, key='Month_DN'),
         sg.Text(sg.SYMBOL_UP, size=3, justification='center', background_color='green', enable_events=True, key='Month_UP')],
        [sg.Text()],
        [sg.Text(weekday, size=4, justification='center')
            for weekday in ('日', '月', '火', '水', '木', '金', '土')]]

    weeks = []
    for row in range(6):
        week = []
        for col in range(7):
            m, d = days[row * 7 + col]
            week.append(
                sg.Text(d, size=4, justification='center',
                        text_color=white if m == month else gray,
                        background_color='blue' if (year, m, int(
                            d)) in selected else sg.theme_background_color(),
                        enable_events=True,
                        metadata=False if m == month else 'gray', key=('Date', row, col)))
        weeks.append(week)
    layout += weeks + [[sg.Push(), sg.Button('OK')]]
    window = sg.Window('Calendar', layout, modal=True, )

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            selected = set()
            break
        elif event == 'OK':
            break
        elif isinstance(event, tuple) and event[0] == 'Date':
            _, row, col = event
            m, d = days[row * 7 + col]
            if window[event].metadata != 'gray':
                window[event].metadata = not window[event].metadata
                window[event].update(
                    background_color=bg[window[event].metadata])
                if window[event].metadata:
                    selected.add((year, m, int(d)))
                else:
                    selected.remove((year, m, int(d)))
        elif event in ('Month_UP', 'Month_DN', 'Year_UP', 'Year_DN'):
            delta = -1 if event.endswith('UP') else 1
            if event.startswith('Month'):
                m = month + delta
                year, month = (year-1, 12) if m < 1 else (year +
                                                          1, 1) if m > 12 else (year, m)
            else:
                year += delta
            days = [(d.month, f'{d.day:>2d}')
                    for d in calendar.itermonthdates(year=year, month=month)]
            days += [(None, '')] * (42-len(days))
            update_calendar(year, month, days)

    window.close()
    return list(selected)


if __name__ == '__main__':
    print(get_dates())
