class auto:
    szin, ajtok, marka, tipus = ["",0,"",""]
    def __init__(self, szin, ajtok, marka, tipus):
        self.szin = szin
        self.ajtok = ajtok
        self.marka = marka
        self.tipus = tipus
    def indul(self):
        print("BRRR")
    def duda(self):
        print("TÜ-TÜ")
    def index(self):
        print("KAT-KAT-KAT")

class BMW(auto):
    def __init__(self,szin, ajtok, marka, tipus):
        super().__init__(self,szin, ajtok, marka, tipus)
    def indul(self):
        print("BRUMM")



if __name__ == "__main__":
    a = auto("a",1,"a","a")
    print(a.index())
