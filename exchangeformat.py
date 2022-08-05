from optparse import Values


def makeSubmitFormat(years):
    mat = str(years)
    mat = mat[1:]
    mat = mat[:-1]
    return mat

def exchangeFormat(mat):
    years = []
    months = []
    dates = []

    for i in range(0, len(mat)):
        years.append(mat[i][0])
        months.append(mat[i][1])
        dates.append(mat[i][2])
    years = ''.join(makeSubmitFormat(years).split())
    months = ''.join(makeSubmitFormat(months).split())
    dates = ''.join(makeSubmitFormat(dates).split())
    return years,months,dates

if __name__ == '__main__':
    material = [(2022, 8, 16), (2022, 8, 23)]
    years,months,dates = exchangeFormat(material)
    print(years)
    print(months)
    print(dates)
    pass