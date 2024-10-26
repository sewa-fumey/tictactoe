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
                
def interactions(tableau_jeu):
    tour_joueur = True
    positions = {
                "A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
                "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
                "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)
            }
    
    while gagnant_oupas(tableau_jeu) == False:
            interface_tictactoe(tableau_jeu) 
            if tour_joueur:
                choix_position = input("joueur, (X), choisissez la position (A1, B2, C3...): ")
            
                if choix_position in positions:
                    x, y = positions[choix_position]

                    if tableau_jeu[x][y] == " ":
                        if tour_joueur:
                            tableau_jeu[x][y] = "X"  
                            tour_joueur = not tour_joueur
                        
                    else:
                        print("Case déjà prise, essayez une autre position.")
                else:
                    print('Entrez une case existante (EX. A1, C3...)') 

            else:  #Ici on aurait pu encore optimiser le code en regroupant les condition, voir en creant des fonctions mais manque de temps
                turn_played = False
                for x in range(3): #Pour le moment l'IA couvre en partie les trois principes enoncees lorsque je l'ai concue, ce qui est un bon debut
                    if turn_played :
                        break
                    for y in range(3):
                            if tableau_jeu[x][y] == " ": #Evidement il faudrait aussi couvrir les diagonales et le sens inverse

                                #On commence par permettre a l'IA d'assurer sa victoire des que possible
                                if tableau_jeu[x][y] == "O" and tableau_jeu[x][(y+1) % 3] == "O": 
                                    tableau_jeu[x][(y+2) % 3] = "O" 
                                    tour_joueur = not tour_joueur #On declare le tour du joueur
                                    turn_played = True #On met fin au tour de l'IA et on evite une boucle infinie
                                elif tableau_jeu[x][y] == "O" and tableau_jeu[x][(y+2) % 3] == "O":
                                    tableau_jeu[x][(y+1) % 3] = "O" 
                                    tour_joueur = not tour_joueur
                                    turn_played = True
                                elif tableau_jeu[x][y] == "O" and tableau_jeu[(x+1) % 3][y] == "O":
                                    tableau_jeu[(x+2) % 3][y] = "O"  
                                    tour_joueur = not tour_joueur
                                    turn_played = True  
                                elif tableau_jeu[x][y] == "O" and tableau_jeu[(x+2) % 3][y] == "O":
                                    tableau_jeu[(x+1) % 3][y] = "O"
                                    tour_joueur = not tour_joueur
                                    turn_played = True

                                #Ensuite on conditionne le blocage du joueur des que possible
                                if tableau_jeu[x][y] == "X" and tableau_jeu[x][(y+1) % 3] == "X": 
                                    tableau_jeu[x][(y+2) % 3] = "O" 
                                    tour_joueur = not tour_joueur
                                    turn_played = True
                                elif tableau_jeu[x][y] == "X" and tableau_jeu[x][(y+2) % 3] == "X":
                                    tableau_jeu[x][(y+1) % 3] = "O" 
                                    tour_joueur = not tour_joueur
                                    turn_played = True
                                elif tableau_jeu[x][y] == "X" and tableau_jeu[(x+1) % 3][y] == "X":
                                    tableau_jeu[(x+2) % 3][y] = "O"  
                                    tour_joueur = not tour_joueur
                                    turn_played = True  
                                elif tableau_jeu[x][y] == "X" and tableau_jeu[(x+2) % 3][y] == "X":
                                    tableau_jeu[(x+1) % 3][y] = "O"
                                    tour_joueur = not tour_joueur
                                    turn_played = True
                                
                                #On conditionne la deuxieme phase de placement
                                elif tableau_jeu[x][y] == "O" and tableau_jeu[x][(y+1) % 3] == " " and tableau_jeu[x][(y+2) % 3] == " " : 
                                    tableau_jeu[x][(y+1) % 3] = "O"
                                    tour_joueur = not tour_joueur
                                    turn_played = True
                                elif tableau_jeu[x][y] == "O" and tableau_jeu[(x+1) %3][y] == " " and tableau_jeu[(x+2) % 3][y] == " " :
                                    tableau_jeu[(x+1) % 3][y] = "O"
                                    tour_joueur = not tour_joueur
                                    turn_played = True
                                
                                #Et enfin on conditionne la premiere phase de placement
                                elif (tableau_jeu[x][y] == " " and tableau_jeu[x][(y+1) % 3] == " " and tableau_jeu[x][(y+2) % 3] == " " or 
                                    tableau_jeu[x][y] == " " and tableau_jeu[(x+1) % 3][y] == " " and tableau_jeu[(x+2) % 3][y] == " "):
                                    tableau_jeu[x][y] = "O"
                                    tour_joueur = not tour_joueur 
                                    turn_played = True

                                turn_played = True #Peut etre repetitif ?
                                break                                

interactions(tableau_jeu)