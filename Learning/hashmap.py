# dictionary
dic = {1: 3, 2: 10, 3: 9, 4: 5}

print(dic.items())

arr = []
for num, cnt in dic.items():
    arr.append([cnt, num])
arr.sort()

print(arr)
print(arr.pop()[1])