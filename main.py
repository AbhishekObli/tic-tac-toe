# game board
board = ["-" for i in range (9)]

current_player = "x"
winner = None
game_Running = True

# print the board
def print_board(board):
	global game_Running
	print ("-------------")
	print ("|" , board [0] , "|" , board [1] , "|" , board [2] , "|")
	print ("-------------")
	print ("|" , board [3] , "|" , board [4] , "|" , board [5] , "|")
	print ("-------------")
	print ("|" , board [6] , "|" , board [7] , "|" , board [8] , "|")
	print ("-------------")

# get input from user
def user_Input(board):
	global game_Running
	user = int(input("Enter a number between 0-8: "))
	if (user>=0 and user<=8 and board[user]=="-"):
		board[user] = current_player
	else:
		print("Oops! another player has already conquered the place")
		return True

# check if input is a win
def check(board,player):
	global game_Running
	if board[0]==player and board[1]==player and board[2]==player:
		return True
	if board[3]==player and board[4]==player and board[5]==player:
		return True
	if board[6]==player and board[7]==player and board[8]==player:
		return True
	if board[0]==player and board[3]==player and board[6]==player:
		return True
	if board[1]==player and board[4]==player and board[7]==player:
		return True
	if board[2]==player and board[5]==player and board[8]==player:
		return True
	if board[0]==player and board[4]==player and board[8]==player:
		return True
	if board[2]==player and board[4]==player and board[6]==player:
		return True
	return False

# check is win
def iswin():
	if check (board, current_player):
		global game_Running
		print_board(board)
		print(f"The winner is {current_player}")
		game_Running = False

# check if input is a tie
def isdraw(board):
	global game_Running
	if ('-' not in board):
		print_board(board)
		print("It's a tie")
		return True

# switch with the players
def switch_player():
	global current_player
	if current_player == "x":
		current_player = "o"
	else:	
		current_player = "x"
	return current_player

# repeat until win or tie
while (game_Running):

	print_board (board)
	user_Input(board)
	iswin()
	isdraw(board)
	switch_player()

