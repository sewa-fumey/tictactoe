tableau_jeu = [
[" "," "," "],
[" "," "," "],
[" "," "," "] ]

def interface_tictactoe(tableau_jeu):

    print(" ", " ", "|", "1", "|", "2", "|", "3")
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

def interactions(joueur1, joueur2, tableau_jeu):
    while gagnant_oupas(tableau_jeu)[0] == False:
        choix_position = input("Choisissez la position : ")
        if choix_position == "A1":
            if joueur1 == True:
                tableau_jeu[0][0] = "X"
            elif joueur2 == True:
                tableau_jeu[0][0] = "O"
        elif choix_position == "A2":
            if joueur1 == True:
                tableau_jeu[0][1] = "X"
            elif joueur2 == True:
                tableau_jeu[0][1] = "O"
        elif choix_position == "A3":
            if joueur1 == True:
                tableau_jeu[0][2] = "X"
            elif joueur2 == True:
                tableau_jeu[0][2] = "O"
        elif choix_position == "B1":
            if joueur1 == True:
                tableau_jeu[1][0] = "X"
            elif joueur2 == True:
                tableau_jeu[1][0] = "O"
        elif choix_position == "B2":
            if joueur1 == True:
                tableau_jeu[1][1] = "X"
            elif joueur2 == True:
                tableau_jeu[1][1] = "O"
        elif choix_position == "B3":
            if joueur1 == True:
                tableau_jeu[1][2] = "X"
            elif joueur2 == True:
                tableau_jeu[1][2] = "O"
        elif tableau_jeu == "C1":
            if joueur1 == True:
                tableau_jeu[2][0] = "X"
            elif joueur2 == True:
                tableau_jeu[2][0] = "O"
        elif choix_position == "C2":
            if joueur1 == True:
                tableau_jeu[2][1] = "X"
            elif joueur2 == True:
                tableau_jeu[2][1] = "O"
        elif choix_position == "C3":
            if joueur1 == True:
                tableau_jeu[2][2] = "X"
            elif joueur2 == True:
                tableau_jeu[2][2] = "O"
        else : choix_position = input('Entrez une case existante (EX. A1, C3...):')


interface_tictactoe(tableau_jeu)

joueur1 = input("Joueur 1, entrez votre nom: ")
joueur2 = input("Joueur 2, entrez votre nom: ")
print("Bonjour,", joueur1, "c'est a vous de commencer !")

i = 0
while i == 0:
    joueur1 = True
    joueur2 = False
    interactions(joueur1, joueur2, tableau_jeu)
    gagnant_oupas(tableau_jeu)
i += 1
while i == 1: 
    joueur1 = False
    joueur2 = True
    interactions(joueur1, joueur2, tableau_jeu)
    gagnant_oupas(tableau_jeu)
i -= 1

if gagnant_oupas(tableau_jeu)[1] == "X":
    print("Victoire de", joueur1)
elif gagnant_oupas(tableau_jeu)[1] == "O":
    print("Victoire de", joueur2)
print(gagnant_oupas(tableau_jeu))