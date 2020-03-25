import matplotlib.pyplot as plt
import numpy as np
import math

data = np.array([60.00,75.00,88.00,74.00,
                73.00,92.00,80.00,97.00,
                83.00,71.00,68.00,76.00])

def getRange(data):
    return int(np.amax(data)-np.amin(data))

def getProperC(data):
    return int(math.log(data.size)/math.log(2))+1

showGrouped = True
showRelative = True

binValue = getProperC(data) if showGrouped else getRange(data)
weightsValue = (np.ones_like(data)/data.size) if showRelative else None
arr=plt.hist(data,bins=binValue, weights = weightsValue)

def showValue(value,isRelative):
    if isRelative:
        return str(round(value*100,2))+"%"
    else:
        return str(int(value))
plt.pie(data)
for i in range(binValue):
    plt.text(arr[1][i],arr[0][i],showValue(arr[0][i],showRelative))

plt.ylabel('numbers')
plt.xlabel('weight')

plt.show()