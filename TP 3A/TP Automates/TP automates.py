"""
TP Automates
MAIN
DZIOPA Raphael

Fichier de L'automate Comportant les fonctions.

"""

mattest=[[1,0,0,4,0,0],
         [1,2,0,4,1,0],
         [1,0,3,0,2,0],
         [5,0,0,7,0,9],
         [1,0,3,4,0,0],
         [1,6,0,4,5,0],
         [1,0,0,4,6,9],
         [1,0,0,4,0,9],
         [1,0,0,4,0,0]]

def converstion(inlist):
#Fonction qui enlève certaincaractères spéciaux et sépare les mots de l'input
#IN txt
#OU liste
    oulist = inlist.replace(";"," ").replace(","," ").replace("?"," ").replace("!"," ")
    cutlist = oulist.split()
    return cutlist    

def trsnfchiffre(inlist):
#Fonction qui prends un liste de mots et leur attribu leur numéro d'état
#IN liste
#OU liste
    nblist = []
    dico ={"le" : 0, "la" : 0, "chat" : 1, "souris" : 1, "martin" : 3,
                "mange" : 2, "la" : 0, "petite" : 4, "joli" : 4, "grosse" : 4,
                "bleu" : 4, "verte" : 4, "dort" : 2,"julie" : 3, "jean" : 3, "." : 5}
    
    for val in inlist:
        if val in dico:
            nblist.append(dico[val])
    return nblist

def matfiltre(inmat, inlist):

    

print(converstion("le chat petite souris la joli julie mange jean ."))
print(trsnfchiffre(converstion("le chat petite souris la joli julie mange jean .")))