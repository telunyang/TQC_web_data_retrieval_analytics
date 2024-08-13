'''
TQC+ 網頁資料擷取與分析 Python 405 樣本：直方圖與散佈圖

1. 題目說明:
請開啟PYD04.py檔案，依下列題意進行組合改寫，使輸出值符合題意要求。作答完成請另存新檔為PYA04.py再進行評分。

2. 設計說明：
依下列要求以matplotlib輸出chart.png圖檔：

利用程式內提供的第一組sample1與第二組sample2數據輸出左右兩個圖，左圖為直方圖（histogram），右圖為散佈圖（scatter）。
直方圖疊合兩個直方圖，兩圖均請在-3~+3間均勻間隔分為100格，透明度（alpha）均為0.5。在左上角放置圖例，sample1的標記為samples 1，sample2的標記為samples 2。
散佈圖以 sample1 作為X軸資料、sample2作為Y軸資料，透明度設為 0.2。

3. 輸入輸出：
輸入說明
無

輸出說明
輸出chart.png圖檔

範例輸入
無

範例輸出
https://i.imgur.com/GKiv6JU.png

注意：
matplotlib套件的版本，會造成輸出的圖檔有差異，但不影響評分的準確性。
Code Judger平台會將您的程式，於伺服器中運行輸出圖檔進行評分。
'''

# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
set_seed = 123
# --結束--批改評分使用，請勿變動

# 載入 numpy 模組並縮寫為 np
import ___ as ___
# 載入 matplotlib.pyplot 並縮寫為 plt
import ___ as ___

samples_1 = np.random.RandomState(set_seed).normal(loc=1, scale=.5, size=1000)
samples_2 = np.random.RandomState(set_seed).standard_t(df=10, size=1000)
bins = np.linspace(___, ___, ___)

# 第一個子圖
plt.subplot(___, ___, ___)
plt.hist(___, bins=___, alpha=___, label='___')
plt.hist(___, bins=___, alpha=___, label='___')
# 在左上角 upper left 放置圖例 legend
plt.___(loc='___')

# 第二個子圖
plt.subplot(___, ___, ___)
plt.scatter(___, ___, alpha=___)

plt.savefig(___)
plt.close()
