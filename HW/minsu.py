import functools

def getIn(query:str):
    return dict([(x,(i,1)) for (i,x) in enumerate(input(query).split())])
user = getIn("Write your sentence: ")
target = getIn("Write Target sentence: ")



for (x,(i,v)) in target.items():
    if x in user:
        user[x] = (user[x][0],2)

def ifTwo(x):
    return x[1][1]==2

f = sorted(
        list(
            map(
                lambda x:(x[0],x[1][0]),
                filter(
                    ifTwo,
                    user.items()))),
        key=lambda x:x[1])

def pColS(x):
    return print(str.join(' ',x[0]))

def concat(x,y):
    if y[1]-x[1] == 1:
        return (x[0]+[y[0]],y[1])
    else:
        pColS(x)
        return ([y[0]],y[1])

pColS(functools.reduce(concat,f,([],-1)))
