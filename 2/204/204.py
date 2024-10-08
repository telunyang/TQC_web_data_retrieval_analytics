'''
TQC+ 網頁資料擷取與分析 Python 204 新北市大專院校名單

1. 題目說明:
請開啟PYD02.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA02.py再進行評分。

2. 設計說明：
(1) 請撰寫一程式，爬取新北市大專院校名單，API連結如下：https://www.codejudger.com/target/5204.json
(2) 程式須輸出：新北市每一所大專院校的相關訊息：名稱、地址、聯絡電話、網站、資料更新時間。

3. 輸入輸出：
輸入說明
爬取API資料

輸出說明
新北市每一所大專院校的相關訊息：名稱、地址、聯絡電話、網站、資料更新時間

範例輸入
無

範例輸出
新北市大專院校名單：

名稱：馬偕醫專三芝校區
地址：新北市三芝區中正路三段42號
聯絡電話：02-26366799
網站：www.mkc.edu.tw
資料更新時間：2018-09-12 06:00:01.0

名稱：馬偕醫學院
地址：新北市三芝區中正路三段46號
聯絡電話：02-26360303
網站：www.mmc.edu.tw
資料更新時間：2018-09-12 06:00:01.0

名稱：法鼓大學
地址：新北市金山區
聯絡電話：
網站：www.ddc.edu.tw/zh-tw
資料更新時間：2018-09-12 06:00:01.0
'''

# 載入 requests 模組
import requests
# 載入 json 模組
import json

# 開放資料連結
url = 'https://www.codejudger.com/target/5204.json'
# 以 requests 模組發出 HTTP GET 請求
res = requests.get(url)

# 將回傳結果轉換成標準JSON格式
data = json.loads(res.text)

# 輸出新北市大專院校名單
print('新北市大專院校名單：\n')
for record in data:
    if record['type'] == '大專院校':
        print('名稱：%s' % record['name'])
        print('地址：%s' % record['address'])
        print('聯絡電話：%s' % record['tel'])
        print('網站：%s' % record['website'])
        print('資料更新時間：%s' % record['update_date'])
        print()
