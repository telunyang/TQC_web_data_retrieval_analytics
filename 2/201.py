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
import ___
import ___

url = '___'

# 使用 GET 請求
htmlfile = requests.___(___)
# 驗證HTTP Status Code
if htmlfile.status_code == ___:
    # 欲搜尋的字串
    ___ = input("請輸入欲搜尋的字串 : ")
    ___ = re.findall(___, htmlfile.text)
    if ___ in htmlfile.text:
        print(___, "搜尋成功")
        print(___, "出現 %d 次" % len(___))
    else:
        print(___, "搜尋失敗")
        print(___, "出現 0 次")
else:
    print("網頁下載失敗")
