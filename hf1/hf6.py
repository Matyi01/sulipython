import random

x = 0
while x == 0:
    szam = random.randint(1000,9999)
    if szam % 6 == 0 and szam % 12 != 0:
        x = 1
        print(szam)
