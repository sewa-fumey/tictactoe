#Interface
def interface_tictactoe():
    print(" " * 3, "A", "|", "B", "|", "C", " ")
    print(" ", "-------------")
    print(str("1"), "|", " ", "|", " ", "|", " ", "|")
    print("---------------")
    print(str("2"), "|", " ", "|", " ", "|", " ", "|")
    print("---------------")
    print(str("3"), "|", " ", "|", " ", "|", " ", "|")
    print(" ", "-------------")
    
interface_tictactoe()



#Conditions de victoire

listeA1B1C1 = [1, 2, 3]
listeA2B2C2 = [1, 2, 3]
listeA3B3C3 = [1, 2, 3]

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

#Faire boucle while, tant que c'est False, boucle continue, si True, finito. while not gagnant_oupas(etat_partie)[0]:

#Exemple : joueur vient de jouer
joueur1 = "Geraldine"
joueur2 = "François"
etat_partie = [
    ['X', 'O', 'X'], 
    ['O', 'X', ' '], 
    ['X', 'O', ' ']
    ]

"""
if gagnant_oupas(etat_partie)[1] == "X":
    print("Victoire de", joueur1)
elif gagnant_oupas(etat_partie)[1] == "O":
    print("Victoire de", joueur2)
print(gagnant_oupas(etat_partie))
"""

