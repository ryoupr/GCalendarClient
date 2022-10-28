# token.pickle
import datetime
from lib2to3.pgen2 import token
import os


def check_token_expiration():
    try:
        # 現在日時を取得
        now = datetime.datetime.now()
        # ファイルの作成日時を取得
        metaTime = os.path.getmtime('./token.pickle')
        genD = datetime.datetime.fromtimestamp(metaTime)
        # 作成したのが何日前かを求める
        diff = genD.date() - now.date()
        diff = str(diff).split(' ')[0]
        # 一週間以上経過していればファイルを削除
        if str(diff) != '0:00:00':
            diff = int(diff)
            print(f'前回のトークン作成から{diff*-1}日が経過しています')
            if diff <= -7:
                print('前回作成から7日以上経過していたのでトークンを削除します')
                os.remove('./token.pickle')
                print('削除完了')
    except:
        print('Error in check token')
        return


if __name__ == '__main__':
    check_token_expiration()
