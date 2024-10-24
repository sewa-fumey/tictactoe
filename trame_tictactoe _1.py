#nom_joueur1 = input("Joueur 1, entrez votre nom: ")
#nom_joueur2 = input("Joueur 2, entrez votre nom: ")
#print("Bonjour,", nom_joueur1, "c'est a vous de commencer !")

ligneA = ["A", " ", "|", " ",  " ", " ", "|", " ",  " ", " ", "|", " ",  " ", " ", "|"]
ligneB = ["B", " ", "|", " ",  " ", " ", "|", " ",  " ", " ", "|", " ",  " ", " ", "|"]
ligneC = ["C", " ", "|", " ",  " ", " ", "|", " ",  " ", " ", "|", " ",  " ", " ", "|"]

def interface_tictactoe():

    print(" " * 3, "1", "|", "2", "|", "3", " ")
    print(" ", "-------------")
    print(''.join(ligneA))
    print("---------------")
    print(''.join(ligneB))
    print("---------------")
    print(''.join(ligneC))
    print(" ", "-------------")
    

def gagnant_oupas(etat_partie): 
    """True = partie terminée, False = Partie continue. 
    Symbole du gagnant ou match nul"""
    if etat_partie[0][0] == etat_partie[1][1] == etat_partie[2][2] and etat_partie[0][0] in ["X","O"]:
        return True, etat_partie[0][0] 
    elif etat_partie[0][2] == etat_partie[1][1] == etat_partie[2][0] and etat_partie[0][2] in ["X","O"]:
        return True, etat_partie[0][2]
    elif etat_partie[0][0] == etat_partie[1][0] == etat_partie[2][0] and etat_partie[0][0] in ["X","O"]:
       return True, etat_partie[0][0]
    elif etat_partie[0][1] == etat_partie[1][1] == etat_partie[2][1] and etat_partie[0][1] in ["X","O"]:
        return True, etat_partie[0][1]
    elif etat_partie[0][2] == etat_partie[1][2] == etat_partie[2][2] and etat_partie[0][2] in ["X","O"]:
        return True, etat_partie[0][2]
    elif etat_partie[0][0] == etat_partie[0][1] == etat_partie[0][2] and etat_partie[0][0] in ["X","O"]:
        return True, etat_partie[0][0]
    elif etat_partie[1][0] == etat_partie[1][1] == etat_partie[1][2] and etat_partie[1][0] in ["X","O"]:
        return True, etat_partie[1][0]
    elif etat_partie[2][0] == etat_partie[2][1] == etat_partie[2][2] and etat_partie[2][0] in ["X","O"]:
        return True, etat_partie[2][0]
    else:
        for ligne in etat_partie:
            for element in ligne:
                if element == " ":
                    return False, "Continue"
        return True, "Match Nul"

def interactions(joueur):
    while gagnant_oupas is False: 
        choix_position = input("Choisissez la position : ")

    if choix_position == "A1":
        ligneA[4] = "X"
    elif choix_position == "A2":
        ligneA[8] = "X"
    elif choix_position == "A3":
        ligneA[12] = "X"
    elif choix_position == "B1":
        ligneB[4] = "X"
    elif choix_position == "B2":
        ligneB[8] = "X"
    elif choix_position == "B3":
        ligneB[12] = "X"
    elif choix_position == "C1":
        ligneC[4] = "X"
    elif choix_position == "C2":
        ligneC[8] = "X"
    elif choix_position == "C3":
        ligneC[12] = "X"
    else : choix_position = input('Entrez une case existante (EX. A1, C3...):\n')

if gagnant_oupas(etat_partie)[1] == "X":
    print("Victoire de", joueur1)
elif gagnant_oupas(etat_partie)[1] == "O":
    print("Victoire de", joueur2)
print(gagnant_oupas(etat_partie))
    