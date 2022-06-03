from operator import truediv
from sqlite3 import Date
from datetimeMaster import *
from calendar import calendar, isleap


def startYearFC(y):
    try:
        y = int(y)
        if len(str(y)) != 4:
            return False
        if y < int(thisYear()):
            return False
        return True
    except:
        return False


def startMonthFC(y, m):
    try:
        y = int(y)
        m = int(m)
        # 1~12月の範囲に入っていないものははじく。
        if 0 >= m or 12 < m:
            return False
        if y == int(thisYear()) and m < int(thisMonth()):
            return False
        return True
    except:
        return False


def startDateFC(y, m, d):
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
        if y == int(thisYear()) and m == int(thisMonth()):
            if d < int(today()):
                return False
        return True
    except:
        return False


def endYearFC(sy, ey):
    try:
        sy, ey = int(sy), int(ey)
        if startYearFC(ey):
            if ey < sy:
                return False
            return True
        else:
            return False
    except:
        return False


def endMonthFC(sy, ey, sm, em):
    if startMonthFC(ey, em):
        sy, ey, sm, em = int(sy), int(ey), int(sm), int(em)
        if sy == ey and sm > em:
            return False
        return True
    else:
        return False


def endDateFC(sy, ey, sm, em, sd, ed):
    if startDateFC(ey, em, ed):
        sy, ey, sm, em, sd, ed = int(sy), int(
            ey), int(sm), int(em), int(sd), int(ed)
        if sy == ey and sm == em and sd > ed:
            return False
        return True
    else:
        return False


if __name__ == '__main__':
    year = "2022"
    month = "06"
    date = "03"
    # print(startYearFC(year))
    # print(startMonthFC(year,month))
    # print(startDateFC(year, month,date))
    # print(endYearFC("2023","2024"))
    print(endMonthFC("2022", "2023", "06", "05"))
