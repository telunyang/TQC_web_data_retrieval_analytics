'''
TQC+ 網頁資料擷取與分析 Python 401 資料：折線圖

1. 題目說明:
請開啟PYD04.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA04.py再進行評分。

2. 設計說明：
利用程式內提供的數據，依下列要求以matplotlib輸出chart.png圖檔：

設定線條寬度設定為1，線條色彩與樣式各別為藍色虛點線與紅色虛點線
設定軸刻度調整至(0,0)開始至(8,70)
標題設定
圖表標題：Figure 字體大小：24
X軸標題：x-Value，字體大小：16
Y軸標題：y-Value，字體大小：16
3. 輸入輸出：
輸入說明
無

輸出說明
輸出chart.png圖檔

範例輸入
無

範例輸出
https://i.imgur.com/OtOr31h.png

注意：
matplotlib套件的版本，會造成輸出的圖檔有差異，但不影響評分的準確性。
Code Judger平台會將您的程式，於伺服器中運行輸出圖檔進行評分。
'''

# -*- coding: utf-8 -*-
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]
seq = [1, 2, 3, 4, 5, 6, 7, 8]

# 數據及線條設定
plt.plot(seq, data1, '--.b', seq, data2, '--.r', linewidth=1)

# 軸刻度
plt.axis([0, 8, 0, 70])

# 圖表標題
plt.title('Figure', fontsize=24)

# X軸標題
plt.xlabel('x-Value', fontsize=16)

# Y軸標題
plt.ylabel('y-Value', fontsize=16)

# 輸出圖片檔案
plt.savefig('chart.png')
plt.close()
