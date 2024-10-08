'''
TQC+ 網頁資料擷取與分析 Python 304 資料處理與分析

1. 題目說明：
請開啟PYD03.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA03.py再進行評分。

2. 設計說明：
請讀取read.csv中的資料轉換成numpy陣列，並輸出以下資訊：

資料集型態
平均數
中位數
標準差
變異數
極差值
註：數值需四捨五入至小數點後兩位

3. 輸入輸出：
輸入說明
讀取read.csv的內容

輸出說明
資料集型態
平均數
中位數
標準差
變異數
極差值
範例輸入
無

範例輸出
https://i.imgur.com/VbKDve5.png
'''

# 載入 numpy 模組
import numpy as np
# 載入 pandas 模組縮
import pandas as pd

# 讀入 read.csv 檔案
n = np.array(pd.read_csv('read.csv'))

# 判斷資料型態
print('資料型態：%s' % type(n))
# 計算平均數
print('平均值：%.2f' % np.mean(n))
# 計算中位數
print('中位數：%.2f' % np.median(n))
# 計算標準差
print('標準差：%.2f' % np.std(n))
# 計算變異數
print('變異數：%.2f' % np.var(n))
# 計算極差值
print('極差值：%.2f' % (np.max(n) - np.min(n) ))
