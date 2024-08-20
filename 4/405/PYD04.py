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
