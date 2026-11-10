# Remove elements smaller than a given value.

list = [5,8,3,2,9,7]
val = 4
out = []

for i in list:
    if i >= val:
        out.append(i)

print(out)
