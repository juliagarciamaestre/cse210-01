#Tic Tac Toe
#By: Julia Garcia
def main():
    #Display initial board
    board_game= board()
    square_board(board_game)

    #
    current_player = player("")

    position = player_position(current_player)
    print(position)
    # choice = player_choice(board_game,position,current_player)
    # print(choice)
    # new_square_board(position,current_player)
    choice = new_board(position,board_game,current_player)
    current_board = square_board(choice)
    print(current_board)
    


def board():
    board = [1,2,3,4,5,6,7,8,9]
    return board

def new_board(new_position,board,player):
    if new_position == 0:
        board[0] = player
    if new_position == 1:
        board[1] = player
    if new_position == 2:
        board[2] = player
    if new_position == 3:
        board[3] = player
    if new_position == 4:
        board[4] = player
    if new_position == 5:
        board[5] = player
    if new_position == 6:
        board[6] = player
    if new_position == 7:
        board[7] = player
    if new_position == 8:
        board[8] = player
    if new_position == 9:
        board[9] = player
    return board
    


def square_board(board):
    print()
    print(f' |{board[0]}| |{board[1]}| |{board[2]}|')
    print(' .-. .-. .-.')
    print(f' |{board[3]}| |{board[4]}| |{board[5]}|')
    print(' .-. .-. .-.')
    print(f' |{board[6]}| |{board[7]}| |{board[8]}|')
    print()

def player(current):
    if current == "" or current == 'o':
        return 'x'
    elif current == 'x':
        return 'o'

def player_position(player):
    position = input(f'{player}Choose a square (1-9): ')
    position = int(position) - 1
    return position

# def player_choice(board,position,player):
#     choice = board[position]
#     current_player = player
#     choice = current_player
#     return choice

# def new_square_board(position,player):
#     board[position] = player
#     square_board(board)



if __name__ == "__main__":
    main()