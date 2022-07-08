from operator import truediv
from sqlite3 import Date
from datetime_master import *
from calendar import calendar, isleap


def verify_year(y):
    try:
        y = int(y)
        if len(str(y)) != 4:
            return False
        if y < int(this_year()):
            return False
        return True
    except:
        return False


def verify_month(y, m):
    try:
        y = int(y)
        m = int(m)
        # 1~12月の範囲に入っていないものははじく。
        if 0 >= m or 12 < m:
            return False
        if y == int(this_year()) and m < int(this_month()):
            return False
        return True
    except:
        return False


def verify_start_date(y, m, d):
    thirty = [4, 6, 9, 11]
    thirtyone = [1, 3, 5, 7, 8, 10, 12]
    try:
        y, m, d = int(y), int(m), int(d)
        if m == 2:
            if isleap(y):
                if 1 > d or 29 < d:
                    return False
            else:
                if 1 > d or 28 < d:
                    return False
        if m in thirty:
            if 1 > d or 30 < d:
                return False
        if m in thirtyone:
            if 1 > d or 31 < d:
                return False
        if y == int(this_year()) and m == int(this_month()):
            if d < int(today()):
                return False
        return True
    except:
        return False


def verify_end_year(sy, ey):
    try:
        sy, ey = int(sy), int(ey)
        if verify_year(ey):
            if ey < sy:
                return False
            return True
        else:
            return False
    except:
        return False


def verify_end_month(sy, ey, sm, em):
    if verify_month(ey, em):
        sy, ey, sm, em = int(sy), int(ey), int(sm), int(em)
        if sy == ey and sm > em:
            return False
        return True
    else:
        return False


def verify_end_date(sy, ey, sm, em, sd, ed):
    if verify_start_date(ey, em, ed):
        sy, ey, sm, em, sd, ed = int(sy), int(
            ey), int(sm), int(em), int(sd), int(ed)
        if sy == ey and sm == em and sd > ed:
            return False
        return True
    else:
        return False


if __name__ == '__main__':
    year = '2022'
    month = '06'
    date = '03'
    # print(verify_year(year))
    # print(verify_month(year,month))
    # print(verify_start_date(year, month,date))
    # print(verify_end_year('2023','2024'))
    print(verify_end_month('2022', '2023', '06', '05'))
