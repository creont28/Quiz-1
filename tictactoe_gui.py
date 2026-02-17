import tkinter
import random

# global vars
playerX = "X"
playerO = "O"
currPlayer = playerX
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]
isBot = False

colorBlue = "#4584b6"
colorEmerald = "#2ecc71"
colorGray = "#343434"
colorLGray = "#646464"

turns = 0
gameOver = False
scoreX = 0
scoreO = 0
scoreTies = 0

# FUNCTIONSSSS

def bot_move():
    if gameOver: return
    
    empty_cells = []
    for row in range(3):
        for column in range(3):
            if board[row][column]["text"] == "":
                empty_cells.append((row, column))
    
    if empty_cells:
        row, column = random.choice(empty_cells)
        set_tile(row, column)
        
def set_tile(row, column):
    global currPlayer
    if gameOver:
        return
    
    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = currPlayer
    board[row][column].config(background=colorGray) # this is for resetting hover
    winCheck()
    
    if not gameOver:
        if currPlayer == playerX:   
            currPlayer = playerO  
        else: 
            currPlayer = playerX        
        label.config(text=f"{currPlayer}'s turn")
    
    if isBot and currPlayer == playerO:
            window.after(1000, bot_move)

    
def winCheck():
    global turns, gameOver
    turns += 1
    
    # row
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            declareWinner(board[row][0]["text"])
            for col in range(3):
                board[row][col].config(foreground=colorEmerald, background=colorLGray)
            return

    # column
    for col in range(3):
        if (board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"]
            and board[0][col]["text"] != ""):
            declareWinner(board[0][col]["text"])
            for row in range(3):
                board[row][col].config(foreground=colorEmerald, background=colorLGray)
            return
        
    # left diag
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        declareWinner(board[0][0]["text"])
        for i in range(3):
            board[i][i].config(foreground=colorEmerald, background=colorLGray)
        return
    
    # right diag
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        declareWinner(board[0][2]["text"])
        board[0][2].config(foreground=colorEmerald, background=colorLGray)
        board[1][1].config(foreground=colorEmerald, background=colorLGray)
        board[2][0].config(foreground=colorEmerald, background=colorLGray)
        return

    # tie check
    if turns == 9:
        global scoreTies
        scoreTies += 1
        updateScore()
        gameOver = True
        label.config(text="It's a Tie!", foreground=colorEmerald)

def declareWinner(winner):
    global gameOver, scoreX, scoreO
    label.config(text=f"{winner} is the winner!", foreground=colorEmerald)
    gameOver = True
    if winner == playerX: scoreX += 1
    else: scoreO += 1
    updateScore()

def updateScore():
    score_label.config(text=f"X: {scoreX}   |   O: {scoreO}   |   Ties: {scoreTies}")
    
def playGame():
    global turns, gameOver, currPlayer
    
    turns = 0
    gameOver = False
    currPlayer = playerX 
    label.config(text=currPlayer + "'s turn", foreground="white")
    
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", background=colorGray, foreground=colorBlue)
            
# hover effect
def on_enter(e):
    if not gameOver and e.widget['text'] == "":
        e.widget['background'] = colorLGray

def on_leave(e):
    if not gameOver and e.widget['text'] == "":
        e.widget['background'] = colorGray

# nav func for main menu

def startPVP():
    global isBot
    isBot = False
    menu_frame.pack_forget()
    game_frame.pack(expand=True, fill="both", padx=10, pady=10)
    playGame()

def startPVBOT():
    global isBot
    isBot = True
    menu_frame.pack_forget()
    game_frame.pack(expand=True, fill="both", padx=10, pady=10)
    playGame()

def backMenu():
    game_frame.pack_forget()
    menu_frame.pack(pady=50)

# gui
window = tkinter.Tk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)
window.configure(background=colorGray)

# menu gui
menu_frame = tkinter.Frame(window, background=colorGray)
menu_frame.pack(expand=True, fill="both")

title_label = tkinter.Label(menu_frame, text="TIC-TAC-TOE", font=("Arial", 30, "bold"), 
                            bg=colorGray, fg="white")
title_label.pack(pady=(50, 20))

# pvp button
btn_pvp = tkinter.Button(menu_frame, text="Player vs Player", font=("Arial", 15), 
                         width=20, command=startPVP)
btn_pvp.pack(pady=10)

btn_pvp.bind("<Enter>", lambda e: e.widget.config(background=colorLGray))
btn_pvp.bind("<Leave>", lambda e: e.widget.config(background="white"))

# pvbot button
btn_pve = tkinter.Button(menu_frame, text="Player vs Bot", font=("Arial", 15), 
                         width=20, command=startPVBOT)
btn_pve.pack(pady=10)

btn_pve.bind("<Enter>", lambda e: e.widget.config(background=colorLGray))
btn_pve.bind("<Leave>", lambda e: e.widget.config(background="white"))

# game gui
game_frame = tkinter.Frame(window, background=colorGray)

label = tkinter.Label(game_frame, text=f"{currPlayer}'s turn", font=("Arial", 20), 
                      background=colorGray, foreground="white")
label.grid(row=0, column=0, columnspan=3, pady=(0, 5))

# scoreboard
score_label = tkinter.Label(game_frame, text=f"X: {scoreX}   |   O: {scoreO}   |   Ties: {scoreTies}", 
                            font=("Courier", 12), background=colorGray, foreground="white")

score_label.grid(row=1, column=0, columnspan=3, pady=5)

for row in range(3):
    for column in range(3):
        btn = tkinter.Button(game_frame, text="", font=("Arial", 50, "bold"),
                             background=colorGray, foreground=colorBlue, width=4, height=1,
                             command=lambda row=row, column=column: set_tile(row, column))
        
        btn.grid(row=row+2, column=column, padx=2, pady=2)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        board[row][column] = btn

button_restart = tkinter.Button(game_frame, text="Restart", font=("Arial", 20), background=colorGray,
                        foreground="white", command=playGame)
button_restart.grid(row=5, column=0, columnspan=2, sticky="we", pady=10)

menu_btn = tkinter.Button(game_frame, text="Menu", font=("Arial", 15), 
                          background=colorGray, foreground="white", 
                          width=10, command=backMenu)
menu_btn.grid(row=5, column=2, sticky="e", padx=10, pady=10)

# hover effect for restart too
button_restart.bind("<Enter>", lambda e: button_restart.config(background=colorLGray))
button_restart.bind("<Leave>", lambda e: button_restart.config(background=colorGray))

# center gui
window.update()
windowWidth = 555
windowHeight = 600
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
windowX = int((screenWidth/2) - (windowWidth/2))
windowY = int((screenHeight/2) - (windowHeight/2))
window.geometry(f"{windowWidth}x{windowHeight}+{windowX}+{windowY}")

window.mainloop()