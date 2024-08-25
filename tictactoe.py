import random
# So this is going to be a simple tic tac toe game
num = int(input('tell us the board size : '))

user_symbol=str(input('''Pick your symbol 'O' or 'X' :  ''')).upper()
if user_symbol == 'O':
    comp_symbol = 'X'
else:
    comp_symbol = 'O'

# num_list = list(range(num*num))
# def board(num_list):
#     for ind, i in enumerate(num_list):
#         print(i,end=' ')
#         if (ind+1)%num == 0:
#             print('')
num_list=list('*' for _ in range(num*num))

def board(num_list):
    for ind, i in enumerate(num_list):
        print(i,end='|')
        if (ind+1)%num == 0:
            print('')
def user():
    move = int(input('Please tell us your move :  '))
    if num_list[move] != 'O' and num_list[move]!='X':
        num_list[move] = user_symbol
    else:
        print('please use valid id')
        user()
def computer():
    comp_move = random.randrange(0,num*num)
    if num_list[comp_move] != 'O' and num_list[comp_move]!='X':
        num_list[comp_move]= comp_symbol
    else:
        computer()

def check_win(player_symbol):
    for i in range(num):
        # for j in range(num):
        if all(num_list[i*num+j]==player_symbol for j in range(num)) or \
            all(num_list[j*num+i]==player_symbol for j in range(num)):
            return True
    if all(num_list[i*num+i] == player_symbol for i in range(num)) or\
          all(num_list[(num-1-i)*num+i]==player_symbol for i in range(num)):
           return True

    return False

def check_draw(player_symbol,comp_symbol):
    return all(num_list[i]==player_symbol or \
               num_list[i]==comp_symbol for i in range(len(num_list)))


def playgame():
    game=True
    while game:
        board(num_list)
        user()
        if check_win(user_symbol):
            board(num_list)
            print('You have won the game')
            game = False
            break
        if check_draw(user_symbol,user_symbol):
            print(f' Nice Try but its a draw \n Better luck next time')
            board(num_list)
            break
        computer()
        if check_win(comp_symbol):
            board(num_list)
            print('You Lose')
            game=False
            break
        if check_draw(user_symbol,user_symbol):
            board(num_list)
            print(f' Nice Try but its a draw \n Better luck next time')

            break

playgame()
        