
import datetime


def thisYear():
    now = str(datetime.date.today())
    thisYear = now[0]+now[1]+now[2]+now[3]
    return thisYear


def thisMonth():
    now = str(datetime.date.today())
    thisMonth = now[5]+now[6]
    return thisMonth

def thisDay():
    now = str(datetime.date.today())
    thisDay = now[8]+now[9]
    return thisDay

if __name__ == "__main__":
    print(thisYear())
    print(thisMonth())
    print(thisDay())
