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
