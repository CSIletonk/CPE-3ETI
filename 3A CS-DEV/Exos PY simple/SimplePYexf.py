"""
Exercices Reprise de PYTHON
M.BAJODEK
FX

UTF-8
"""

#Exercice 1 == Verification de l'existance d'une date

def anbiss(an):     
    #Verification que l'an est bissextile ou non input:user
    #Input int
    #Output booléen
    if (an % 4 == 0) and ((an/100) % 1 != 0):
        return True
    elif (an % 400 == 0):
        return True
    else:
        return False

def nbjours(in_an, in_mois):    
    #Donne le nombre de jours dans un mois selon l'an
    #Input int
    #Output int
    courtjour = [4, 6, 9, 11]
    longjour = [1, 3, 5, 7, 8, 10, 12]
    if in_mois == 2:
        if anbiss(in_an) is True:
            return 29
        else:
            return 28
    elif in_mois in courtjour:
        return 30
    elif in_mois in longjour:
        return 31
    
def datevalide(in_jour, in_mois, in_an):    
    #Verification de validité d'un date
    #Input int
    #Output text
    courtjour = [4, 6, 9, 11]
    longjour = [1, 3, 5, 7, 8, 10, 12]
    if in_an < 0 or in_jour < 0 or in_jour > 31 or in_mois < 0 or in_mois > 12:
        return "Date Invalide: Erreur Entré"
    if in_mois in courtjour and nbjours(in_an, in_mois) <= 30:
        return "Date Valide" 
    if in_mois in longjour and nbjours(in_an, in_mois) <= 31:
        return "Date Valide"
    if in_mois == 1 and anbiss(in_an) is False and nbjours(in_an, in_mois) <= 28:
        return "Date Valide"
    if in_mois == 1 and anbiss(in_an) is True and nbjours(in_an, in_mois) <= 29:
        return "Date Valide"
    else:
        return "Date Invalide"
    

#Exercice 2 == Calcul d'impots

def ImpotsRevenu(revenu):
    #Verification de la tranche et clacul des impots a payer
    #Input int
    #Output text, int
    tranche = [(0.0,10225), (0.11,26070), (0.3,74545), (0.41,160336), (0.45,float('inf'))]
    impot = 0.0

    for i in range(len(tranche)):
        taux, plafond = tranche[i]
        if revenu > plafond:
            if i == 0:
                continue
            impot += (plafond - tranche[i-1][0])* taux
        else:
            if i > 0:
                impot += (revenu - tranche[i-1][0])* taux
            break
    
    return "Impots à payer = ",impot


#Exercice 4 == Récursivité / Tour de Hanoï

def verifcol(in_col_debut, in_col_fin):
    #Verification si la valeur peut etre mise sur une autre colonne
    #Input int
    #Output booléen
    if len(in_col_fin) == 0 :
        return True
    elif in_col_debut[len(in_col_debut)-1] < in_col_fin[len(in_col_fin)-1]:
        return True
    if in_col_debut[len(in_col_debut)-1] > in_col_fin[len(in_col_fin)-1]:
        return False
    
def deplacer(in_col_debut, in_col_fin):
    #Deplacement d'un valeur d'une colonne à une autre
    #Input list
    #Output list, Booléen
    val = in_col_debut[len(in_col_debut)-1]
    if verifcol(in_col_debut, in_col_fin) is True:
        in_col_fin.append(val)
        in_col_debut = in_col_debut[:-1]
        return in_col_debut, in_col_fin
    else:
        return False

def TourdeHanoi(nbmove, in_col1, in_col2, in_col3):

    print(nbmove, in_col1, in_col2, in_col3)
    #Verification que la tour a été entièrement déplacé correctement
    for i,val in range(len(in_col3)-1):
        if in_col3[i+1] < in_col3[i] and in_col1 == []:
            if i == len(col3)-1:
                return nbmove
            else:
                continue
    
    if verifcol(in_col1, in_col2) is True:
        ou_col1, ou_col2 = deplacer(in_col1, in_col2)
        TourdeHanoi(nbmove+1, ou_col1, ou_col2, in_col3)
    elif verifcol(in_col1, in_col3) is True:
        ou_col1, ou_col3 = deplacer(in_col1, in_col3)
        TourdeHanoi(nbmove+1, ou_col1, in_col2, ou_col3)
    elif verifcol(in_col3, in_col2) is True:
        ou_col3, ou_col2 = deplacer(in_col3, in_col2)
        TourdeHanoi(nbmove+1, in_col1, ou_col2, ou_col3)
    elif verifcol(in_col2, in_col1) is True:
        ou_col2, ou_col1 = deplacer(in_col2, in_col1)
        TourdeHanoi(nbmove+1, ou_col1, ou_col2, in_col3)
    elif verifcol(in_col2, in_col3) is True:
        ou_col2, ou_col3 = deplacer(in_col2, in_col3)
        TourdeHanoi(nbmove+1, in_col1, ou_col2, ou_col3)