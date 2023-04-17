"""
Ország:	Állatok (Animalia)
Törzs:	Gerinchúrosok (Chordata)
Altörzs:	Gerincesek (Vertebrata)
Főosztály:	Négylábúak (Tetrapoda)
Osztály:	Emlősök (Mammalia)
Alosztály:	Elevenszülő emlősök (Theria)
Alosztályág:	Méhlepényesek (Placentalia)
Rend:	Ragadozók (Carnivora)
Alrend:	Kutyaalkatúak (Caniformia)
Család:	Kutyafélék (Canidae)
Alcsalád:	Valódi kutyaformák (Caninae)
Nemzetség:	Rókák (Vulpini)
Nem:	Róka (Vulpes)
"""

class orszag():
    def __init__(self,o):
        self.orszag = o
class torzs(orszag):
    def __init__(self,o,t):
        super().__init__(o)
        self.torzs = t
class altorzs(torzs):
    def __init__(self,o,t,at):
        super().__init__(o,t)
        self.altorzs = at
class foosztaly(altorzs):
    def __init__(self,o,t,at,fo):
        super().__init__(o,t,at)
        self.foosztaly = fo
class osztaly(foosztaly):
    def __init__(self,o,t,at,fo,os):
        super().__init__(o,t,at,fo)
        self.osztaly = os
class alosztaly(osztaly):
    def __init__(self,o,t,at,fo,os,ao):
        super().__init__(o,t,at,fo,os)
        self.alosztaly = ao
class alosztaly(osztaly):
    def __init__(self,o,t,at,fo,os,ao):
        super().__init__(o,t,at,fo,os)
        self.alosztaly = ao
class alosztalyag(alosztaly):
    def __init__(self,o,t,at,fo,os,ao,aoag):
        super().__init__(o,t,at,fo,os,ao)
        self.alosztalyag = aoag
class rend(alosztalyag):
    def __init__(self,o,t,at,fo,os,ao,aoag,r):
        super().__init__(o,t,at,fo,os,ao,aoag)
        self.rend = r
class alrend(rend):
    def __init__(self,o,t,at,fo,os,ao,aoag,r,ar):
        super().__init__(o,t,at,fo,os,ao,aoag,r)
        self.alrend = ar
class csalad(alrend):
    def __init__(self,o,t,at,fo,os,ao,aoag,r,ar,c):
        super().__init__(o,t,at,fo,os,ao,aoag,r,ar)
        self.csalad = c
class alcsalad(csalad):
    def __init__(self,o,t,at,fo,os,ao,aoag,r,ar,c,ac):
        super().__init__(o,t,at,fo,os,ao,aoag,r,ar,c)
        self.alcsalad = ac
class nemzetseg(alcsalad):
    def __init__(self,o,t,at,fo,os,ao,aoag,r,ar,c,ac,ng):
        super().__init__(o,t,at,fo,os,ao,aoag,r,ar,c,ac)
        self.nemzetseg = ng
class nem(nemzetseg):
    def __init__(self,o,t,at,fo,os,ao,aoag,r,ar,c,ac,ng,n):
        super().__init__(o,t,at,fo,os,ao,aoag,r,ar,c,ac,n)
        self.nem = n
