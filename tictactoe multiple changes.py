game_board = [
[" "," "," "],
[" "," "," "],
[" "," "," "] ]

def interface_tictactoe(game_board):

    print(" ", " ", " ", "1", "|", "2", "|", "3")
    print("   ", "-------------")
    print(" ", "A", "|", (game_board[0][0]), "|", (game_board[0][1]), "|", (game_board[0][2]), "|")
    print("-----------------")
    print(" ", "B", "|", (game_board[1][0]), "|", (game_board[1][1]), "|", (game_board[1][2]), "|")
    print("-----------------")
    print(" ", "C", "|", (game_board[2][0]), "|", (game_board[2][1]), "|", (game_board[2][2]), "|")
    print("   ", "-------------")
    
def winner_or_not(game_state): 
    """ True = game ending, False = continue game.
    Winner's symbol or draw game.
    Remember that return make a list, True = [0], game_board[0][0] = [1]"""
    if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[0][0] in ["X","O"]:
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

def interactions(game_board):
    player_turn = True
    while True:
        interface_tictactoe(game_board)
        if player_turn:
            position_choice = input(f"{player1} (X), select your position (A1, B2, C3...): ")
        else:
            position_choice = input(f"{player2} (O), select your position (A1, B2, C3...): ")
        positions = {
            "A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
            "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
            "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)
        }
        if position_choice in positions:
            x, y = positions[position_choice]
            if game_board[x][y] == " ":
                game_board[x][y] = "X" if player_turn else "O"
                winner, symbol = winner_or_not(game_board)              
                if winner:
                    interface_tictactoe(game_board)
                    if symbol in ["X", "O"]:
                        print(f"Congratulations, {player1 if symbol == 'X' else player2} ! You won !")
                    else:
                        print("It's a draw !")
                    break
                player_turn = not player_turn
            else:
                print("This case is already taken, please select another one.")
        else:
            print("Select an existing case (EX. A1, C3...).")

interface_tictactoe(game_board)
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")
print(f"Hello {player1}, select a case to start the game !")

interactions(game_board)