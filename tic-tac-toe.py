from random import randint


def create_board(board):
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print('--+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+---+--')
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('')
    print('------------------------------------------------------------')
    print('')


def choose_letter():
    print('Which letter do you choose \'X\' or \'O\'')
    players_letter = input().upper()
    while players_letter not in ('O', 'X'):
        print('Letter must be \'X\' or \'O\'')
        players_letter = input().upper()
    if players_letter == 'X':
        computer_letter = 'O'
    else:
        computer_letter = 'X'
    return players_letter, computer_letter


def choose_first_player():
    # '1' means player goes first and vice versa.
    first_player = ''
    if randint(0,1) == 1:
        first_player = 'player'
    else:
        first_player = 'computer'
    return first_player


def winning_moves(bo, le):
    win = ((bo[6] == le and bo[7] == le and bo[8] == le) or
           (bo[3] == le and bo[4] == le and bo[5] == le) or
           (bo[0] == le and bo[1] == le and bo[2] == le) or # across the sides. right to left.
           (bo[0] == le and bo[3] == le and bo[6] == le) or
           (bo[1] == le and bo[4] == le and bo[7] == le) or
           (bo[2] == le and bo[5] == le and bo[8] == le) or # from top to bottom.
           (bo[0] == le and bo[4] == le and bo[8] == le) or
           (bo[2] == le and bo[4] == le and bo[6] == le) # across diagonals.
           )
    return win


def get_user_input():
    print("Play: ", end='')
    try:
        return int(input())
    except ValueError:
        print('input a number')
        return get_user_input()


def if_free(board, move):
    try:
        if board[move] == ' ':
            return True
        else:
            return False
    except IndexError:
        print('Input numbers between 0 - 8')



def get_computer_move(board):
    move = randint(0, 8)
    while board[move] != ' ':
        move = randint(0, 8)
    return move


def is_board_full(board):
    for move in range(0, 9):
        if if_free(board, move):
            return False
    return True


def has_won(board, letter):
    bo, le = board, letter
    if winning_moves(bo, le):
        return True


def play_again():
    print('Do you want to play again?')
    play_again = input().lower()
    if play_again == 'y':
        return True
    else:
        return False


def start_game():
    board = [' '] * 9
    player_letter, computer_letter = choose_letter()
    turn = choose_first_player()
    if turn == 'player':
        print('You go first')
    else:
        print('Computer goes first.')

    while True:
        create_board(board)

        if turn == 'player':
            player_move = get_user_input()
            while not (if_free(board, player_move)):
                print('Spot has been taken')
                player_move = get_user_input()

            board[player_move] = player_letter
            turn = 'computer'

        else:
            computer_move = get_computer_move(board)
            board[computer_move] = computer_letter
            has_won(board, computer_letter)
            turn = 'player'

        if has_won(board, player_letter):
            create_board(board)
            print(f'You have won.')
            if play_again():
                start_game()
            else:
                break
        elif has_won(board, computer_letter):
            create_board(board)
            print('Computer won')
            if play_again():
                start_game()
            else:
                break
        elif is_board_full(board):
            print('No one won')
            if play_again():
                start_game()
            else:
                break


start_game()



'''class Computer:
    def __init__(self):
        self.move = ''

    def plays_first(self):
        self.move = randint(1, 9)
        return self.move

    def plays(self, player_move, board):
        if player_move in [1, 3] and board[1] == '' and board[3] == '' and board[4] == '':
            self.move = 8
        elif player_move in [7, 9] and board[1] == '' and board[3] == '' and board[4] == '':
            self.move = 2
        elif player_move in [3, 9] and board[1] == '' and board[7] == '':
            self.move = 4
        elif '''


