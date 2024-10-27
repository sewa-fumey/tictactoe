game_board = [
[" "," "," "],
[" "," "," "],
[" "," "," "] ]

def interface_tictactoe(game_board):  # displays the game interface ( first empty, then updated after each move ) using the hints and values of the control panel squares
    print(" ", " ", " ", "1", "|", "2", "|", "3") # interface column
    print("   ", "-------------")
    print(" ", "A", "|", (game_board[0][0]), "|", (game_board[0][1]), "|", (game_board[0][2]), "|")  # premiere ligne de l'interface 
    print("-----------------")
    print(" ", "B", "|", (game_board[1][0]), "|", (game_board[1][1]), "|", (game_board[1][2]), "|")
    print("-----------------")
    print(" ", "C", "|", (game_board[2][0]), "|", (game_board[2][1]), "|", (game_board[2][2]), "|")
    print("   ", "-------------")
    
def winner_or_not(game_state): 
    """ True = game ending, False = continue game.
    Winner's symbol or draw game.
    Remember that return make a list, True = [0], game_board[0][0] = [1]"""
    if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[0][0] in ["X","O"]: # victory conditions for the left to the right diagonal
        return True, game_state[0][0] 
    elif game_state[0][2] == game_state[1][1] == game_state[2][0] and game_state[0][2] in ["X","O"]:
        return True, game_state[0][2]
    elif game_state[0][0] == game_state[1][0] == game_state[2][0] and game_state[0][0] in ["X","O"]:
       return True, game_state[0][0]
    elif game_state[0][1] == game_state[1][1] == game_state[2][1] and game_state[0][1] in ["X","O"]:
        return True, game_state[0][1]
    elif game_state[0][2] == game_state[1][2] == game_state[2][2] and game_state[0][2] in ["X","O"]:
        return True, game_state[0][2]
    elif game_state[0][0] == game_state[0][1] == game_state[0][2] and game_state[0][0] in ["X","O"]:
        return True, game_state[0][0]
    elif game_state[1][0] == game_state[1][1] == game_state[1][2] and game_state[1][0] in ["X","O"]:
        return True, game_state[1][0]
    elif game_state[2][0] == game_state[2][1] == game_state[2][2] and game_state[2][0] in ["X","O"]:
        return True, game_state[2][0]
    else: 
        for ligne in game_state:
            for element in ligne:
                if element == " ":
                    return False, "Continue"
        return True, "Draw"

