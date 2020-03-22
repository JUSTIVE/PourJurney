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

showGrouped = False

binValue = getProperC(data) if showGrouped else getRange(data)
arr=plt.hist(data,bins=binValue, weights = np.ones_like(data)/ (data.size))

for i in range(binValue):
    plt.text(arr[1][i],arr[0][i],str(round(arr[0][i]*100,2))+"%")

plt.ylabel('numbers')
plt.xlabel('weight')

plt.show()