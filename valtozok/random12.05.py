import random
import math


l = []
for i in range(10):
    szam = random.random()
    l.append(math.floor(szam * 90)+10)

print(l)

l = []
for i in range(10):
    szam = random.random()
    l.append(random.randint(10,99))

print(l)

l = []
for i in range(100):
    l.append(random.randint(-1000,1000)*3)


print(l)

print(sum(l))

l5 = []
for e in l:
    if e % 5 == 0:
        l5.append(e)
    
print(l5)

l5 = [e//l5 for e in l if e % 5 == 0]

print(l5)