def interactions_1_player(game_board):
    turn_played = True
    positions = {
        "A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
        "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
        "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)
    }
    
    while True:
        interface_tictactoe(game_board)

        if turn_played:
            position_choice = input(f"{player} (X), select your position (A1, B2, C3...): ")

            if position_choice in positions:
                    x, y = positions[position_choice]
                    if game_board[x][y] == " ":
                        game_board[x][y] = "X"  
                        winner, symbol = winner_or_not(game_board)              
                        if winner: 
                            interface_tictactoe(game_board)
                            if symbol in ["X", "O"]:
                                if symbol == "X" : 
                                    print("Congratulations", player, ",YOU WIN !")
                                if symbol == "O": 
                                    print("You loose...")
                            else:
                                print("It's a draw !")
                            break # stops play in the event of a draw
                        turn_played = not turn_played  # Changement de tour
                    else:
                        print("This case is already taken, please select another one.")
            else:
                print('Select an existing case (EX. A1, C3...)') 

        else:
            turn_played = False
            for x in range(3):
                for y in range(3):
                    # On commence par permettre à l'IA d'assurer sa victoire dès que possible
                    if game_board[x][0] == "O" and game_board[x][1] == "O" and game_board[x][2] == " ":
                        game_board[x][2] = "O"
                        turn_played = True
                    if game_board[x][0] == "O" and game_board[x][2] == "O" and game_board[x][1] == " ":
                        game_board[x][1] = "O"
                        turn_played = True
                    if game_board[x][1] == "O" and game_board[x][2] == "O" and game_board[x][0] == " ":
                        game_board[x][0] = "O"
                        turn_played = True

                    # Vérification des colonnes
                    if game_board[0][y] == "O" and game_board[1][y] == "O" and game_board[2][y] == " ":
                        game_board[2][y] = "O"
                        turn_played = True
                    if game_board[0][y] == "O" and game_board[2][y] == "O" and game_board[1][y] == " ":
                        game_board[1][y] = "O"
                        turn_played = True
                    if game_board[1][y] == "O" and game_board[2][y] == "O" and game_board[0][y] == " ":
                        game_board[0][y] = "O"
                        turn_played = True

                    # Vérification des diagonales
                    if game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == " ":
                        game_board[2][2] = "O"
                        turn_played = True
                    if game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == " ":
                        game_board[2][0] = "O"
                        turn_played = True
                    if game_board[0][0] == "O" and game_board[2][2] == "O" and game_board[1][1] == " ":
                        game_board[1][1] = "O"
                        turn_played = True
                    if game_board[0][2] == "O" and game_board[2][0] == "O" and game_board[1][1] == " ":
                        game_board[1][1] = "O"
                        turn_played = True

                    # Vérification du blocage du joueur
                    if game_board[x][0] == "X" and game_board[x][1] == "X" and game_board[x][2] == " ":
                        game_board[x][2] = "O"
                        turn_played = True
                    if game_board[x][0] == "X" and game_board[x][2] == "X" and game_board[x][1] == " ":
                        game_board[x][1] = "O"
                        turn_played = True
                    if game_board[x][1] == "X" and game_board[x][2] == "X" and game_board[x][0] == " ":
                        game_board[x][0] = "O"
                        turn_played = True

                    # Vérification des colonnes pour bloquer le joueur
                    if game_board[0][y] == "X" and game_board[1][y] == "X" and game_board[2][y] == " ":
                        game_board[2][y] = "O"
                        turn_played = True
                    if game_board[0][y] == "X" and game_board[2][y] == "X" and game_board[1][y] == " ":
                        game_board[1][y] = "O"
                        turn_played = True
                    if game_board[1][y] == "X" and game_board[2][y] == "X" and game_board[0][y] == " ":
                        game_board[0][y] = "O"
                        turn_played = True

                    # Vérification des diagonales pour bloquer le joueur
                    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == " ":
                        game_board[2][2] = "O"
                        turn_played = True
                    if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == " ":
                        game_board[2][0] = "O"
                        turn_played = True

                    # Placement d'un "O" dans des cases vides pour remplir
                    if game_board[x][0] == "O" and game_board[x][1] == " " and game_board[x][2] == " ":
                        game_board[x][1] = "O"
                        turn_played = True
                    if game_board[0][y] == "O" and game_board[1][y] == " " and game_board[2][y] == " ":
                        game_board[1][y] = "O"
                        turn_played = True

                    # Placement d'un "O" dans des cases vides
                    if game_board[x][0] == " " and game_board[x][1] == " " and game_board[x][2] == " ":
                        game_board[x][0] = "O"
                        turn_played = True
                    if game_board[0][y] == " " and game_board[1][y] == " " and game_board[2][y] == " ":
                        game_board[0][y] = "O"
                        turn_played = True

                    if turn_played:
                        winner_or_not(game_board)
                        turn_played = True  #Tour du joueur
                        break  
                    
                if turn_played:
                    winner_or_not(game_board)
                    break  

def interactions_2_Players(game_board):  # step by step interactions of the game  
    turn_played = True
    positions = {
            "A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
            "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
            "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)
        }
    while True:
        interface_tictactoe(game_board)
        if turn_played:
            position_choice = input(f"{player1} (X), select your position (A1, B2, C3...): ")
        else:
            position_choice = input(f"{player2} (O), select your position (A1, B2, C3...): ")
       
        if position_choice in positions: # loop that checks whether or not there is a victory at each turn , depending on the player's positioning choices 
            x, y = positions[position_choice]
            if game_board[x][y] == " ":
                game_board[x][y] = "X" if turn_played else "O"
                winner, symbol = winner_or_not(game_board)              
                if winner: 
                    interface_tictactoe(game_board)
                    if symbol in ["X", "O"]:
                        print(f"Congratulations, {player1 if symbol == 'X' else player2} ! You won !")
                    else:
                        print("It's a draw !")
                    break # stops play in the event of a draw
                turn_played = not turn_played
            else:
                print("This case is already taken, please select another one.") # checks if this slot is free
        else:
            print("Select an existing case (EX. A1, C3...)")

game_mode_choice = input("Enter 1 for one player, 2 for Two players: ")

if game_mode_choice == "2":

    interface_tictactoe(game_board) # the start of the game
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    print(f"Hello {player1}, select a case to start the game !")

    interactions_2_Players(game_board) # playing of the game  

if game_mode_choice == "1":

    interface_tictactoe(game_board) # the start of the game
    player = input("Enter your name: ")
    print(f"Hello {player}, select a case to start the game !")

    interactions_1_player(game_board)