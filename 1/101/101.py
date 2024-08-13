'''
1. 題目說明:
請開啟PYD01.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA01.py再進行評分。

程式所產出的檔案，須輸出與程式同一層資料夾。

2. 設計說明：
請撰寫一程式，讀取文化部展覽資訊read.json，請將其中title（活動名稱）、showUnit（演出單位）、startDate（活動起始日期）、endDate（活動結束日期）等四個欄位內容轉存為write.csv (需為UTF-8編碼格式)，各欄位內容之間以一個半形逗號隔開。

提示：只需要輸出資料，不需要輸出欄位名稱。

3. 輸入輸出：
輸入說明
讀取read.json

輸出說明
將四個欄位的內容：title、showUnit、startDate、endDate，輸出至write.csv檔案，各欄位內容之間以一個半形逗號隔開

範例輸入
無

範例輸出
https://i.imgur.com/QJiwndh.png
'''

# 載入 json 與 csv 模組
import ___
import ___

# 讀取 json 檔案並指定編碼為 utf8
with ___("___", encoding='___') as file:
    data = json.load(file)

# 寫入 csv 檔案並指定編碼為 utf8
with ___("___", "___", encoding='___') as file:
    csv_file = csv.writer(file)
    # 寫入 title（活動名稱）、showUnit（演出單位）、startDate（活動起始日期）、endDate（活動結束日期）等四個欄位
    for item in data:
        csv_file.writerow([___['___'], ___['___'],
                           ___['___'], ___['___']])
