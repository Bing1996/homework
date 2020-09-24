import os
import numpy as np
import pandas as pd
import math

os.system('clear')
myDir = './share/'
fileName = '2292949.csv'
#----------------------------------#

def changeFormat(time):
    month = time[4:6]
    day = time[6:8]
    year = time[0:4]
    hour = time[9:11]

    res = isZero(month) + '/' + isZero(day) + '/' + year + ' ' + isZero(hour) + ':00'
    return res

def isZero(number):
    if number[0] == '0':
        number = number[-1]
    return str(number)


#----------------------------------#
data = pd.read_csv(myDir + fileName)
data = np.array(data)
data = data[2:  , 1 : ]
[x_row , y_col] = np.shape(data)

print(np.shape(data))

for i in range(x_row):
    data[i,0] = changeFormat(data[i,0])

pd.DataFrame(data).to_csv(myDir + 'rain2_sample_data.csv',index=False,header=False)
