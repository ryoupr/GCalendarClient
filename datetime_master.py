
import datetime


def this_year():
    now = str(datetime.date.today())
    this_year = now[0]+now[1]+now[2]+now[3]
    return this_year


def this_month():
    now = str(datetime.date.today())
    this_month = now[5]+now[6]
    return this_month


def today():
    now = str(datetime.date.today())
    today = now[8]+now[9]
    return today


def generateDate(year, month, date):
    date = f'{year}-{month}-{date}'
    return date


if __name__ == '__main__':
    print('Functions return.')
    print('this_year     '+str(this_year()))
    print('this_month    '+str(this_month()))
    print('today        '+str(today()))
    print('generateDate '+generateDate('2000','07','10'))
