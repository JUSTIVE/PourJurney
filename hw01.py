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

pielabels =[]
piedata =[]
gapValue = getRange(data) / getProperC(data)

for i in range(getProperC(data)):
    tempvalue = 0
    for j in range(data.size):
        if ((data[j] >= np.amin(data)+gapValue*i) and (data[j]<=np.amin(data)+gapValue*(i+1))):
            tempvalue+=1
    piedata.append(tempvalue)
    pielabels.append((str(np.amin(data)+gapValue*i)+"~"+str(np.amin(data)+gapValue*(i+1))))

plt.pie(piedata,labels=pielabels,autopct="%f")
plt.show()