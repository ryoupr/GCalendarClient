from datetime import date


def dateFormatCheck(date):
    checkSum = 0
    if len(date) != 10:
        return(0)
    for i in range(0, 10):
        if i == 4 or i == 7:
            if date[i] == "-":
                checkSum += 1
        if date[i].isdecimal():
            checkSum += 1
        if checkSum == 10:
            return(1)
        elif i == 9:
            return(0)


def main():
    dateFlag = 0
    while dateFlag == 0:
        startDate = input("Start date(yyyy-mm-dd):")
        dateFlag = dateFormatCheck(startDate)
        if dateFlag == 1:
            break
        else:
            print("Invalid format. Please enter again.")

if __name__ == "__main__":
    main()

