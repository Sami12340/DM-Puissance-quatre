# *********************************
# Projet NSI : JEU DU PUISSANCE 4 
# Date: 17/02/2022
# Nom: HALHALI  
# Prénom: Sami
# *********************************


# --------------------------------------
# -------- INITIALISATION --------------
# --------------------------------------

# Variables GLOBALE (pourront être utilisées à l'intérieur de toutes nos fonctions)



jetons_joueur=['X','O'] # Contient la représentation des jetons: Joueur 1: 'X' et Joueur 2: 'O'
partie_terminee = False
num_joueur_courant = 1 # Numéros du joueur qui commence.
grille = []  # Contiendra la grille du Jeu



# -------------------------------------------------------------
# -------- FONCTIONS ET PROCEDURES ----------------------------
# -------------------------------------------------------------

def creation_grille_vierge():
    ''' Cette fonction va remplir la grille du jeu par des "."
    
        IN: Rien
        OUT: Rien car on va remplir la variable globale grille, déjà déclarée au tout début du programme
        
        On fabrique une liste de liste de string (de 1 caractère) modélisant notre grille de jeu de 6 lignes par 7 colonnes
            [ [".", ".", ".", "." , "." , "." , "."], 
              [".", ".", ".", "." , "." , "." , "."],
              ...
              [".", ".", ".", "." , "." , "." , "."] ]  
    '''
    # On déclare que l'on va utiliser la variable globale grille (déjà initialisée) 
    global grille
    
    # Pour chaque ligne
    for num_ligne in range(6):
        ligne = [] # on crée un nouveau tableau vide en mémoire
        for j in range(7): # On ajoute les sept éléments ".", séparémment.
            ligne.append(".")
            
        # On ajoute la nouvelle ligne à la grille
        grille.append(ligne)
    
    # Le travail est terminé, la variable globale grille est remplie, on quitte la procédure
    return

# ------ TEST TEMPORAIRE --------
#creation_grille_vierge()
#print(grille)




def affiche_grille() -> None :
    ''' Cette fonction affiche la grille de jeu telle que ci-dessous
    IN: Rien
    OUT: Rien
    Affichage souhaitée :
       0 1 2 3 4 5 6 
  
    0 |.|.|.|.|.|.|.|
    1 |.|.|.|.|.|.|.|
    2 |.|.|.|.|.|.|.|
    3 |.|.|.|.|.|.|.|
    4 |.|.|.|X|.|.|.|
    5 |O|X|.|X|O|X|O|
      ---------------
    '''
    global grille
    
    # Affichage des indices du haut de la grille (0 à 6)
    print("")
    print("   ", end="")
    for i in range(7):
        print(str(i)+" ",end="")
    print("\n  ") # '\n' est un saut de ligne  (passage à une nouvelle ligne) suivi de deux espaces
    
    # Affichage des lignes
    for i in range(6): # Pour chaque ligne i
        print(str(i)+" ",end="")
        for j in range(7): # Pour chaque colonne j
            print("|"+ grille[i][j],end ="")
        print("|")
        
    # Affichage du trait en bas de la grille
    print("  ............... ", end="")
    print("\n")
    
    
# -------- TEST TEMPORAIRE ------------
''''''
#grille[5][1] = "X"
#grille[5][0] = "O"
#grille[5][3] = "X"
#grille[5][4] = "O"
#grille[5][5] = "X"
#grille[5][6] = "O"
#grille[4][3] = "X"

#affiche_grille()
''''''



def colonne_pleine(indice_colonne: int) -> bool:
    '''
        IN: indice de la colonne à analyser (0 à 6)
        OUT: un booleen (True si la colonne est déjà pleine, False sinon)
    '''
    global grille
    global pleine
    pleine = True
    for i in range(6):                              #pass par toute la colonne
        if grille[i][indice_colonne] == ".":        # vérifie si il y a un espace vide
            pass
        else:                                       # si il n y'en a pas cela veut dire que la colonne n'est pas vide
            return True
        
        return False                                
# --------- TEST TEMPORAIRE --------------

''''''
#grille[0][0] = "O"
#grille[1][0] = "O"
#grille[2][0] = "X"
#grille[3][0] = "O"
#grille[4][0] = "X"
#grille[5][0] = "O"
#colonne_pleine(0)
#print(pleine)
#.......
''''''




