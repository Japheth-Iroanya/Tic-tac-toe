########### This is a tic-tac-toe game also known as X and O in NIGERIA

#from IPython.display import clear_output
#import string

print('Welcome to the 2-player tic-tac-toe game. \n\nThis is the input guide: \
Please take a look at and use the number system shown here to guide your input \n\n')



#A dictionary that'll store the players' moves.
plays = {1:' ', 2:' ', 3:' ',4:' ',5:' ',6:' ', 7:' ',8:' ', 9:' '}

def reset_dict():
    global plays
    plays = {1:' ', 2:' ', 3:' ',4:' ',5:' ',6:' ', 7:' ',8:' ', 9:' '}


def show():
    
    #The initial layout for the keyboard and guide to the players so they understand the game's input system.
    layout = '   |   |   \n 7 | 8 | 9 \n   |   |   \n-----------\n   \
|   |   \n 4 | 5 | 6 \n   |   |   \n-----------\n   |   |   \n 1 | 2 | 3 \n   |   |   \n'

    
    gameDisplay = f'   |   |   \n {plays[7]} | {plays[8]} | {plays[9]} \n   |   |   \n-----------\n   \
|   |   \n {plays[4]} | {plays[5]} | {plays[6]} \n   |   |   \n-----------\n   |   |   \n \
{plays[1]} | {plays[2]} | {plays[3]} \n   |   |   \n'

    print(layout)
    print(gameDisplay)
show()

p1=''
p2 =''

while p1.upper() != 'X' or p1.upper() != 'O':
    p1 = (input('Player 1 please pick a side: \nX or O\n')).upper()

    if p1 == 'X':
        p2 = 'O'
        break
    elif p1 == 'O':
        p2 = 'X'
        break
                    
    else:
        print('You have not chosen a side!!!!!')
        
sides = {1 :p1, 2 :p2}        

########################################################################################        
def win(num):
    """
    DOCSTRING:
    This function will check if the game has been won everytime a player makes a move
        
    """
    val = False
    combinations = {1:[[4,7],[5,9],[2,3]],       #All these are the winning combinations
                    2: [[1,3],[5,8]],           #i.e all combinations that form a straight line.
                    3: [[6,9],[5,7],[1,2]],
                    4: [[1,7],[5,6]],
                    5: [[4,6],[1,9],[2,8],[3,7]],
                    6: [[3,9],[4,5]],
                    7: [[3,5],[8,9],[4,1]],
                    8: [[7,9],[2,5]],
                    9: [[7,8],[1,5],[3,6]]}
    for i in combinations[num]:
    
        if plays[num]== plays[i[0]] == plays[i[1]]:
            val = True
            break
    return val
#######################################################################################               
reply ='YES'
while reply.upper() == 'YES':
    reset_dict()
    player_arrangement =  [1,2,1,2,1,2,1,2,1]
    for player in player_arrangement:
        
        user_input = None
        try:
            user_input = int(input(f'Player {player}. Make you move!!!\n'))
        except (SyntaxError,ValueError,NameError):
            pass
       
                
        while not (user_input in plays.keys()):
            print('Invalid Move!')
        
            try:
                user_input = int(input(f'Player {player}. Make you move!!!\n'))
            except (SyntaxError,ValueError,NameError):
                continue
                
        else:
            while plays[user_input] != ' ':
                print('Invalid Move! This spot is already taken')
                user_input = int(input(f'Player {player}. Make you move!!!\n'))
                continue
               
        move = user_input
        
        plays[move] = sides[player]
        #clear_output()
        show()

        if win(move):
            print(f'CONGATULATIONS Player {player}, You\'ve won.')
            break

    else:
        print('Nobody Won!')
        
    reply = input('Do you want to play again? \nType yes to play again, anything else to end :\n')
