# Count how many elements appear more than once

num = [10,7,4,8,9,4,7,7,10,1,7,1]
count = 0

for i in set(num):
    if num.count(i) > 1:
        count += 1

print(count)
