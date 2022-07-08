
# def generateDateTimeFromUserImput(year, month, date, hour, minute):
def generate_datetime(year, month, date, hour, minute):
    # Goal generate yyyy-mm-ddThh:mm:ss(ss = 00)
    datetime = f'{year}-{month}-{date}T{hour}:{minute}:00'
    return datetime


def make_datetime(date, time):
    datetime = str(date) + 'T' + str(time)
    return datetime


def main():
    date = '2020-07-10'
    time = '20:10:00'
    print('make_datetime(date, time)')
    print(make_datetime(date, time))
    print("generate_datetime('2000', '07', '10', '12', '00')")
    print(generate_datetime('2000', '07', '10', '12', '00'))


if __name__ == '__main__':
    main()
