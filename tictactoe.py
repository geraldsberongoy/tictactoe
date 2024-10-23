#Tic Tac Toe game
def assigning_players():
    """Assign the players to X and O."""
    while True:
        player1 = input("Who is first player? (X or O): ").upper()
        if player1 not in ['X', 'O']:
            print("Please enter X or O")
            continue
        if player1 == 'X':
            player2 = 'O'
            playerx = 1
            playero = 2
        elif player1 == 'O':
            player2 = 'X'
            playero = 1
            playerx = 2
        return player1, player2, playerx, playero

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print("-" * 13)
        print("| ",end="")
        print(" | ".join(row),end="")
        print(" |")
    print("-" * 13)
    
def player_input(board, player, order):
    """Check if the player's input is valid."""
    while True:
        try:
            player_turn = input(f"Player {order}:{player}, enter your move(row column e.g.(1 3)): ").split()
            row , col = player_turn
            
            if any(1 > int(i) > 3  for i in player_turn):
                print("Invalid move. Please try again.")
                continue
                
            if board[int(row)-1][int(col)-1] != ' ':
                print("This space is already occupied. Please try again.")
                continue
            
            else:
                return row, col
        except Exception as e:
            print("Invalid move. Please try again.")
            continue

def check_winner(board, x, o):
    """Check if there is a winner."""
    if board[0] == ['X', 'X', 'X'] or board[1] == ['X', 'X', 'X'] or board[2] == ['X', 'X', 'X']:
        print(f"Player {x}(X) wins!")
        return True
    # Vertical X
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        print(f"Player {x}(X) wins!")
        return True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        print(f"Player {x}(X) wins!")
        return True
    
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print(f"Player {x}(X) wins!")
        return True
    # Diagonal X
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print(f"Player {x}(X) wins!")
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print(f"Player {x}(X) wins!")
        return True
    # Horizontal O
    elif board[0] == ['O', 'O', 'O'] or board[1] == ['O', 'O', 'O'] or board[2] == ['O', 'O', 'O']:
        print(f"Player {o}(O) wins!")
        return True
    # Vertical O
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        print(f"Player {o}(O) wins!")
        return True
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        print(f"Player {o}(O) wins!")
        return True
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        print(f"Player {o}(O) wins!")
        return True
    # Diagonal O
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        print(f"Player {o}:O wins!")
        return True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        print(f"Player {o}:O wins!")
        return True
    # No winner
    else:
        return False

# Main game loop
def main():
    player1, player2, playerx, playero = assigning_players()

    first = 1
    second = 2

    print(f"Player 1 is {player1} and Player 2 is {player2}.\n")

    # Initialize the board
    board = [[' ' for i in range(3)] for i in range(3)]
    print_board(board)

    print("\n")

    # Main game loop
    is_winner = False
    counter = 0 

    while True:
        # Player 1's turn
        row, col = player_input(board, player1, first)


        board[int(row)-1][int(col)-1] = player1
        print_board(board)
        
        is_winner = check_winner(board, playerx, playero)
        if is_winner:
            break
        
        counter += 1
        if counter == 9:
            print("It's a tie!")
            break
        
        # Player 2's turn
        row, col = player_input(board, player2, second)
        
        board[int(row)-1][int(col)-1] = player2
        print_board(board)
        
        # Check for a winner
        is_winner = check_winner(board, playerx, playero)
        if is_winner:
            break
        counter += 1

# Game loop
def play_game():
    while True:
        print("\n" + "-" * 50)
        print("Welcome to Tic Tac Toe!")
        print("Player 1 will be 'X' and Player 2 will be 'O'.")
        print("To make a move, enter the row and column number (1 1).")
        print("For example, to place your mark in the top left corner, enter '1 1'.")
        print("Let's begin!") 
        print("-" * 50 + "\n" )

        main()

        answer = input("Do you want to play again? (Y/N): ").upper()
        while answer not in ['Y', 'N']:
            print("Please enter Y or N.")
            answer = input("Do you want to play again? (Y/N): ").upper()
        
        if answer == 'N':
            print("Thanks for playing!")
            break  # Breaks out of the loop to stop the game

    print("Exiting...")

if __name__ == '__main__':
    play_game()
    

    