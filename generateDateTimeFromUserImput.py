
def generateDateTimeFromUserImput(year,month,date,hour,minute):
    #Goal generate yyyy-mm-ddThh:mm:ss(ss = 00)
    datetime = f"{year}-{month}-{date}T{hour}:{minute}:00"
    return datetime

if __name__ == "__main__":
    print(generateDateTimeFromUserImput("2000","07","10","12","00"))