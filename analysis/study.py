import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfs = pd.read_excel("./banks.xls", sheetname=None, index_col='机构')

stks = ['工商银行','农业银行','中国银行','建设银行','交通银行','中信银行','光大银行',
	'华夏银行','广东发展银行','平安银行','招商银行','上海浦东发展银行','兴业银行','民生银行']

stks2 = ['招商银行','上海浦东发展银行','兴业银行','民生银行', '中信银行']
pdata = pd.Panel(dfs, major_axis=stks2)

loans = pdata.swapaxes('items', 'minor_axis')['各项贷款']
plt.plot(loans.T)
plt.show()
