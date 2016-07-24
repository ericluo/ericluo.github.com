import pandas as pd
# import numpy as np

# from bokeh.charts import TimeSeries, show, output_file
from bokeh.plotting import figure, show, output_file
from bokeh.charts import TimeSeries

# stks = ['工商银行','农业银行','中国银行','建设银行','交通银行','中信银行','光大银行',
# 	'华夏银行','广东发展银行','平安银行','招商银行','上海浦东发展银行','兴业银行','民生银行']

dfs = pd.read_excel("./banks.xls", sheetname=None, index_col='机构')
stks2 = ['招商银行','上海浦东发展银行','兴业银行','民生银行', '中信银行']
pdata = pd.Panel(dfs, major_axis=stks2)

loans = pdata.swapaxes('items', 'minor_axis')['各项贷款'].T
# line = TimeSeries(loans)

p = figure(width=800, height=600, x_axis_type="datetime")
loans.index = pd.to_datetime(loans.index, format="%Y%m%d")
loans = loans.astype('int')
p = TimeSeries(loans, y=stks2)

# for stk in stks2:
# 	p.line(loans.index, loans[stk], legend=stk)
output_file("loans.html", title="各项贷款")
show(p)