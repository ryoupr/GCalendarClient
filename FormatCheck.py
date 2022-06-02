def timeFormatCheck(time):
    checkSum = 0
    if len(time) != 5:
        return(False)
    for i in range(0, 5):
        if i == 2 and time[i] == ":":
            checkSum += 1
        if time[i].isdecimal():
            checkSum += 1
        if checkSum == 5:
            return(1)
        elif i == 4:
            return(0)


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
