N = int(input())
k = []
for _ in range(N):
    word = input()
    k.append(word)

k = list(set(k))
k.sort()

ind = []
for i in range(len(k)):
    ind.append(len(k[i]))

res = []
for _ in range(len(ind)):
    res.append(k[ind.index(min(ind))])
    k.remove(k[ind.index(min(ind))])
    ind.remove(min(ind))


for i in range(len(res)):
    print(res[i])