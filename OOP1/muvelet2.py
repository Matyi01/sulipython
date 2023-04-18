import muvelet as m

class muv(m.muvelet):
    def __init__(self,x,y):
        super().__init__(x,y)
    def p(self):
        return super().osszead()

w = m.muvelet(12,13)
print(w.osszead())
e = muv(12,13)
print(e.p())
