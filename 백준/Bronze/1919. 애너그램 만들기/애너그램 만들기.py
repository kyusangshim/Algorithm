from collections import Counter

a = input()
b = input()

count_a = Counter(a)
count_b = Counter(b)

count = 0
# a에서 카운트
for item in count_a:
  if item not in count_b:
    count += count_a[item]
  
  else:
    if count_a[item] == count_b[item]:
      continue

    else:
      temp = abs(count_a[item] - count_b[item])
      count += temp
      if count_a[item] < count_b[item]:
        count_a[item] += temp
      else:
        count_b[item] += temp

# b에서 카운트
for item in count_b:
  if item not in count_a:
    count += count_b[item]
    
    
    
print(count)