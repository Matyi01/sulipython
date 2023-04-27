class ember:
    szuletesiev = 0
    magassag = 0
    testsuly = 0
    def __init__(self,szuletesiev,magassag,testsuly):
        self.szuletesiev = szuletesiev
        self.magassag = magassag
        self.testsuly = testsuly
    def eletkor(self):
        return 2023 - self.szuletesiev
    def TTI(self):
        return self.testsuly/(self.magassag*self.magassag)

class diak(ember):
    osztaly = ""
    def __init__(self,szuletesiev,magassag,testsuly,osztaly):
        super().__init__(szuletesiev,magassag,testsuly)
        self.osztaly = osztaly
    def evfolyam(self):
        if 2023 - self.szuletesiev > 6 and 2023 - self.szuletesiev <= 19:
            return 2023 - self.szuletesiev - 6
        elif 2023 - self.szuletesiev == 6:
            return 1
        elif 2023 - self.szuletesiev > 19:
            return "felsőoktatás"
a = diak(2006,180,70,"C")
print(a.evfolyam())

 
q = ember(2006,180,70)
print(q.TTI())
