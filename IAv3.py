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
    print("                  ")

def gagnant_oupas(tableau_jeu):
    
    if tableau_jeu[0][0] == tableau_jeu[1][1] == tableau_jeu[2][2] and tableau_jeu[0][0] in ["X","O"]:
        if tableau_jeu[0][0] == "X":
            print("joueur, you won !")
        else: print("Game won !")
        return True
    elif tableau_jeu[0][2] == tableau_jeu[1][1] == tableau_jeu[2][0] and tableau_jeu[0][2] in ["X","O"]:
        if tableau_jeu[0][2] == "X":
            print("joueur, you won !")
        else: print("Game won !")
        return True
    elif tableau_jeu[0][0] == tableau_jeu[1][0] == tableau_jeu[2][0] and tableau_jeu[0][0] in ["X","O"]:
        if tableau_jeu[0][0] == "X":
            print("joueur, you won !")
        else: print("Game won !")
        return True
    elif tableau_jeu[0][1] == tableau_jeu[1][1] == tableau_jeu[2][1] and tableau_jeu[0][1] in ["X","O"]:
        if tableau_jeu[0][1] == "X":
            print("joueur, you won !")
        else: print("Game won !")
        return True
    elif tableau_jeu[0][2] == tableau_jeu[1][2] == tableau_jeu[2][2] and tableau_jeu[0][2] in ["X","O"]:
        if tableau_jeu[0][2] == "X":
            print("joueur, you won !")
        else: print("Game won !")
        return True
    elif tableau_jeu[0][0] == tableau_jeu[0][1] == tableau_jeu[0][2] and tableau_jeu[0][0] in ["X","O"]:
        if tableau_jeu[0][0] == "X":
            print("joueur, you won !")
        else: print("Game won !")
        return True
    elif tableau_jeu[1][0] == tableau_jeu[1][1] == tableau_jeu[1][2] and tableau_jeu[1][0] in ["X","O"]:
        if tableau_jeu[1][0] == "X":
           print("joueur, you won !")
        else: print("Game won !")
        return True
    elif tableau_jeu[2][0] == tableau_jeu[2][1] == tableau_jeu[2][2] and tableau_jeu[2][0] in ["X","O"]:
        if tableau_jeu[2][0] == "X":
            print("joueur, you won !")
        else: print("Game won !")
        return True
    else:
        for ligne in tableau_jeu:
            for element in ligne:
                if element == " ":
                    return False
                '''elif element == "X" or "O":
                    print("Draw !")'''
                
