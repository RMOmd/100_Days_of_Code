sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)

sum2 = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum2 += i
print(sum2)    
    