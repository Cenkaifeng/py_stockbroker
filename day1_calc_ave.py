# coding:utf-8
# 计算日线平均数据 N日移动平均线=N日收市价之和/N

import pandas as pd

url_str = 'stock_data/sh000001.csv'
stock_data = pd.read_csv(url_str, parse_dates=[1])
stock_data = pd.DataFrame(stock_data)
# print(pf)
# 将数据按照date 增量排序 sort api 在新版本改为sort_values
stock_data.sort_values('date', inplace=True)

# 计算的日期 放入list
ma_list = [5, 20, 60]


# MA 为每天算数平均线 close 为收盘价 rolling_mean api v0.18 -> rolling().mean v0.23

for ma in ma_list:
    print(ma)
    print(stock_data['close'])
    print(stock_data['close'].rolling(250))
    stock_data['MA_' + str(ma)] = stock_data['close'].rolling(ma).mean()
    # print(stock_data['MA_' + str(ma)])
# 计算平滑移动平均线 EMA

for ma in ma_list:
    stock_data['EMA_' + str(ma)] = stock_data['close'].ewm(span=ma).mean()

# 输出前再排序一次

stock_data.sort_values('date', ascending=False, inplace=True)
print(stock_data)
# 然后输出
stock_data.to_csv('stock_data/sh600000_ma_ema.csv', index=False)
exit()
