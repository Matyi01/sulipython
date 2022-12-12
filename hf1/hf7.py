import random

vezetek = ["Nagy","Kovács","Tóth","Szabó","Horváth"]
ferfi = ["Tamás","Bence","Péter","János","Patrik"]
no = ["Réka","Anna","Katalin","Hanna","Regina"]

for i in range(100):
    first2 = ""
    last = random.choice(vezetek)
    if random.randint(1,2) == 1:
        first1 = random.choice(ferfi)
        if random.randint(1,5) == 1:
            first2 = random.choice(ferfi)
            while first1 == first2:
                first2 = random.choice(ferfi)
    else:
        first1 = random.choice(no)
        if random.randint(1,5) == 1:
            first2 = random.choice(no)
            while first1 == first2:
                first2 = random.choice(no)
    print(last+" "+first1+" "+first2)
