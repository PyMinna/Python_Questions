# Find the first element that appears more than once.

arr = [10,5,8,2,2,6,8,7,6]

for i in arr:
    if arr.count(i)>1:
        print(i)
        break