a = int(input())

#################################################################
'''
n = 1
for i in range(a):
    for j in range(i+1):
        if n<10:
            print(str(n)+' ',end='')
        else:
            print(n,end='')
        n+=1
    print()
#'''
#################################################################
#'''
n = 1
for i in range(a):
    for j in range(i+1):
        print(str(n)+' ' if n<10 else n,end='')
        n+=1
    print()
#'''