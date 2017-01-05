# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:48:11 2016

@author: ywang
"""

import xlwings as xw

xw.Book()

# open an Excel File, it is now the active sheet
xw.Range('A1').value = 'Foo 1'   # input data into cell A1
xw.Range('A1').value   # show value of cell A1

# Range expanding
xw.Range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
xw.Range('A1').expand().value

# convert to dataframe
import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
xw.Range('A1').value = df
xw.Range('A1').options(pd.DataFrame, expand='table').value

# instantiate a new book, add a new sheet and write a value
wb = xw.Book()
wb.sheets.add()
wb.sheets['Sheet1'].range('A1').value = 'Foo1'

# use ww.Book to find your workbook
# xw.Book('Quickstart.xlsx')

# more control (e.g. same file open in two Excel instance)
# xw.apps[0].books('Quickstart.xlsx')

# Show Matplotlib in Excel
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
wb = xw.Book()
wb.sheets[0].pictures.add(fig, name='MyPlot', update=True)

@xw.func
def hello(name):
    return 'Hello {0}'.format(name)



    