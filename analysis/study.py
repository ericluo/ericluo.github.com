import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

import tushare as ts

print(ts.sh_margins(start='2015-01-01', end='2015-04-19'))