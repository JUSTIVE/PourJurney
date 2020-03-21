a = int(input())
#################################################################
#'''
#upper triangle
'''
for i in range(int((a+1)/2)):
    for j in range(i+1):
        print("*",end='')
    print()
#lower triangle
for i in range(int(a/2),0,-1):
    for j in range(i):
        print("*",end='')
    print()
#'''
#################################################################
'''
def printRow(amount):
    for j in range(amount):
        print("*",end='')
        
half = int((a+1)/2)
for i in range(a):
    if i < half:
        printRow(i+1)
    else:
        printRow(half-(i-half)-1)
        
    print()
#'''
#################################################################
#"""
def printRow(amount):
    for j in range(amount):
        print("*",end='')
        
half = int((a+1)/2)
for i in range(a):
    printRow(i+1 if i < half else (half-(i-half)-1))
    print()
#"""