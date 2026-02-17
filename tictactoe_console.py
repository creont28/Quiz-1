import os
import time as t

# global variables

currPlayer = "X"
board = [" "] * 9

# clear termi
def clear():
    if os.name == 'nt': os.system('cls')
           
# tictactoe board
def gameBoard(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")
    
# get move logic
def getMove(board, currPlayer):
    while True:
        try:
            position = int(input(f"Player {currPlayer}, choose position (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid position. Choose 1-9.")
            elif board[position] != " ":
                print("That spot is already taken by the other player.")
            else:
                return position
        except:
            print("Please enter a valid number.")
    
# check win/lose/tie conditions
def winCheck(board, currPlayer):
    winCombi = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Check Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Check Columns
        [0, 4, 8], [2, 4, 6]             # Check Diagonals
    ]
    for triple in winCombi:
        if board[triple[0]] == board[triple[1]] == board[triple[2]] == currPlayer:
            return True
    return False
        
def tieCheck(board):
    return " " not in board
    
# run game
def playGame():
    global currPlayer
    # menu
    while True:
        clear()
        choice = input("Do you want to be X or O? ").upper()
        if choice in ["X", "O"]: 
            currPlayer = choice
            break
        else:
            print("Invalid choice. Please pick X or O.")
            t.sleep(1)
            
    # main game
    while True:
        clear()
        print("TIC TAC TOE")
        print(f"You are Player {currPlayer}!")
        gameBoard(board)
        move = getMove(board, currPlayer)
        board[move] = currPlayer
        
        if winCheck(board, currPlayer):
            clear()
            gameBoard(board)
            print(f"Player {currPlayer} wins the game!")
            break
        elif tieCheck(board):
            clear()
            gameBoard(board)
            print("It's a draw!")
            break
        else:
            if currPlayer == "X":
                currPlayer = "O"
            else:
                currPlayer = "X"
         
# main loop for whole
def main():
    while True:
        playGame()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

# start game
main()