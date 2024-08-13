'''
TQC+ 網頁資料擷取與分析 Python 302 矩陣

1. 題目說明:
請開啟PYD03.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA03.py再進行評分。

2. 設計說明：
請用numpy隨機產生5~15之間，15個正整數並輸出
請將 1. 轉成3×5的X矩陣並輸出
請輸出X矩陣的最大值
請輸出X矩陣的最小值
請輸出X矩陣的總和
請輸出X矩陣四個角落的元素內容

3. 輸入輸出：
輸入說明
無

輸出說明
請用numpy隨機產生5~15之間，15個正整數並輸出
請將 1. 轉成3×5的X矩陣並輸出
請輸出X矩陣的最大值
請輸出X矩陣的最小值
請輸出X矩陣的總和
請輸出X矩陣四個角落的元素內容

範例輸入
無

範例輸出
隨機正整數： [ 7  7 11  6  8 15 14 11  6  5  6 14  5  5 14]
X矩陣內容：
[[ 7  7 11  6  8]
 [15 14 11  6  5]
 [ 6 14  5  5 14]]
最大： 15
最小： 5
總和： 134
四個角落元素：
[[ 7  8]
 [ 6 14]]
'''

# --開始--批改評分使用，請勿變動
set_seed = 123
# --結束--批改評分使用，請勿變動

import numpy as np

x = np.random.RandomState(set_seed).randint(low=5, high=16, size=15)
print('隨機正整數：', ___)

x = x.reshape(___, ___)
print('X矩陣內容：')
print(___)
print('最大：', ___)
print('最小：', ___)
print('總和：', ___)
print('四個角落元素：')
print(x[np.ix_([___, ___], [___, ___])])
