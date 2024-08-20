'''
TQC+ 網頁資料擷取與分析 Python 103 勞保投保薪資分級表

1. 題目說明:
請開啟PYD01.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA01.py再進行評分。

程式所產出的檔案，須輸出與程式同一層資料夾。

2. 設計說明：
請撰寫一程式，讀取勞保投保薪資分級表read.json內的資料後，將資料轉存為write.yaml。

3. 輸入輸出：
輸入說明
讀取read.json

輸出說明
將資料輸出至write.yaml

範例輸入
無

範例輸出
https://i.imgur.com/yUDhxMA.png
'''

# 載入 yaml 與 json 模組
import yaml
import json

# 讀取 json 檔案
with open("read.json", encoding='utf-8-sig') as file:
    data = json.load(file)

# 寫入 yaml 檔案
with open("write.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
