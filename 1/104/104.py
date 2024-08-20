'''
TQC+ 網頁資料擷取與分析 Python 104 JSON檔案輸出處理

1. 題目說明:
請開啟PYD01.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA01.py再進行評分。

2. 設計說明：
請撰寫一程式，建立以下資料並將其輸出為write.json檔案：

{
'people' :
[{  
    'id': '1',
    'name': 'Peter',
    'country': 'Taiwan'
},
{  
    'id': '2',
    'name': 'Jack',
    'country': 'USA'
},
{  
    'id': '3',
    'name': 'Cindy',
    'country': 'Japan'
}]
}

3. 輸入輸出：
輸入說明
無

輸出說明
將資料輸出至write.json

範例輸入
無

範例輸出
https://i.imgur.com/c06G8ia.png
'''

# 載入 json 模組
import json


# 建立資料
data = {
    'people': [
        {
            'id': '1',
            'name': 'Peter',
            'country': 'Taiwan'
        },
        {
            'id': '2',
            'name': 'Jack',
            'country': 'USA'
        },
        {
            'id': '3',
            'name': 'Cindy',
            'country': 'Japan'
        }
    ]
}

# 將資料寫入json檔案
with open('write.json', 'w') as outfile:
    json.dump(data, outfile)

