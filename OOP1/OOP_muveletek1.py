class muvelet:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def osszead(self):
        return self.x + self.y
    def kivon(self):
        return self.x - self.y
    def szoroz(self):
        return self.x * self.y
    def oszt(self):
        return self.x / self.y

if __name__ == "__main__":
    q = muvelet(1,2)
    print(q.osszead())
    print(q.kivon())
    print(q.szoroz())
    print(q.oszt())
    q = muvelet(10,20)
    print(q.osszead())
    print(q.kivon())
    print(q.szoroz())
    print(q.oszt())
