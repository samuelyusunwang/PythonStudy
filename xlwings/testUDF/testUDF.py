import xlwings as xw

@xw.func
def hello(name):
    return 'Hello {0}'.format(name)

import pandas as pd

@xw.func
@xw.arg('x', pd.DataFrame)
def correl2(x):
    # x arrives as DataFrame
    return x.corr()