import xlwings as xw
import numpy as np
import pandas as pd

@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 2 * (x + y)
    
    
@xw.func
@xw.arg('data', ndim=2)   # To ensure the input is two-dim
def add_one(data):
    return [[cell + 1 for cell in row] for row in data]


@xw.func
@xw.arg('x', np.array, ndim=2)
@xw.arg('y', np.array, ndim=2)
def matrix_mult(x,y):
    return x.dot(y)
    

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=False)
@xw.ret(index=False, header=False)
def CORREL2(x):
    """Like CORREL, but as array fomula for more than 2 data sets"""
    return x.corr()
    

# convert the argument x into a pandas DataFrame and suppress the index when returning it
@xw.func
@xw.arg('x', pd.DataFrame)
@xw.ret(index=False)
def myfunction(x):
    # x is a DataFrame, do sth with it
    return x
    

# Dynamic Array Formula
@xw.func
@xw.ret(expand='table')
def dynamic_array(r,c):
    return np.random.randn(int(r), int(c))

    
# "vba" keyword
# get the address of the calling cell
@xw.func
@xw.arg('xl_app', vba='Application')
def get_caller_address(xl_app):
    return xl_app.Caller.Address


# Macros
@xw.sub
def my_macro():
    """Writes the name of the Workbook into Range("A1") of Sheet 1"""
    wb = xw.Book.caller()
    wb.sheets[0].range('A1').value = wb.name



















