import numpy as np

number = np.random.randint(10,51)

print(number)
list = []

num = 0
while True:
    num = np.random.randint(10,101)
    list.append(num)
    if len(list) == number:
        print(list)
        break

while True:
    for num in list:
        for j in list:
            if num>j:
                print(end="")
            else:
                num=j
    break
print(num)