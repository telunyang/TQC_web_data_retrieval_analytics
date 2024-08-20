'''
TQC+ 網頁資料擷取與分析 Python 105 受僱員工資料表

1. 題目說明:
請開啟PYD01.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA01.py再進行評分。

2. 設計說明：
請撰寫一程式連結read.db資料庫，讀取Employee資料表，輸出Employee資料表內的資料。

3. 輸入輸出：
輸入說明
無

輸出說明
輸出Employee資料表內的資料

範例輸入
無

範例輸出
(1, '小陳', 1997, '新北市', 58000)
(2, '小范', 2000, '臺北市', 50000)
(3, '小施', 1999, '高雄市', 47000)
(4, '小吳', 1998, '台中市', 52000)

資料庫內容：
https://i.imgur.com/6eFUaNA.png
'''

# 載入 sqlite3 模組
import sqlite3

# 建立資料庫連結
con = sqlite3.connect('read.db')
# 建立cursor物件
cur = con.cursor()

# 查詢Employee資料表
cur.execute("SELECT * FROM Employee")

# 印出查詢結果
for t in cur.fetchall():
    print(t)

# 關閉與資料庫的連結
con.close()
