
def generateDateTimeFromUserImput(year, month, date, hour, minute):
    # Goal generate yyyy-mm-ddThh:mm:ss(ss = 00)
    datetime = f"{year}-{month}-{date}T{hour}:{minute}:00"
    return datetime


def makeDateTime(date, time):
    datetime = str(date) + "T" + str(time)
    return datetime


def main():
    date = "2020-07-10"
    time = "20:10:00"
    dateTime = makeDateTime(date, time)
    print(dateTime)


if __name__ == "__main__":
    main()
if __name__ == "__main__":
    print(generateDateTimeFromUserImput("2000", "07", "10", "12", "00"))
