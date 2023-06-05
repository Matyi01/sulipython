class szo:
    def __init__(self, szo):
        self.szo = szo
    def minta(self, be):
        vissza = ""
        for i in range(6):
            if be[i] == self.szo[i]:
                vissza += be[i]
            else:
                vissza += "."
        return vissza