def joue_jeton(num_joueur: int, indice_colonne: int) -> None:
    ''' Place un jeton du joueur numéros num_joueur, dans la colonne indice_colonne.
    
        IN: num_joueur (int qui vaut 1 ou 2)
        OUT: Rien puisque cette fonction va modifier directement la variable global grille.
    '''
    # On utilise les deux variables globales suivantes
    global grille
    global jetons_joueur

    # Dans la colonne indice_colonne, en partant, du bas, on cherche la première case vide.
    for i in range(5, -1, -1):    #pass du haut vers le bas
        if grille[i][indice_colonne] == ".":     #à la premiere case vide on pose un jetons dépendants de si cest le joueur 1 ou 2 il pose une X ou O
            if num_joueur == 0:
                grille[i][indice_colonne] = "X"
                break
            elif num_joueur == 1:   
                grille[i][indice_colonne] = "O"
                break

# ------------ TEST TEMPORAIRE ----------------

'''

joue_jeton(1, 3)  # Joueur 1 joue
affiche_grille()

joue_jeton(2, 0)  # Joueur 2 joue
affiche_grille()

joue_jeton(1, 3)  # Joueur 1 joue
affiche_grille()

joue_jeton(2, 0)  # Joueur 2 joue
affiche_grille()

'''








def demander_ou_jouer() -> int:
    ''' Doit demander au joueur dans quel indice de colonne il souhaite jouer.
        Si l'indice n'est pas valable (non compris entre 0 et 6), ou bien s'il correspond à une colonne pleine, on lui indique
        que sa saisie est incorrecte et on lui renouvelle la question.
        Si l'utilisateur saisie 'Q' (pour "Quitter"), la partie doit se terminer.
        IN: rien
        OUT: Renvoie un indice de colonne (int) valable (colonne non pleine) où l'on peut jouer.
    '''
    
    while True:
        saisie = input("Dans quel indice de colonne souhaiter vous jouez de 0 à 6 et Q pour quiter?: ")
        
        if len(saisie) == 1 and (saisie in "0, 1, 2, 3 , 4, 5, 6, Q"):  #fait en sorte que seule les saisie autoriser peuvent etre accepté
            #La saisie est correct (1 seul caractère et il est autorisé)
            if saisie == "Q":    #quit si Q est choisi
                print("\n")
                exit()
                
            # On vérifie que la colonne n'est pas pleine
            j = int(saisie)  #car on sait que seule des nimbre on les transforme en int pour pouvoir manipler le dictionaire 
            
            if colonne_pleine(j) == True:
                print("ATTENTION, cette colonne est déjà pleine !")
            else: #Sinon, il y a encore de la place 
                # On renvoie l'indice de la colonne choisie
                return j #nous renvoyons la colonne saisie
        else:
            print("SAISIE INCORRECTE")
        
# ------------ TEST TEMPORAIRE ----------------

'''
colonne = demander_ou_jouer()
joue_jeton(1, colonne)  # Joueur 1 joue
affiche_grille()
joue_jeton(2, colonne)  # Joueur 1 joue
affiche_grille()
joue_jeton(2, colonne)  # Joueur 1 joue
affiche_grille()
joue_jeton(1, colonne)  # Joueur 1 joue
affiche_grille()
joue_jeton(2, colonne)  # Joueur 1 joue
affiche_grille()
joue_jeton(2, colonne)  # Joueur 1 joue
affiche_grille()
colonne = demander_ou_jouer()
joue_jeton(1, colonne)  # Joueur 1 joue
affiche_grille()
        
'''


def Quatre_jetons_en_ligne(num_joueur: int) -> bool:
    '''
        IN: Numéros du joueur à détecter 1 ou 2
        OUT: booleen (True si 4 jetons alignés trouvés en ligne, False sinon)
    '''
    # On déclare les variables globales qui nous seront utiles
    global jetons_joueur
    global grille
    chaine = ""
    # définition du jeton à trouver
    jeton = jetons_joueur[num_joueur]
    
    chaine_a_trouver = jeton * 4

    for i in range(6):
        chaine += " "     #on ajoute cela pour évitr des erreurs comme si il y a 3 de suite dans une ligne possible, puis la premier de suivante est aussi remplies

        for j in range(7):
            chaine += grille[i][j]          #nous passons par toute les lignes un à une et les mettons dans une variable

    if chaine_a_trouver in chaine:   #si jamais la suite des quatre jetons est trouver dans la variable cela veut dire que il y a quatre jetons de suite

        return True    
    

    # Si on arrive ici, c'est qu'aucun alignement de 4 jetons n'a été trouvé en ligne
    return False
    
    
# ------------ TEST TEMPORAIRE ----------------

'''
grille[0][0] = "O"
grille[0][1] = "O"
grille[0][2] = "O"
grille[0][3] = "O"
if Quatre_jetons_en_ligne(1) == True:
    print("True")
else:
    print("False")    
affiche_grille()


grille[0][0] = "O"
grille[0][1] = "O"
grille[0][2] = "O"
grille[0][5] = "O"
if Quatre_jetons_en_ligne(1) == True:
    print("True")
else:
    print("False")    
affiche_grille()
 
'''


