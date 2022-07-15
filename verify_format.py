from operator import truediv
from sqlite3 import Date
from ssl import VerifyFlags
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


def verify_all_day_event(values):
    is_verified = False
    verify_flags = {'IS_VERIFIED_START_YEAR': '', 'IS_VERIFIED_START_MONTH': '', 'IS_VERIFIED_START_DATE': '',
                    'IS_VERIFIED_END_YEAR': '', 'IS_VERIFIED_END_MONTH': '', 'IS_VERIFIED_END_DATE': ''}
    verify_flags['IS_VERIFIED_START_YEAR'] = verify_year(values['startYear'])
    # 検証用辞書の中にFalseが一つもなければ続行
    if False not in verify_flags.values():
        verify_flags['IS_VERIFIED_START_MONTH'] = verify_month(
            values['startYear'], values['startMonth'])
    if False not in verify_flags.values():
        verify_flags['IS_VERIFIED_START_DATE'] = verify_start_date(
            values['startYear'], values['startMonth'], values['startDate'])
    if False not in verify_flags.values():
        verify_flags['IS_VERIFIED_END_YEAR'] = verify_end_year(
            values['startYear'], values['endYear'])
    if False not in verify_flags.values():
        verify_flags['IS_VERIFIED_END_MONTH'] = verify_end_month(
            values['startYear'], values['endYear'], values['startMonth'], values['endMonth'])
    if False not in verify_flags.values():
        verify_flags['IS_VERIFIED_END_DATE'] = verify_end_date(
            values['startYear'], values['endYear'], values['startMonth'], values['endMonth'], values['startDate'], values['endDate'])
    if False not in verify_flags.values():
        return True
    else:
        return False



if __name__ == '__main__':
    here_is = '検証用エリア'