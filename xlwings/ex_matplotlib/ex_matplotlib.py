import xlwings as xw

import matplotlib.pyplot as plt


@xw.func
def myplot(n):
    sht = xw.Book.caller().sheets.active
    fig = plt.figure()
    plt.plot(range(int(n)))
    sht.pictures.add(fig, name='MyPlot', update=True)
    return 'Plotted with n={}'.format(n)


if __name__ == "__main__":
    fig = plt.figure()
    plt.plot([1, 2, 3])
    
    sht = xw.books['ex_matplotlib.xlsm'].sheets[0]
    sht.pictures.add(fig, name='MyPlot', update=True)

    sht.pictures.add(fig, name='MyPlot', update=True, left=sht.range('B5').left, top=sht.range('B5').top)
    
    plot = sht.pictures.add(fig, name='Myplot', update=True)
    plot.height /= 2
    plot.width /= 2
    
    