def interactions_1_player(tableau_jeu):
    tour_joueur = True
    positions = {
        "A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
        "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
        "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)
    }
    
    while True:
        interface_tictactoe(tableau_jeu)
        
        if gagnant_oupas(tableau_jeu):
            break

        if tour_joueur:
            choix_position = input("joueur (X), choisissez la position (A1, B2, C3...): ")

            if choix_position in positions:
                x, y = positions[choix_position]

                if tableau_jeu[x][y] == " ":
                    tableau_jeu[x][y] = "X"  
                    tour_joueur = False  # Changement de tour
                else:
                    print("Case déjà prise, essayez une autre position.")
            else:
                print('Entrez une case existante (EX. A1, C3...)') 

        else:
            turn_played = False
            for x in range(3):
                for y in range(3):
                    # On commence par permettre à l'IA d'assurer sa victoire dès que possible
                    if tableau_jeu[x][0] == "O" and tableau_jeu[x][1] == "O" and tableau_jeu[x][2] == " ":
                        tableau_jeu[x][2] = "O"
                        turn_played = True
                    if tableau_jeu[x][0] == "O" and tableau_jeu[x][2] == "O" and tableau_jeu[x][1] == " ":
                        tableau_jeu[x][1] = "O"
                        turn_played = True
                    if tableau_jeu[x][1] == "O" and tableau_jeu[x][2] == "O" and tableau_jeu[x][0] == " ":
                        tableau_jeu[x][0] = "O"
                        turn_played = True

                    # Vérification des colonnes
                    if tableau_jeu[0][y] == "O" and tableau_jeu[1][y] == "O" and tableau_jeu[2][y] == " ":
                        tableau_jeu[2][y] = "O"
                        turn_played = True
                    if tableau_jeu[0][y] == "O" and tableau_jeu[2][y] == "O" and tableau_jeu[1][y] == " ":
                        tableau_jeu[1][y] = "O"
                        turn_played = True
                    if tableau_jeu[1][y] == "O" and tableau_jeu[2][y] == "O" and tableau_jeu[0][y] == " ":
                        tableau_jeu[0][y] = "O"
                        turn_played = True

                    # Vérification des diagonales
                    if tableau_jeu[0][0] == "O" and tableau_jeu[1][1] == "O" and tableau_jeu[2][2] == " ":
                        tableau_jeu[2][2] = "O"
                        turn_played = True
                    if tableau_jeu[0][2] == "O" and tableau_jeu[1][1] == "O" and tableau_jeu[2][0] == " ":
                        tableau_jeu[2][0] = "O"
                        turn_played = True
                    if tableau_jeu[0][0] == "O" and tableau_jeu[2][2] == "O" and tableau_jeu[1][1] == " ":
                        tableau_jeu[1][1] = "O"
                        turn_played = True
                    if tableau_jeu[0][2] == "O" and tableau_jeu[2][0] == "O" and tableau_jeu[1][1] == " ":
                        tableau_jeu[1][1] = "O"
                        turn_played = True

                    # Vérification du blocage du joueur
                    if tableau_jeu[x][0] == "X" and tableau_jeu[x][1] == "X" and tableau_jeu[x][2] == " ":
                        tableau_jeu[x][2] = "O"
                        turn_played = True
                    if tableau_jeu[x][0] == "X" and tableau_jeu[x][2] == "X" and tableau_jeu[x][1] == " ":
                        tableau_jeu[x][1] = "O"
                        turn_played = True
                    if tableau_jeu[x][1] == "X" and tableau_jeu[x][2] == "X" and tableau_jeu[x][0] == " ":
                        tableau_jeu[x][0] = "O"
                        turn_played = True

                    # Vérification des colonnes pour bloquer le joueur
                    if tableau_jeu[0][y] == "X" and tableau_jeu[1][y] == "X" and tableau_jeu[2][y] == " ":
                        tableau_jeu[2][y] = "O"
                        turn_played = True
                    if tableau_jeu[0][y] == "X" and tableau_jeu[2][y] == "X" and tableau_jeu[1][y] == " ":
                        tableau_jeu[1][y] = "O"
                        turn_played = True
                    if tableau_jeu[1][y] == "X" and tableau_jeu[2][y] == "X" and tableau_jeu[0][y] == " ":
                        tableau_jeu[0][y] = "O"
                        turn_played = True

                    # Vérification des diagonales pour bloquer le joueur
                    if tableau_jeu[0][0] == "X" and tableau_jeu[1][1] == "X" and tableau_jeu[2][2] == " ":
                        tableau_jeu[2][2] = "O"
                        turn_played = True
                    if tableau_jeu[0][2] == "X" and tableau_jeu[1][1] == "X" and tableau_jeu[2][0] == " ":
                        tableau_jeu[2][0] = "O"
                        turn_played = True

                    # Placement d'un "O" dans des cases vides pour remplir
                    if tableau_jeu[x][0] == "O" and tableau_jeu[x][1] == " " and tableau_jeu[x][2] == " ":
                        tableau_jeu[x][1] = "O"
                        turn_played = True
                    if tableau_jeu[0][y] == "O" and tableau_jeu[1][y] == " " and tableau_jeu[2][y] == " ":
                        tableau_jeu[1][y] = "O"
                        turn_played = True

                    # Placement d'un "O" dans des cases vides
                    if tableau_jeu[x][0] == " " and tableau_jeu[x][1] == " " and tableau_jeu[x][2] == " ":
                        tableau_jeu[x][0] = "O"
                        turn_played = True
                    if tableau_jeu[0][y] == " " and tableau_jeu[1][y] == " " and tableau_jeu[2][y] == " ":
                        tableau_jeu[0][y] = "O"
                        turn_played = True

                    if turn_played:
                        gagnant_oupas(tableau_jeu)
                        tour_joueur = True  #Tour du joueur
                        break  
                    
                if turn_played:
                    gagnant_oupas(tableau_jeu)
                    break  

            

interactions(tableau_jeu)