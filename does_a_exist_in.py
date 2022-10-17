def does_a_exist_in(text, temps):
    text = str(text)
    for i in temps:
        if i in text:
            return True , i
    return False,''


if __name__ == '__main__':
    print(does_a_exist_in('今月のバイトは', ['asss', 'grdfg','バイト']))
    #True Falseのみ出力
    print(does_a_exist_in('今月のバイトは', ['asss', 'grdfg','バイト'])[0])
    #見つけたテンプレートのサマリー
    print(does_a_exist_in('今月のバイトは', ['asss', 'grdfg','バイト'])[1])
