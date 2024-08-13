'''
TQC+ 網頁資料擷取與分析 Python 102 新北市公共自行車即時資訊

1. 題目說明:
請開啟PYD01.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA01.py再進行評分。

程式所產出的檔案，須輸出與程式同一層資料夾。

2. 設計說明：
請撰寫一程式，讀取新北市公共自行車即時資訊read.xml，請將其中sno（站點代號）、sna（中文場站名稱）、tot（場站總停車格）等三個欄位轉存為write.csv (需為UTF-8編碼格式)，各欄位內容之間以一個半形逗號隔開。

提示：只需要輸出資料，不需要輸出欄位名稱。

3. 輸入輸出：
輸入說明
讀取read.xml

輸出說明
將三個欄位的內容：sno、sna、tot，輸出至write.csv檔案，各欄位內容之間以一個半形逗號隔開

範例輸入
無

範例輸出
https://i.imgur.com/teNT4zC.png
'''

# 載入 xml.etree.ElementTree 模組並縮寫為 ET
import ___ as ___
# 載入 csv 模組
import ___

# 讀取 xml
tree = ___.___("___")
root = tree.getroot()

# 寫入 csv 檔案，編碼設定為 utf8
ubikefile = ___("___", "___", encoding='___')
csvwriter = csv.writer(ubikefile)

# 將其中 sno（站點代號）、sna（中文場站名稱）、tot（場站總停車格）等三個欄位寫出
for row in root:
    ubike = []
    sno = row.find('___').text
    ubike.append(___)
    sna = row.find('___').text
    ubike.append(___)
    tot = row.find('___').text
    ubike.append(___)
    csvwriter.writerow(ubike)
ubikefile.close()
