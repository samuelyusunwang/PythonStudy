# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:09:24 2016

@author: ywang
"""

import xlwings as xw

xw.Book()
xw.Range('A1').value = 'something'

app = xw.App()
app.books['Book1']
