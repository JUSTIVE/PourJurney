import matplotlib.pyplot as plt

data = [60.00,75.00,88.00,74.00,73.00,92.00,80.00,97.00,83.00,71.00,68.00,76.00]
plt.hist(data,density=False)
plt.axis([0, 100, 0, 5]) 
plt.ylabel('수')
plt.xlabel('몸무게')
plt.show()