#'''
alpha = dict([(i,-1) for i in map(chr,range(97,123))])
alpha.update(dict([(x,i) for i,x in reversed(list(enumerate(input())))]))
for (x,i) in sorted(list(alpha.items())):
    print(i,end=' ')
'''
s = list(map(str,input()))

alphabet = list('abcdefghijklmnopqrstuvwxyz')

array = [-1 for j in range(len(alphabet))]

for i in range(len(s)):
    if array[alphabet.index(s[i])] == -1:
        array[alphabet.index(s[i])] = i

for j in array :
    print(j,end=' ')
#'''