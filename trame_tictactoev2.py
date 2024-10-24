tableau_jeu = [
[" "," "," "],
[" "," "," "],
[" "," "," "]
]

def interface_tictactoe(tableau_jeu):

    print("A", " ", "|", "1", "|", "2", "|", "3")
    print(" ", "-------------")
    print("A", " ", "|", (tableau_jeu[0][0]), "|", (tableau_jeu[0][1]), "|", (tableau_jeu[0][2]), "|")
    print("---------------")
    print("B", " ", "|", (tableau_jeu[1][0]), "|", (tableau_jeu[1][1]), "|", (tableau_jeu[1][2]), "|")
    print("---------------")
    print("C", " ", "|", (tableau_jeu[2][0]), "|", (tableau_jeu[2][1]), "|", (tableau_jeu[2][2]), "|")
    print(" ", "-------------")
    
def gagnant_oupas(tableau_jeu): 
    """True = partie terminée, False = Partie continue. 
    Symbole du gagnant ou match nul"""
    if tableau_jeu[0][0] == tableau_jeu[1][1] == tableau_jeu[2][2] and tableau_jeu[0][0] in ["X","O"]:
        return True, tableau_jeu[0][0] 
    elif tableau_jeu[0][2] == tableau_jeu[1][1] == tableau_jeu[2][0] and tableau_jeu[0][2] in ["X","O"]:
        return True, tableau_jeu[0][2]
    elif tableau_jeu[0][0] == tableau_jeu[1][0] == tableau_jeu[2][0] and tableau_jeu[0][0] in ["X","O"]:
       return True, tableau_jeu[0][0]
    elif tableau_jeu[0][1] == tableau_jeu[1][1] == tableau_jeu[2][1] and tableau_jeu[0][1] in ["X","O"]:
        return True, tableau_jeu[0][1]
    elif tableau_jeu[0][2] == tableau_jeu[1][2] == tableau_jeu[2][2] and tableau_jeu[0][2] in ["X","O"]:
        return True, tableau_jeu[0][2]
    elif tableau_jeu[0][0] == tableau_jeu[0][1] == tableau_jeu[0][2] and tableau_jeu[0][0] in ["X","O"]:
        return True, tableau_jeu[0][0]
    elif tableau_jeu[1][0] == tableau_jeu[1][1] == tableau_jeu[1][2] and tableau_jeu[1][0] in ["X","O"]:
        return True, tableau_jeu[1][0]
    elif tableau_jeu[2][0] == tableau_jeu[2][1] == tableau_jeu[2][2] and tableau_jeu[2][0] in ["X","O"]:
        return True, tableau_jeu[2][0]
    else:
        for ligne in tableau_jeu:
            for element in ligne:
                if element == " ":
                    return False, "Continue"
        return True, "Match Nul"

def interactions(joueur1, joueur2):
    while gagnant_oupas is False: 
        tableau_jeu = input("Choisissez la position : ")

    if tableau_jeu == "A1":
        if joueur1 == True:
            tableau_jeu[0][0] = "X"
        elif joueur2 == True:
            tableau_jeu[0][0] = "O"
    elif tableau_jeu == "A2":
        if joueur1 == True:
            tableau_jeu[0][1] = "X"
        elif joueur2 == True:
            tableau_jeu[0][1] = "O"
    elif tableau_jeu == "A3":
        if joueur1 == True:
            tableau_jeu[0][2] = "X"
        elif joueur2 == True:
            tableau_jeu[0][2] = "O"
    elif tableau_jeu == "B1":
        if joueur1 == True:
            tableau_jeu[1][0] = "X"
        elif joueur2 == True:
            tableau_jeu[1][0] = "O"
    elif tableau_jeu == "B2":
        if joueur1 == True:
            tableau_jeu[1][1] = "X"
        elif joueur2 == True:
            tableau_jeu[1][1] = "O"
    elif tableau_jeu == "B3":
        if joueur1 == True:
            tableau_jeu[1][2] = "X"
        elif joueur2 == True:
            tableau_jeu[1][2] = "O"
    elif tableau_jeu == "C1":
        if joueur1 == True:
            tableau_jeu[2][0] = "X"
        elif joueur2 == True:
            tableau_jeu[2][0] = "O"
    elif tableau_jeu == "C2":
        if joueur1 == True:
            tableau_jeu[2][1] = "X"
        elif joueur2 == True:
            tableau_jeu[2][1] = "O"
    elif tableau_jeu == "C3":
        if joueur1 == True:
            tableau_jeu[2][2] = "X"
        elif joueur2 == True:
            tableau_jeu[2][2] = "O"
    else : tableau_jeu = input('Entrez une case existante (EX. A1, C3...):\n')


joueur1 = input("Joueur 1, entrez votre nom: ")
joueur2 = input("Joueur 2, entrez votre nom: ")
print("Bonjour,", joueur1, "c'est a vous de commencer !")


if gagnant_oupas(tableau_jeu)[1] == "X":
    print("Victoire de", joueur1)
elif gagnant_oupas(tableau_jeu)[1] == "O":
    print("Victoire de", joueur2)
print(gagnant_oupas(tableau_jeu))