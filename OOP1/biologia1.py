"""
Ország:	Állatok (Animalia)
Törzs:	Gerinchúrosok (Chordata)
Altörzs:	Gerincesek (Vertebrata)
Főosztály:	Négylábúak (Tetrapoda)
Osztály:	Emlősök (Mammalia)
Alosztály:	Elevenszülő emlősök (Theria)
Csoport:	Eutheria
Alosztályág:	Méhlepényesek (Placentalia)
Öregrend:	Laurasiatheria
Csoport:	Ferae
Rend:	Ragadozók (Carnivora)
Alrend:	Kutyaalkatúak (Caniformia)
Család:	Kutyafélék (Canidae)
Alcsalád:	Valódi kutyaformák (Caninae)
Nemzetség:	Rókák (Vulpini)
Nem:	Róka (Vulpes)
Frisch, 1775
"""

class orszag():
    def __init__(self,orszag):
        self.orszag = orszag
class torzs(orszag):
    def __init__(self,orszag,torzs):
        super().__init__(orszag)
        self.torzs = torzs
class altorzs(torzs):
    def __init__(self,o,t,at):
        super().__init__(o,t)
        self.altorzs = at
class foosztaly(foosztaly):
    def __init__(self,o,t,at,fo):
        super().__init__(o,t,at)
        self.foosztaly = fo
