tableau = [
[" "," "," "],
[" "," "," "],
[" "," "," "]
]

def interface_tictactoe(tableau):

    print("A", " ", "|", "1", "|", "2", "|", "3")
    print(" ", "-------------")
    print("A", " ", "|", (tableau[0][0]), "|", (tableau[0][1]), "|", (tableau[0][2]), "|")
    print("---------------")
    print("B", " ", "|", (tableau[1][0]), "|", (tableau[1][1]), "|", (tableau[1][2]), "|")
    print("---------------")
    print("C", " ", "|", (tableau[2][0]), "|", (tableau[2][1]), "|", (tableau[2][2]), "|")
    print(" ", "-------------")
    
def gagnant_oupas(tableau): 
    """True = partie terminée, False = Partie continue. 
    Symbole du gagnant ou match nul"""
    if tableau[0][0] == tableau[1][1] == tableau[2][2] and tableau[0][0] in ["X","O"]:
        return True, tableau[0][0] 
    elif tableau[0][2] == tableau[1][1] == tableau[2][0] and tableau[0][2] in ["X","O"]:
        return True, tableau[0][2]
    elif tableau[0][0] == tableau[1][0] == tableau[2][0] and tableau[0][0] in ["X","O"]:
       return True, tableau[0][0]
    elif tableau[0][1] == tableau[1][1] == tableau[2][1] and tableau[0][1] in ["X","O"]:
        return True, tableau[0][1]
    elif tableau[0][2] == tableau[1][2] == tableau[2][2] and tableau[0][2] in ["X","O"]:
        return True, tableau[0][2]
    elif tableau[0][0] == tableau[0][1] == tableau[0][2] and tableau[0][0] in ["X","O"]:
        return True, tableau[0][0]
    elif tableau[1][0] == tableau[1][1] == tableau[1][2] and tableau[1][0] in ["X","O"]:
        return True, tableau[1][0]
    elif tableau[2][0] == tableau[2][1] == tableau[2][2] and tableau[2][0] in ["X","O"]:
        return True, tableau[2][0]
    else:
        for ligne in tableau:
            for element in ligne:
                if element == " ":
                    return False, "Continue"
        return True, "Match Nul"

def interactions(joueur1, joueur2):
    while gagnant_oupas is False: 
        tableau = input("Choisissez la position : ")

    if tableau == "A1":
        if joueur1 == True:
            tableau[0][0] = "X"
        elif joueur2 == True:
            tableau[0][0] = "0"
    elif tableau == "A2":
        if joueur1 == True:
            tableau[0][1] = "X"
        elif joueur2 == True:
            tableau[0][1] = "0"
    elif tableau == "A3":
        if joueur1 == True:
            tableau[0][2] = "X"
        elif joueur2 == True:
            tableau[0][2] = "0"
    elif tableau == "B1":
        if joueur1 == True:
            tableau[1][0] = "X"
        elif joueur2 == True:
            tableau[1][0] = "0"
    elif tableau == "B2":
        if joueur1 == True:
            tableau[1][1] = "X"
        elif joueur2 == True:
            tableau[1][1] = "0"
    elif tableau == "B3":
        if joueur1 == True:
            tableau[1][2] = "X"
        elif joueur2 == True:
            tableau[1][2] = "0"
    elif tableau == "C1":
        if joueur1 == True:
            tableau[2][0] = "X"
        elif joueur2 == True:
            tableau[2][0] = "0"
    elif tableau == "C2":
        if joueur1 == True:
            tableau[2][1] = "X"
        elif joueur2 == True:
            tableau[2][1] = "0"
    elif tableau == "C3":
        if joueur1 == True:
            tableau[2][2] = "X"
        elif joueur2 == True:
            tableau[2][2] = "0"
    else : tableau = input('Entrez une case existante (EX. A1, C3...):\n')


joueur1 = input("Joueur 1, entrez votre nom: ")
joueur2 = input("Joueur 2, entrez votre nom: ")
print("Bonjour,", joueur1, "c'est a vous de commencer !")


if gagnant_oupas(tableau)[1] == "X":
    print("Victoire de", joueur1)
elif gagnant_oupas(tableau)[1] == "O":
    print("Victoire de", joueur2)
print(gagnant_oupas(tableau))