def Quatre_jetons_en_colonne(num_joueur: int) -> bool:
    '''
        IN: Numéros du joueur à détecter 1 ou 2
        OUT: booleen (True si 4 jetons alignés trouvés en ligne, False sinon)
    '''
    # On déclare les variables globales qui nous seront utiles
    global jetons_joueur
    global grille
    chaine = ""
    # définition du jeton à trouver
    jeton = jetons_joueur[num_joueur]
    
    chaine_a_trouver = jeton * 4

    for j in range(7):
        chaine += " "     #on ajoute cela pour évitr des erreurs comme si il y a 3 de suite dans une colonne possible, puis la premier de suivante est aussi remplies

        for i in range(6):                     #meme chose que précedament sauf que nous passons par les colonnes au lieu des lignes
            chaine += grille[i][j]
    if chaine_a_trouver in chaine:
        return True    
    

    # Si on arrive ici, c'est qu'aucun alignement de 4 jetons n'a été trouvé en ligne
    return False
    
    
# ------------ TEST TEMPORAIRE ----------------

'''
grille[0][0] = "O"
grille[1][0] = "O"
grille[2][0] = "O"
grille[3][0] = "O"
if Quatre_jetons_en_colonne(1) == True:
    print("True")
else:
    print("False")    
affiche_grille()

'''
'''
grille[0][0] = "O"
grille[1][0] = "O"
grille[2][0] = "O"
grille[4][0] = "O"
if Quatre_jetons_en_colonne(1) == True:
    print("True")
else:
    print("False")    
affiche_grille()
 
'''



def Quatre_jetons_diagonal(num_joueur: int) -> bool:
    '''
        IN: Numéros du joueur à détecter 1 ou 2.
        OUT: booleen (True si 4 jetons alignés trouvé en diagonale, False sinon)
    '''
    global grille
    global jetons_joueur
    
    jeton = jetons_joueur[num_joueur]
    
    chaine_a_trouver = jeton *4
    
    # ------------------------------------------------------
    # PARTIE 1 : Recherche sur les diagonales descendantes vers la droite:
    ''' 
    # On définit la liste des coordonnées des points de départ possible pour les diagonales descendantes vers la droite.
        0   1   2   3   4   5   6
    0   X   X   X   X           
    1   X   X   X   X          
    2   X   X   X   X         
    3                            
    4                      
    5  ___________________________                     

    '''

    
    chaine = ""

    for i in range(3):  #nous passons par une ligne
        a = i           #pour reset i à chaque boucle, pas utiles mais c'est une précaution
        for j in range(4): 
            chaine += grille[i][j]                      #commencons par une localisation qui peut commencer une suite puis nous incrémentons de 1 3 fois pour avoir
            chaine += grille[i+1][j+1]                  #une diagonale à la suite
            chaine += grille[i+2][j+2]
            chaine += grille[i+3][j+3]
            chaine += " "     #on ajoute cela pour évitr des erreurs comme si il y a 3 de suite dans un diagonale possible, puis la premier de suivante est aussi remplies

            i = a

    # Si un alignement en diagonale a été trouvé    
    if chaine_a_trouver in chaine:
        # Une diagonale complète trouvée
        print("VICTOIRE EN DIAGONALE DE " + jeton)   
        return True
        
    #----------------- FIN PARTIE 1 -----------------------
        
    
    # ------------------------------------------------------
    # PARTIE 2 : Recherche sur les diagonales descendantes vers la gauche:
    ''' 
    # On définit la liste des coordonnées des points de départ possible pour les diagonales descendantes vers la gauche.
        0   1   2   3   4   5   6
    0               X   X   X   X
    1               X   X   X   X 
    2               X   X   X   X
    3                            
    4                      
    5  ___________________________                     

    
'''
    chaine =""
    for i in range(3):
        a = i
        for j in range(6, 2, -1):
            chaine += grille[i][j]
            chaine += grille[i+1][j-1]
            chaine += grille[i+2][j-2]      #meme chose que avant mais cette fois nous désincrementons
            chaine += grille[i+3][j-3]
            chaine += " "     #on ajoute cela pour évitr des erreurs comme si il y a 3 de suite dans un diagonale possible, puis la premier de suivante est aussi remplies

            i = a

   #print(chaine)

    # Si un alignement en diagonale a été trouvé    
    if chaine_a_trouver in chaine:
        # Une diagonale complète trouvée
        
        return True

    #----------------- FIN PARTIE 2 -----------------

    
    # Si on arrive ici, aucune diagonale n'a été trouvée, on renvoie False
    return False

