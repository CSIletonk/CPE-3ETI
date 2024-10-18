"""
Exercices Reprise de PYTHON
M.BAJODEK
TEST

UTF-8
"""
import SimplePYexf as f

#Exercice 1 == Verification de l'existance d'une date
"""
an = int(input("Année : "))
mois = int(input("Mois : "))
jour = int(input("Jour :"))

print(f.datevalide(jour, mois, an)) #Appel dans Main (fichier FX) de verification d'une date*
"""


#Exercice 2 == Calcul d'impots
"""
print(f.ImpotsRevenu(int(input("Revenus par an : "))))
"""

#Exercice 4 == Récursivité / Tour de Hanoï

col1 = [5, 4, 3, 2, 1]
col2 = []
col3 = []

f.TourdeHanoi(0, col1, col2, col3)