import xlwings as xw
import numpy as np

@xw.func
@xw.arg('x', np.array)
def myfunction(x):
    print(x.T)
    return x @ x.T
    
if __name__ == "__main__":
    xw.serve()
