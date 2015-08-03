'''
Created on Jul 31, 2015

@author: ywang
'''

def cheer_up(times):
    for i in range(1, times+1):
        print('You will become a good programmer' + i*'!')

sadness = int(input('Enter 1-10 indicating how sad you are:'))
cheer_up(sadness)


