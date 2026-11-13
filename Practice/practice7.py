#  Check if a given list contains only numbers

li = ["7", "0", "6", "sql"]

n = "0,1,2,3,4,5,6,7,8,9,10"

for i in li:
    if i not in n:
        print(False)
        break
else:
    print(True)
