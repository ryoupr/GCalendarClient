def take_month_and_date_from_text(text):
    from datetime import datetime
    material = text

    # リターンする情報用の辞書（ここにイベントの情報を投入していく）
    eventdata = {
        'year': '',
        'month': '',
        'date': ''
    }
    one_to_nine = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 月情報の抽出
    for i in text:
        if i == '月' and text[text.index(i)-1] in one_to_nine:
            month_index = text.index(i)
            print(f'month_index = {month_index}')
            if month_index >= 2:
                month = text[month_index-2]+text[month_index-1]
            else:
                month = text[month_index-1]
            print(month[0])
            if month[0] not in one_to_nine:
                month = month[1:]
            print(month)
            eventdata['month'] = str(month)
    # 日付情報の抽出
    # テキストから月の情報を削除
    monthslist = ['12月', '11月', '10月', '9月', '8月',
                  '7月', '6月', '5月', '4月', '3月', '2月', '1月']
    for i in monthslist:
        text = text.replace(i, '')
    print(f'text = {text}')

    date = []

    # ３１日まであるかどうか分岐
    if eventdata['month'] in ['2', '4', '6', '9', '11']:
        # 30日までの場合
        for i in reversed(range(1, 30)):
            if str(i) in str(text):
                date.append(str(i))
                text = text.replace(str(i), '')
    else:
        # 31までの場合
        for i in reversed(range(1, 31)):
            if str(i) in str(text):
                date.append(str(i))
                text = text.replace(str(i), '')

    eventdata['date'] = list(reversed(date))

    if eventdata['month'] == '' and '今月' in material:
        eventdata['month'] = str(datetime.today().month)

    if eventdata['month'] == '' and '来月' in material:
        eventdata['month'] = str((datetime.today().month+1) % 12)

    # monthを日付の要素数と同一になるよう複製
    addtemp = ','+eventdata['month']
    addcount = len(eventdata['date'])-1
    for i in range(0, addcount):
        eventdata['month'] += addtemp

    # yearを日付の要素数と同じになるよう生成（今年）
    thisyear = str(datetime.today().year)
    addtemp = ','+thisyear
    year = thisyear
    for i in range(0,len(eventdata['date'])-1):
        year += addtemp
    
    eventdata['year'] = year
    
    return eventdata



if __name__ == '__main__':
    print(take_month_and_date_from_text('11月のアルバイトは1日9日10日25日です'))
