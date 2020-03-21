def superMultiply(x):
    if(x==1):
        return 1
    else:
        return x * superMultiply(x-1)

print(superMultiply(5))