# ----------- TEST TEMPORAIRE -------------
'''
'''
'''
grille[3][2] = "O"
grille[2][1] = "O"
grille[1][0] = "O"
grille[4][3] = "O"

grille[3][3] = "X"
grille[2][4] = "X"
grille[1][5] = "X"
grille[0][6] = "X"


affiche_grille()
if Quatre_jetons_diagonal(0) == True:
    print("10")
else:
    print("20")    

'''




def Recherche_si_victoire(num_joueur) -> bool:
    '''
        IN: num_joueur (1 ou 2)
        OUT: un booléen (True si le joueur indiqué a gagné, False sinon)
    '''

    global type_victoire
    type_victoire = ""     #Pour que ca print si on a gangé en diagonale, 
                        #ligne ou collone suite à une victoire, on le met on global pour ne pas devoire à la definire dans une autre fonction
    
    if Quatre_jetons_diagonal(num_joueur) == True:     #verifie si une victoire a été trouvé pour les 3 type de victoire
        type_victoire = "VICTOIRE EN DIAGONALE"        #message de victoire
        return True
    if Quatre_jetons_en_colonne(num_joueur) == True:
        type_victoire = "VICTOIRE EN COLONNE"           #message de victoire
        return True
    if Quatre_jetons_en_ligne(num_joueur) == True:
        type_victoire = "VICTOIRE EN LIGNE"             #message de victoire
        return True
    
    return False

# ----------- TEST TEMPORAIRE -------------



'''

grille[3][3] = "X"
grille[2][4] = "X"
grille[1][5] = "X"
grille[0][6] = "X"

affiche_grille()
if Recherche_si_victoire(0) == True:
    print("Victoire")
else:
    print("Défaite")


grille[3][0] = "X"
grille[2][0] = "X"
grille[1][0] = "X"
grille[0][0] = "X"

affiche_grille()
if Recherche_si_victoire(0) == True:
    print("Victoire")
else:
    print("Défaite")

grille[0][3] = "O"
grille[0][2] = "O"
grille[0][1] = "O"
grille[0][0] = "O"

affiche_grille()
if Recherche_si_victoire(1) == True:
    print("Victoire")
else:
    print("Défaite")

    '''



def grille_pleine():



    '''
        IN: None.
        OUT: booleen (True si pleine, False sinon)

    '''


    chaine = ""
    for j in range(7):                   #Nous allons seulements vérifier si la grille du haut est pleine car si celle ci est pleine cela veut dire que toute la grille l'est
        chaine += grille[0][j]      #i est égale à 0 car c'est suelemnt la ligne du haut qu'on test, j incrmente de 1 pour tester toute les collones, nous ajoutons le résultats à chaine


    if "." in chaine:    #si il y a un point dans la ligne du haut cela veut dire qu'elle n'est pas pleine donc on retourn False.
        return False
    else:
        return True        #si il n'y a pas de points cela veut dire que la ligne est donc la grille est pleine









# --------------------------------------
# -------- PROGRAMME PRINCIPAL ---------
# --------------------------------------

creation_grille_vierge()
affiche_grille()
num_joueur_courant=0
forme = "X"     #pour print le jeton
# Tant que la partie n'est pas terminée, un joueur joue.
while partie_terminee==False:
    
    print("Joueur  ",num_joueur_courant+1, "   (", forme,")   " )    # message pour que le joueur sache que c'est à lui et quelle est son jeton

    colonne = demander_ou_jouer()
    print("Vous jouez dans la colonne: ", colonne)
    if grille_pleine == True:
        print("La grille est pleine, c'est une égalité:\n")       #vérifie que la grille soit pleine, si c'est le cas une égalité est déclencher
        break
    else:

        if colonne_pleine(colonne) == True:
            print("La colonne est pleine choisissez une autre:\n")
        else:
            joue_jeton(num_joueur_courant, colonne)
            if Recherche_si_victoire(num_joueur_courant) == True:
                affiche_grille()    #car on va break la fonction affice_grille ne sera pas utiliser donc on ne pourra pas voire la grille finale, donc on le met ici au cas d'une victoire
                print("")
                print(type_victoire)
                print("")
                print("Le joueur ", num_joueur_courant+1,"  (", forme, ")   a gangé!. \n")     #donne le message de victoire finale

                break
            else:
                pass
    affiche_grille()     #affiche la grille à chhaque passage
    print("\n")
    
    
    # On change le numéros du joueur courant
    if num_joueur_courant==0:
        num_joueur_courant=1
        forme = "O"
    else:
        num_joueur_courant=0
        forme = "X"
# FIN DU WHILE        
        
# On est sorti de la boucle donc:
print("FIN DE PARTIE")        