l = []
for i in range(28):
    l.append(int(input()))
v = 1
for c in sorted(l):
    if v is not c:
        print(v)
        v += 1
    v += 1