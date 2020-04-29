c= int(input())
for i in range(c):
    n = int(input())
    for j in range(n):
        for k in range(n):
            print("#" if j is 0 or k is 0 or k is n-1 or j is n-1 else "J" , end="")
        print("")
    print("\n")
