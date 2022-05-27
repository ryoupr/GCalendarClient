
import datetime


def thisYear():
    now = str(datetime.date.today())
    thisYear = now[0]+now[1]+now[2]+now[3]
    return thisYear


def thisMonth():
    now = str(datetime.date.today())
    thisMonth = now[5]+now[6]
    return thisMonth


def today():
    now = str(datetime.date.today())
    today = now[8]+now[9]
    return today


def generateDate(year, month, date):
    date = f"{year}-{month}-{date}"
    return date


if __name__ == "__main__":
    print("Functions return.")
    print("thisYear     "+str(thisYear()))
    print("thisMonth    "+str(thisMonth()))
    print("today        "+str(today()))
    print("generateDate "+generateDate("2000","07","10"))
