"""
MAIN Pendu Console
DZIOPA Raphael 2024
UTF-8

"""

"""Import de la fonction"""
import VerConsole.PenduVocab as v #Import des mots
from random import randint


"""Fonctions de MAIN"""
image0 = ["""
  ___________   
  ___________
  ||//    |
  ||/     |
  ||
  ||
  ||
 /||\\
//||\\\\
=============
==   ===   ==
""","""
  ___________   
  ___________
  ||//    |
  ||/     |
  ||      O
  ||
  ||
 /||\\
//||\\\\
=============
==   ===   ==
""", """
  ___________   
  ___________
  ||//    |
  ||/     |
  ||      O
  ||      |
  ||
 /||\\
//||\\\\
=============
==   ===   ==
""","""
  ___________   
  ___________
  ||//    |
  ||/     |
  ||      O
  ||     /|
  ||
 /||\\
//||\\\\
=============
==   ===   ==
""","""
  ___________   
  ___________
  ||//    |
  ||/     |
  ||      O
  ||     /|\\
  ||
 /||\\
//||\\\\
=============
==   ===   ==
""","""
  ___________   
  ___________
  ||//    |
  ||/     |
  ||      O
  ||     /|\\
  ||     /
 /||\\
//||\\\\
=============
==   ===   ==
""","""
  ___________   
  ___________
  ||//    |
  ||/     |
  ||      O
  ||     /|\\
  ||     / \\
 /||\\
//||\\\\
=============
==   ===   ==
""","""
  ___________   
  ___________
  ||//    |
  ||/     |
  ||      0
  ||     /|\\
  ||     / \\
 /||\\
//||\\\\
=============
==   ===   ==
"""]

def userinfx():
#Traitement d'input text de l'utilisateur.
#Renvoie un requete jusqu'a qu'un bonne saisie est mise
#IN none
#OU txt
  numb = [0,1,2,3,4,5,6,7,8,9]
  forbidens = ["&","~","'","(","-","_",")","=","+","°","}","]","@","^","\\","|","/"]
  userin = input("Letter of choice : -> ")
  if len(userin) > 1:
    print("Error: Choice has <1 lettre")
    userinfx()
  elif userin in numb:
    print("Error: Choice has 1 Number")
    userinfx()
  elif userin in forbidens:
    print("Error: Choice has other character")
    userinfx()
  else:
    filtre1 = userin.replace("é","E").replace("è","E").replace("à","A").replace("ç","C")
    filtre2 = filtre1.upper()
    return filtre2

def chooseword():
#Choix d'un mot dans le fichier de vocabulaire
#IN none
#OU liste
  mots = v.vocab()
  i = randint(0, len(mots))
  listmot = mots[i-1].split()
  return listmot

def showpendus(used, mot):
#Affichage de pendus, du mots (plus ou moins complété) et des lettres utilisées
#IN liste,liste
#OU txt
  showword = []
  fails = 0

  for val in mot:
    if val in used:
      showword.append(val)
    elif val == "_":
      showword.append(" ")
    else:
      showword.append("_")

  for vals in used:
    if vals not in showword:
      fails += 1

  if fails == len(image0):
    return "GAME_OVER"
  elif "_" not in showword:
    return "GAME_WON"
  else:  
    print(showword)
    print(image0[fails])
    print("Letters used : ",used)

def runpendus():
#Mise en jeux des fonctions de MAIN
#IN none
#OU none
  mot = chooseword()
  used = []
  print("Hangman has chosen a word")
  while True:
    used.append(userinfx())
    status = showpendus(used,mot)
    if status == "GAME_OVER" or status == "GAME_WON":
      print(status)
      print("The word was :",mot)
      break