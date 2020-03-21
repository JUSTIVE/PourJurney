a = int(input())
#################################################################
#'''
#upper triangle
for i in range(int(a/2)):
    for j in range(i+1):
        print("*",end='')
    for j in range(a-(2*(i+1))):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()
#middle line
for i in range(a):
    print("*",end='')
print()
#lower triangle
for i in range(int(a/2),0,-1):
    for j in range(i):
        print("*",end='')
    for j in range(a-(2*i)):
        print("",end=' ')
    for j in range(i):
        print("*",end='')
    print()
#'''
#################################################################
#'''
half = int((a)/2)
for i in range(a):
    #upper triangle
    if i < half:
        for j in range(i+1):
            print("*",end='')
        for j in range(a-(2*(i+1))):
            print("",end=' ')
        for j in range(i+1):
            print("*",end='')
    #middle line
    elif i == half:
        for i in range(a):
            print("*",end='')
    #lower triangle
    else:
        for j in range(a-i):
            print("*",end='')
        for j in range((i-half-1)*2+1):
            print("",end=' ')
        for j in range(a-i):
            print("*",end='')
    print()
#'''
#################################################################
#"""
half = int((a)/2)
for i in range(a):
    #upper triangle
    if i < half:
        for j in range(a):
            print("*" if (i>=j)or(a-i-1)<=j else " ",end ='')
    #middle line
    elif i == half:
        for i in range(a):
            print("*",end='')
    #lower triangle
    else:
        for j in range(a):
            print("*" if ((a-i)>j)or(i<=j) else ' ',end ='')
    print()
#"""
