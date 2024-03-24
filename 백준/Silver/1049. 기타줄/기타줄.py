need, number = map(int, input().split())
result = []
for i in range(number):
    a, b = map(int, input().split())
    if i == 0:        
        result.append(a)
        result.append(b)
    
    else:
        if (result[0] > a and result[1] > b):
            result[0] = a
            result[1] = b
        elif (result[0] < a and result[1] > b):
            result[1] = b
        elif (result[0] > a and result[1] < b):
            result[0] = a
        else:
            continue

if result[0] < (result[1] * 6):
    if (need // 6) > 0:
        count = need // 6
        etc = (need - (count*6))
        if etc != 0:
            if result[0] > (etc * result[1]):
                result.append((count * result[0]) + ((need - (count * 6)) * result[1]))
            else:
                result.append(result[0] * (count+1))
        else:
            result.append(result[0] * count)
    else:
        if result[0] > (result[1] * need):
            result.append((need * result[1]))
        else:
            result.append(result[0])
else:
    result.append((result[1]) * need)
    
    
print(result[2])