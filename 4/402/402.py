'''
TQC+ 網頁資料擷取與分析 Python 402 市場成交行情：折線圖

1. 題目說明:
請開啟PYD04.py檔案，依下列題意進行組合改寫，使輸出值符合題意要求。作答完成請另存新檔為PYA04.py再進行評分。

2. 設計說明：
請讀取果菜市場香蕉成交行情read.csv資料，主要有兩個欄位：成交日期、成交平均價。再以matplotlib輸出折線圖chart.png，輸出圖表的參數如下：

顯示圖例（legend）：banana
圖表標題：Market Average Price
以成交日期為X軸，X軸名稱：date
以成交平均價為Y軸，Y軸名稱：NT$
Y軸下限15、上限25
3. 輸入輸出：
輸入說明
讀取read.csv的內容

輸出說明
輸出chart.png圖檔

範例輸入
無

範例輸出
https://i.imgur.com/Z9fh5fs.png

注意：
matplotlib套件的版本，會造成輸出的圖檔有差異，但不影響評分的準確性。
Code Judger平台會將您的程式，於伺服器中運行輸出圖檔進行評分。
'''

# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt
# 載入 csv 模組
import csv

x = []
y = []

# 讀入 read.csv
with open('read.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

x_ticks = range(1, len(x) + 1)
plt.plot(x_ticks, y, label='banana')
plt.xticks(x_ticks, x)
plt.xlabel('date')
plt.ylabel('NT$')
plt.ylim(15, 25)

# 添加圖表標題 title()
plt.title('Market Average Price')
plt.legend()

# 使用 savefig() 函數
plt.savefig('chart.png')
plt.close()
