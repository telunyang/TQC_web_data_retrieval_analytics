'''
TQC+ 網頁資料擷取與分析 Python 403 月份統計：長條圖與圓餅圖

1. 題目說明:
請開啟PYD04.py檔案，依下列題意進行組合改寫，使輸出值符合題意要求。作答完成請另存新檔為PYA04.py再進行評分。

2. 設計說明：
依下列要求以matplotlib輸出四個月份（labels = 'Jun', 'Jul', 'Aug', 'Sep'）的統計圖形chart.png，輸出圖表的參數如下：

完成左右兩個圖，左圖為長條圖（bar），右圖為圓餅圖（pie）
長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）
圓餅圖以labels為圖標，sizes為各項所占百分比
圓餅圖colors為各項顏色，長寬比為1:1，並突顯「Aug」
圓餅圖顯示各項百分比到小數點第1位

3. 輸入輸出：
輸入說明
無

輸出說明
輸出chart.png圖檔

範例輸入
無

範例輸出
https://i.imgur.com/86uexKO.png

注意：
matplotlib套件的版本，會造成輸出的圖檔有差異，但不影響評分的準確性。
Code Judger平台會將您的程式，於伺服器中運行輸出圖檔進行評分。
'''

# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 四個月份
labels = [__, __, __, __]
sizes = [20, 30, 40, 10]
# 圓餅圖顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 長條圖 位置
plt.subplot(1, 2, ___)
xticks = range(1, len(labels) + 1)
# 長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）
plt.xticks(xticks, ___)
plt.bar(___, ___, color=___)

# 圓餅圖 位置
plt.subplot(1, 2, ___)
# 圓餅圖以labels為圖標，sizes為各項所占百分比
# 圓餅圖colors為各項顏色，突顯「Aug」
# 圓餅圖顯示各項百分比到小數點第1位
explode = (0, 0, 0.1, 0)
plt.pie(___, explode=___, labels=___,
        colors=___, autopct='___')
# 長寬比為1:1
plt.axis('___')

plt.savefig('chart.png')
plt.close()
