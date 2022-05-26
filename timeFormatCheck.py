def timeFormatCheck(time):
    checkSum = 0
    if len(time) != 5:
        return(0)
    for i in range(0, 5):
        if i == 2 and time[i] == ":":
            checkSum += 1
        if time[i].isdecimal():
            checkSum += 1
        if checkSum == 5:
            return(1)
        elif i == 4:
            return(0)


def main():
    timeFlag = 0
    while timeFlag == 0:
        startTime = input("Start time(hh:mm)")
        timeFlag = timeFormatCheck(startTime)
        if timeFlag == 1:
            startTime += ":00"
            break
        else:
            print("Invalid format. Please enter again.")


if __name__ == "__main__":
    main()
