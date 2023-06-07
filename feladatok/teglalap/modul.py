class szamitas:
    def __init__(self, h, sz):
        self.h = int(h)
        self.sz = int(sz)
    def terulet(self):
        return self.h * self.sz
    def kerulet(self):
        return (self.h + self.sz) * 2
