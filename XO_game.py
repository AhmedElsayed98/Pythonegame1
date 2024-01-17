#X-O Game
from guizero import App, Box, Text, PushButton

def clear_board():
    new_board = [[None,None,None],[None,None,None],[None,None,None]]

    for x in range(3):
        for y in range(3):
            button = PushButton(
                board, text="", grid=[x, y], width=3, command=choose_square, args=[x,y]
            )
            new_board[x][y] = button
    return new_board
def choose_square(x,y):
    board_squares[x][y].text = turn
    board_squares[x][y].disable()
    toggle_player()
    check_win()

def toggle_player():
   global turn
   print(turn)
   if turn == "X":
       turn = "O"
   else:
       turn = "X"
   text1 = 'it is your turn ' + turn
   turn_msg.value = text1

def moves_taken():
    moves = 0
    for row in board_squares:
        for col in row:
            if col.text == "X" or col.text == "O":
                moves = moves + 1
    return moves
def check_win():
    winner = None

    #Vertical check
    if(
        board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text
    ) and board_squares[0][0].text in ["X", "O"]:
        winner = board_squares[0][0].text
    if (
            board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text
    ) and board_squares[1][0].text in ["X", "O"]:
        winner = board_squares[1][0].text
    if (
            board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text
    ) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[2][0].text
    #Horizontal check
    if(
        board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text
    ) and board_squares[0][0].text in ["X", "O"]:
        winner = board_squares[0][0].text
    if (
            board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text
    ) and board_squares[0][1].text in ["X", "O"]:
        winner = board_squares[0][1].text
    if (
            board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text
    ) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][2].text
    #Diagonal_check
    if (
            board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text
    ) and board_squares[0][0].text in ["X", "O"]:
        winner = board_squares[0][0].text
    if (
            board_squares[0][2].text == board_squares[1][1].text == board_squares[2][0].text
    ) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][2].text
    if winner is not None:
        message.value = winner + "Wins !"
        reset_button.enable()
    elif moves_taken() == 9:
        message.value = 'Draw !'
        reset_button.enable()

def reset():
    global turn
    global board_squares
    board_squares = clear_board()

turn = 'X'
app = App('XO Game')
board = Box(app, layout="grid")
app.title = "Game on"
text1 = 'it is your turn '+ turn
turn_msg = Text(app, text = text1)
reset_button = PushButton(app, text="reset", width=5, command=reset)
reset_button.disable()
for x in range(3):
    for y in range(3):
        button = PushButton(
            board, text="", grid=[x,y], width=3
        )
board_squares = clear_board()

print(board_squares)
message = Text(app, text="by Ahmed Sayed (Zecka)")
app.display()
