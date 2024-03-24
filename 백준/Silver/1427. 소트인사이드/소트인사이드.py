N = int(input())
b = str(N)
c = []
d = []
result = ""
for i in range(len(b)):
    c.append(b[i])
for i in range(len(c)):
    result += max(c)
    c.remove(max(c))
print(int(result))