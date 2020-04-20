w = []
k = []
for i in range(10):
    w.append(int(input()))
for i in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

wtop = w[0]+w[1]+w[2]
ktop = k[0]+k[1]+k[2]

print(str(wtop)+" "+str(ktop))
"""
def getTop3():
    u=[]
    for i in range(10):
        u.append(int(input()))
    return str(sum(sorted(u)[0::3]))

#sum function, inplace sorting, outplace sorting, what is sorting, list slicing
print(getTop3()+" "+getTop3())
"""
