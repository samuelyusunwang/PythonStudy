# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:22:15 2016

@author: ywang
"""

# Data Structure Tutorial

import xlwings as xw

# Single Cells
import datetime as dt
sht = xw.Book().sheets[0]
sht.range('A1').value = 1
sht.range('A1').value
sht.range('A2').value = 'Hello'
sht.range('A2').value
sht.range('A3').value is None
sht.range('A4').value = dt.datetime(2000,1,1)
sht.range('A4').value

# 1d List
sht = xw.books[0].sheets[0]
sht.range('A1').value = [[1], [2], [3], [4], [5]]
sht.range('A1:A5').value
sht.range('A1').value = [1, 2, 3, 4, 5]
sht.range('A1:E1').value

# force a single cell to be returned as list
sht.range('A1').options(ndim=1).value

# To write a list in column orientation to Excel
sht.range('A1').options(transpose=True).value = [1, 2, 3, 4, 5]

# 2d list
sht.range('A1:A5').options(ndim=2).value

sht.range('A10').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10, 20, 30]]
sht.range((10,1),(11,3)).value

# Range Expand
sht = xw.books[0].sheets[0]
sht.range('A1').value = [[1, 2], [3, 4]]
rng1 = sht.range('A1').expand('table')   # or just expand()
rng2 = sht.range('A1').options(expand='table')
rng1.value
rng2.value
sht.range('A3').value = [5,6]
rng1.value
rng2.value


# Numpy array
import numpy as np
sht = xw.books[0].sheets[0]
sht.range('A1').value = np.eye(3)
sht.range('A1').options(np.array, expand='table').value


# DataFrames
import pandas as pd
sht = xw.books[0].sheets[0]
df = pd.DataFrame([[1.1, 2.2], [3.3, None]], columns=['one', 'two'])
sht.range('A1').value = df
sht.range('A1:C3').options(pd.DataFrame).value
# options: work for reading and writing
sht.range('A5').options(index=False).value = df
sht.range('A9').options(index=False, header=False).value = df


# Pandas Series
sht = xw.books[0].sheets[0]
sht.clear()
s = pd.Series([1.1, 3.3, 5., np.nan, 6., 8.], name='myseries')
sht.range('A1').value = s
sht.range('A1:B7').options(pd.Series).value









