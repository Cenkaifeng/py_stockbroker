# coding:utf-8

import pandas as pd

stock_data = pd.read_csv('stock_data/sz300293.csv', parse_dates=[1])
# stock_data = pd.DataFrame(pd.read_csv('stock_data/sz300293.csv', parse_dates=[1]))

print(stock_data)

# 设定装换周期 period_type, 周-W 月-M 季度-Q 五分钟5min 12天 12D

period_type = 'W'

# 将date 设定为index (索引）

stock_data.set_index('date', inplace=True)

# 进行转换，周线的每一个变量都等于那一周中最后一个交易日的变量值
period_stock_data = stock_data.resample(period_type).last()

# 周线change = 一周每日change连乘
period_stock_data['change'] = stock_data['change'].resample(period_type).apply(lambda x: (x + 1.0).prod() - 1.0)

# 周线的open 等于一周中第一个交易日open
period_stock_data['open'] = stock_data['open'].resample(period_type).first()

# 周线high 等于一周中high 最大值
period_stock_data['high'] = stock_data['high'].resample(period_type).max()

# ￿周线 low = 一周最low 的值
period_stock_data['low'] = stock_data['low'].resample(period_type).min()

# 周 money volume 等于各自的日和
period_stock_data['volume'] = stock_data['volume'].resample(period_type).sum()
period_stock_data['money'] = stock_data['money'].resample(period_type).sum()

# 计算周线 turnover
period_stock_data['turnover'] = period_stock_data['volume'] / \
                                (period_stock_data['traded_market_value']/period_stock_data['close'])

# 去除整周没有交易的股票
period_stock_data = period_stock_data[period_stock_data['close'].notnull()]
period_stock_data.reset_index(inplace=True)

# 输出csv

period_stock_data.to_csv('stock_data/week_stock_data.csv', index=False)


