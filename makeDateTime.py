def makeDateTime(date, time):
    datetime = str(date) + "T" + str(time)
    return datetime

def main():
    date = "2020-07-10"
    time = "20:10:00"
    dateTime = makeDateTime(date,time)
    print(dateTime)

if __name__ == "__main__":
    main()