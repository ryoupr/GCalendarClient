# token.pickle
import datetime
from lib2to3.pgen2 import token
import os


def tExpiration_check():
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
            print(diff)
            if diff < -7:
                os.remove('./token.pickle')
    except:
        return


if __name__ == "__main__":
    tExpiration_check()
