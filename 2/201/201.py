'''
TQC+ 網頁資料擷取與分析 Python 201 搜尋字詞

1. 題目說明:
請開啟PYD02.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA02.py再進行評分。

2. 設計說明：
請撰寫一程式，爬取https://www.codejudger.com/target/5201.html，程式須回傳下列資訊：
讓使用者輸入欲搜尋的字詞，再輸出字詞的搜尋結果及字詞出現的次數。

3. 輸入輸出：
輸入說明
爬取網頁
搜尋的字詞

輸出說明
字詞的搜尋結果
字詞出現的次數

範例輸入及輸出
請輸入欲搜尋的字串 : TQC
TQC 搜尋成功
TQC 出現 23 次
'''

# 載入模組
import requests
import re

url = 'https://www.codejudger.com/target/5201.html'

# 使用 GET 請求
htmlfile = requests.get(url)
# 驗證HTTP Status Code
if htmlfile.status_code == 200:
    # 欲搜尋的字串
    s = input("請輸入欲搜尋的字串 : ")
    l = re.findall(s, htmlfile.text)
    if s in htmlfile.text:
        print(s, "搜尋成功")
        print(s, "出現 %d 次" % len(l))
    else:
        print(s, "搜尋失敗")
        print(s, "出現 0 次")
else:
    print("網頁下載失敗")
