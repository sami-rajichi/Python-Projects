nb_list = list(map(str , range(1 , 10)))
ttt_board = ['-']*len(nb_list)

def draw_board(arr):
    print("\t\t   Tic-tac-toe")
    for i in range(0 , len(arr) , 3):
        print('\t\t~~~~~~~~~~~~~~~~~')
        print('\t\t', end='')
        for j in range(i , i + 3):
            print("|| " + arr[j] + " " , end='')
        print("||")
    print('\t\t~~~~~~~~~~~~~~~~~\n')

draw_board(nb_list)
draw_board(ttt_board)

player_O = 'O'
player_X = 'X'
def get_user_input(arr , player):
    userInput = input(player + " : where would you like to place your piece (1 - 9) : ")
    while True:

        if userInput in list(map(str , range(1 , 10))):
            if arr[int(userInput) - 1] != '-':
                print("This spot has already been chosen .. Try again.")
                userInput = input(player + " : where would you like to place your piece (1 - 9) : ")
            else:
                break
        else:
            print("This is not a spot on the board .. Try again.")
            userInput = input(player + " : where would you like to place your piece (1 - 9) : ")
    return  userInput

def char_place(arr , player , pp):
    arr[int(pp) - 1] = player

def theWinner(arr , player):
    for i in range(0 , len(arr) , 3):
        if arr[i] == arr[i+1] == arr[i+2] == player:
            return True
            break
    for i in range(3):
        if arr[i] == arr[i+3] == arr[i+6] == player:
            return True
            break
    return ((arr[0] == arr[4] == arr[8] == player) or (arr[2] == arr[4] == arr[6] == player))

def emptying_the_board(arr):
    for i in range(len(arr)):
        arr[i] = '-'

while True:
    while True:
        piece_position = get_user_input(ttt_board, player_X)
        char_place(ttt_board , player_X , piece_position)
        draw_board(nb_list)
        draw_board(ttt_board)
        if theWinner(ttt_board , player_X) == True:
            print("\nCongratulations! Player X wins the game.")
            break
        elif '-' not in ttt_board:
            print("\nIt's a tie that resolved the matter!")
            break
        piece_position = get_user_input(ttt_board, player_O)
        char_place(ttt_board, player_O, piece_position)
        draw_board(nb_list)
        draw_board(ttt_board)
        if theWinner(ttt_board , player_O) == True:
            print("\nCongratulations! Player O wins the game.")
            break
    emptying_the_board(ttt_board)
    rep = input("\nWould you like to play again (y/n) : ").lower().strip()
    if rep.startswith('n'):
        print("\nI hope you enjoyed the game .. Goodbye.")
        break
    else:
        draw_board(nb_list)
        draw_board(ttt_board)