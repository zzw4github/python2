import random
x = random.randint(1,10)
print(x)

list = []

for i in range(0,100):
    x = random.randint(1,10)
    list.append(x)

print(list)

list = [1,2,3,4,5,6,7,8,9,10]
x = random.sample(list,3)
print(x)