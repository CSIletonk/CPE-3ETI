"""
COURS CLASS PY
DZIOPA Raphael 3ETI
utf-8
09/24
"""

from math import sqrt

class etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.note = []
    def moyenne(self):
        if len(self.note) == 0:
            return -1
        else:
            return sum(self.note)/len(self.note)
    
class polynome:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def evaluation(self, x):
        if x > 0:
            return (self.a*(x**2))+(self.b*x)+(self.c)
        elif x == 0:
            return 0
        else:
            return "Error x in C"
    def racine(self):
        delta = (self.b**2)-(4*self.a*self.c)
        if delta == 0:
            return (-self.b)/(2*self.a)
        elif delta > 0:
            return ((-self.b)*sqrt(delta))/(2*self.a)
        else:
            return "Error delta in C"
        
class polynome2:
    def __init__(self, a, b, c, d ,e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def add(self):
        return [self.a+self.d, self.b+self.e, self.c+self.f]
    def sous(self):
        return [self.a-self.d, self.b-self.e, self.c-self.f]
    def scalaire(self, k):
        print("k* polynome 1")
        return [self.a*k,self.b*k,self.c*k]
    def printer(self):
        print(self.a,"x**2 +", self.b,"x +",self.c)



"""FX TEST"""
"""
e0 = etudiant("Dupre","Paul")
e1 = etudiant("Francis","Patrick")
e0.note=[12,13,15]
e1.note=[16,8.5,6.3]
liste_etudiants = [e0,e1]
for e in liste_etudiants:
    print(e.nom,e.prenom,round(e.moyenne(),2))

p0 = polynome(1,4,3)
p1 = polynome(1,0,1)
print(p0.evaluation(1.0))
print(p0.evaluation(1.5))
print(p0.racine())
print(p1.racine())

p2 = polynome2(1,4,2,1,2,2)
print(p2.add())
print(p2.sous())
print(p2.scalaire(2))
p2.printer()
"""
