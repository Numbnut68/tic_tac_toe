board_values = {
    0: '   ',
    1: '   ',
    2: '   ',
    3: '   ',
    4: '   ',
    5: '   ',
    6: '   ',
    7: '   ',
    8: '   ',
}


def print_board():
    board = (board_values[0] + '|' + board_values[1] + '|' + board_values[2] + '\n' +
             '---|---|---' + '\n' +
             board_values[3] + '|' + board_values[4] + '|' + board_values[5] + '\n' +
             '---|---|---' + '\n' +
             board_values[6] + '|' + board_values[7] + '|' + board_values[8])
    print(board)


example_board = ('(1)' + '|' + '(2)' + '|' + '(3)' + '\n' +
                 '---|---|---' + '\n' +
                 '(4)' + '|' + '(5)' + '|' + '(6)' + '\n' +
                 '---|---|---' + '\n' +
                 '(7)' + '|' + '(8)' + '|' + '(9)')

used_nums = []


def user_input(player_name):
    while True:
        inp = int(input(f'{player_name}, please enter a number between 1-9:  '))
        inp -= 1
        if 0 <= inp < 10:
            if inp in used_nums:
                print('This spot is already taken.')
                continue
            used_nums.append(inp)
            return inp
        print('Please Enter a number between 1-9')


def result(vals, p1, p2):
    if (vals[0] == vals[1] == vals[2] == ' X '
            or vals[1] == vals[4] == vals[7] == ' X '
            or vals[0] == vals[4] == vals[8] == ' X '
            or vals[2] == vals[5] == vals[8] == ' X '
            or vals[3] == vals[4] == vals[5] == ' X '
            or vals[2] == vals[4] == vals[6] == ' X '
            or vals[6] == vals[7] == vals[8] == ' X '
            or vals[0] == vals[3] == vals[6] == ' X '):
        print(f'\n\nCongratulations {p1}. You won the game!\n')
        quit()

    elif (vals[0] == vals[1] == vals[2] == ' O '
          or vals[1] == vals[4] == vals[7] == ' O '
          or vals[0] == vals[4] == vals[8] == ' O '
          or vals[2] == vals[5] == vals[8] == ' O '
          or vals[3] == vals[4] == vals[5] == ' O '
          or vals[2] == vals[4] == vals[6] == ' O '
          or vals[6] == vals[7] == vals[8] == ' O '
          or vals[0] == vals[3] == vals[6] == ' O '):
        print(f'\n\nCongratulations {p2}. You won the game!\n')
        quit()
   ''' else:
        print(f'Noone wins this time\n')
        quit()'''


def start_game():
    print("Hello and welcome to my tic tac toe game!")

    player_1 = input("Player 1, please enter your name: ")
    player_2 = input("Player 2, please enter your name: ")

    print(f'\nThis is what the game board looks like:\n{example_board}')

    print('\nTo play, the respective player needs to input\n'
          'the number relating to the block you would like\n'
          'to fill\n')

    print(f"{player_1} are you ready to start us off?")

    for n in range(0, 9):
        if n % 2 == 0:
            board_values[user_input(player_1)] = ' X '
        else:
            board_values[user_input(player_2)] = ' O '

        print_board()
        result(board_values, player_1, player_2)


start_game()
