# GCalendarClient

ようこそGCalendarClientへ、このソフトウェアを使用することで GoogleCalendar への予定登録をさらに効率的に行えるようになります。
アルバイトなどの不定期に起こる予定の登録にご活用ください。

## 一つの予定を複数日程へ追加
![複数日程追加](https://user-images.githubusercontent.com/55190661/182026090-f16fb1e9-929d-45d9-8781-fe5a011ef7f0.png)
![複数日程追加結果](https://user-images.githubusercontent.com/55190661/182026099-ec2bc522-e26f-4f44-92bf-3c71719c9922.png)

日付欄をカンマ区切りで入力することで一括で複数日の不規則な予定を簡単に登録することができます。
これらは時間でも同様です。

## カレンダーからグラフィカルに指定することもできます

![カレンダーから選択協調画面](https://user-images.githubusercontent.com/55190661/182070202-4d5da4ec-0918-4592-82cc-11aa1fc49c01.png)
![image](https://user-images.githubusercontent.com/55190661/182070278-1c83f738-ac73-4f0d-a474-a7d1aa2e16ae.png)　　

カレンダーから選択ボタンを押下することで、グラフィカルに予定を追加する日を指定することができます。

## 頻繁に登録する予定をテンプレートとして登録できます。
![usetemplate](https://user-images.githubusercontent.com/55190661/184474412-da2d2223-bb74-4543-ae07-6c2ac9d3891c.png)
![pushtemp](https://user-images.githubusercontent.com/55190661/184474456-024abb86-18a7-4691-823f-b4c8afd61492.png)  
テンプレートは予定情報が入力された状態で左上のメニューからFile→テンプレートとして登録を選択することで登録できます。（次回起動時から選択可能です）

## 登録先カレンダーの変更
![image](https://user-images.githubusercontent.com/55190661/182026178-e9cba667-cd13-4947-871a-456f2f93efc1.png)

登録先のカレンダーは setting.ini の calendarID を変更することで変更できます。
カレンダー ID は GoogleCalendar の設定画面から取得することができます。（デフォルトでは[テスト用のカレンダー](https://calendar.google.com/calendar/u/0?cid=a2UzN2Qxb2Jrb2E5aWhiamdobmM1MnVpNTRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)に接続するように設定されています）
