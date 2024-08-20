'''
TQC+ 網頁資料擷取與分析 Python 205 空氣品質指標（AQI）

1. 題目說明:
請開啟PYD02.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA02.py再進行評分。

2. 設計說明：
(1) 請撰寫一程式，爬取政府AQI開放資料，API連結：https://www.codejudger.com/target/5205.json

(2) 程式須回傳下列資訊：

內容長度
新北市每一個地區的相關訊息：地區名稱、AQI指數、PM2.5指數、PM10指數、資料更新時間；
在輸出時，AQI指數、PM2.5指數、PM10指數與資料更新時間四項資訊前加入一個 tab 鍵（\t）
3. 輸入輸出：
輸入說明
爬取API資料

輸出說明
內容長度
新北市每一個地區的相關訊息：地區名稱、AQI指數、PM2.5指數、PM10指數、資料更新時間
在輸出時，AQI指數、PM2.5指數、PM10指數與資料更新時間四項資訊前加入一個 tab 鍵（\t）
範例輸入
無

範例輸出
Content-Length: 37985

新北市PM2.5相關資料：
汐止：
        AQI：36
        PM2.5：16
        PM10：36
        資料更新時間：2018-06-27 13:00
萬里：
        AQI：49
        PM2.5：10
        PM10：20
        資料更新時間：2018-06-27 13:00
新店：
        AQI：45
        PM2.5：22
        PM10：22
        資料更新時間：2018-06-27 13:00
土城：
        AQI：60
        PM2.5：20
        PM10：32
        資料更新時間：2018-06-27 13:00
板橋：
        AQI：38
        PM2.5：15
        PM10：42
        資料更新時間：2018-06-27 13:00
新莊：
        AQI：42
        PM2.5：12
        PM10：27
        資料更新時間：2018-06-27 13:00
菜寮：
        AQI：60
        PM2.5：20
        PM10：32
        資料更新時間：2018-06-27 13:00
林口：
        AQI：58
        PM2.5：19
        PM10：27
        資料更新時間：2018-06-27 13:00
淡水：
        AQI：40
        PM2.5：10
        PM10：16
        資料更新時間：2018-06-27 13:00
三重：
        AQI：60
        PM2.5：19
        PM10：62
        資料更新時間：2018-06-27 13:00
永和：
        AQI：50
        PM2.5：21
        PM10：35
        資料更新時間：2018-06-27 13:00
富貴角：
        AQI：42
        PM2.5：
        PM10：11
        資料更新時間：2018-06-27 13:00
'''

# 載入 requests 與 json 模組
import requests
import json

# 開放資料Json格式連結
url = 'https://www.codejudger.com/target/5205.json'
# 發出Get請求
response = requests.get(url)
# 回傳內容長度
print('Content-Length:', len(response.content))
# 將取得的回傳內容轉換成Json格式
response = json.loads(response.text)

print()

# 顯示新北市每一個地區的PM2.5相關資料
print('新北市PM2.5相關資料：')
for record in response:
    if record['County'] == '新北市':
        print('%s：' % record['SiteName'])
        print('\tAQI：%s' % record['AQI'])
        print('\tPM2.5：%s' % record['PM2.5'])
        print('\tPM10：%s' % record['PM10'])
        print('\t資料更新時間：%s' % record['PublishTime'])
