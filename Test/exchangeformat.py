material = [(2022, 7, 26), (2023, 7, 5), (2024, 7, 12), (2024, 7, 19)]


def betweenOneYear(years):
    for i in range(0, len(years)):
        if years[0] != years[i]:
            return False
    return True

def makeSubmitFormat(years):
    mat = str(years)
    mat = mat[1:]
    mat = mat[:-1]
    return mat

years = []
months = []
dates = []

for i in range(0, len(material)):
    years.append(material[i][0])
    months.append(material[i][1])
    dates.append(material[i][2])

if __name__ == '__main__':
    # print(f'material = {material}')
    # print(f'years = {years}')
    # print(f'months = {months}')
    # print(f'dates = {dates}')
    print(f'submit format years = {makeSubmitFormat(years)}')
    print(f'submit format months = {makeSubmitFormat(months)}')
    print(f'submit format dates = {makeSubmitFormat(dates)}')