from audioop import add
from stringprep import in_table_c9
from tracemalloc import start
from datetime_master import *
from verify_format import verify_all_day_event


def include_conma(mat):
    for i in mat:
        if i == ',':
            return True
    else:
        return False


# テスト用values
values = {'summary': '概要', 'location': '場所', 'description': '説明', 'startYear': '2022', 'startMonth': '07', 'startDate': '08,21,25', 'startHour': '',
          'startMinute': '', 'allDay': True, 'endYear': '2022', 'endMonth': '07', 'endDate': '08,21,25', 'endHour': '', 'endMinute': ''}


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
        print('終日イベント')
        # カンマ区切りでリストを作成
        startdates = values['startDate'].split(',')
        print(startdates)
        enddates = values['endDate'].split(',')
        print(enddates)
        # forで回しながら予定を追加
        for i in range(0, len(startdates)):
            calendarEvent['summary'] = values['summary']
            calendarEvent['location'] = values['location']
            calendarEvent['description'] = values['description']
            calendarEvent['start']['date'] = generate_date(
                values['startYear'], values['startMonth'], startdates[i])
            calendarEvent['end']['date'] = generate_date(
                values['endYear'], values['endMonth'], enddates[i]
            )
            print(calendarEvent)
            if verify_all_day_event(values):
                #todo スケジュールの登録
                pass
    else:
        # 非終日イベント
        print('非終日イベント')


if __name__ == '__main__':
    add_schedules(values)
