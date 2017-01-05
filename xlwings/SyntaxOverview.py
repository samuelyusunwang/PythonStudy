# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:07:42 2016

@author: ywang
"""

# Syntax Overview

import xlwings as xw

## Active Objects
# Active app (i.e. Excel instance)
app = xw.apps.active

# Active book
wb = xw.books.active   # in active app
wb = app.books.active   # in specific app

# Active sheet
sht = xw.sheets.active   # in active book
sht = wb.sheets.active   # in specific book

# Range on active sheet
xw.Range('A1')
xw.Range('A1:C3')
xw.Range((1,1))
xw.Range((1,1), (3,3))
xw.Range('NamedRange')
xw.Range(xw.Range('A1'), xw.Range('B2'))

xw.apps[0].books[0].sheets[0].range('A1')
xw.apps(1).books(1).sheets(1).range('A1')
xw.apps[0].books['Book1'].sheets['Sheet1'].range('A1')
xw.apps(1).books('Book1').sheets('Sheet1').range('A1')

# rng = xw.Book().sheets[0].range('A1:D5')
rng = xw.books[0].sheets[0].range('A1:D5')
rng[0,0]
rng[1]
rng[:,3:]
rng[1:3,1:3]

# rnage shortcuts
sht = xw.books[0].sheets['Sheet1']
sht['A1']
sht['A1:B5']
sht[0,1]
sht[:10,:10]


# Object Hierarchy
rng = xw.apps[0].books[0].sheets[0].range('A1')
rng.sheet.book.app
