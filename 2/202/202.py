'''
TQC+ 網頁資料擷取與分析 Python 202 美元收盤匯率

1. 題目說明:
請開啟PYD02.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA02.py再進行評分。

程式所產出的檔案，須輸出與程式同一層資料夾。

2. 設計說明：
請撰寫一程式，爬取read.html，取得「新臺幣對美元銀行間成交之收盤匯率」資料，並將其中日期、NTD/USD兩個欄位的名稱與資料轉存為write.csv (需為UTF-8編碼格式)。

3. 輸入輸出：
輸入說明
爬取網頁

輸出說明
日期、NTD/USD兩個欄位的名稱與資料，輸出至write.csv

範例輸入
無

範例輸出
https://i.imgur.com/rHM1NcI.png
'''

# 載入 csv 模組
import csv
# 自 urllib.request 模組載入 urlopen 函數
from urllib.request import urlopen
# 自 bs4 模組載入 BeautifulSoup 函數
from bs4 import BeautifulSoup


# 將資料寫入csv檔案，編碼為 utf8
file_name = "write.csv"
f = open(file_name, "w", encoding='utf8')
# 以 csv 模組的 writer 函數初始化寫檔
w = csv.writer(f)

# 爬取的目標網頁
htmlname = "file:./read.html"
# urlopen 函數讀取 html 檔案
html = urlopen(htmlname)
# 指定 BeautifulSoup 的解析器為 lxml
bsObj = BeautifulSoup(html, "lxml")

count = 0
# 將其中日期、NTD/USD 兩個欄位的名稱與資料轉存為csv
# 資料位置
for single_tr in bsObj.find("table", {"class": "DataTable2"}).findAll("tr"):
    if count == 0:
        # 擷取資料位置
        cell = single_tr.findAll("th")
    else:
        # 擷取資料位置
        cell = single_tr.findAll("td")
    F0 = cell[0].text
    F1 = cell[1].text
    data = [[F0, F1]]
    w.writerows(data)
    count = count + 1
f.close()
