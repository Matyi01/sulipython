import random

vezetek = ["Nagy","Kovács","Tóth","Szabó","Horváth"]
ferfi = ["Tamás","Bence","Péter","János","Patrik"]
no = ["Réka","Anna","Katalin","Hanna","Regina"]

for i in range(100):
    last2 = ""
    first = random.choice(vezetek)
    if random.randint(1,2) == 1:
        last1 = random.choice(ferfi)
        if random.randint(1,5) == 1:
            last2 = random.choice(ferfi)
            while last1 == last2:
                last2 = random.choice(ferfi)
    else:
        last1 = random.choice(no)
        if random.randint(1,5) == 1:
            last2 = random.choice(no)
            while last1 == last2:
                last2 = random.choice(no)
    print(first+" "+last1+" "+last2)
