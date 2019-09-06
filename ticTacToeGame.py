player=0
boardPos=None
ticTacBoard={1:'  ',2:'  ',3:'  ',4:'  ',5:'  ',6:'  ',7:'  ',8:'  ',9:'  '}

def printBoard(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('--+--+--')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('--+--+--')
    print(board[7]+'|'+board[8]+'|'+board[9])

def winnerDecide(a):
    if a[1]==a[2] and a[2]==a[3] and a[1]=='X':
        return 1
    elif a[4]==a[5] and a[5]==a[6] and a[4]=='X':
        return 1
    elif a[6]==a[7] and a[7]==a[8] and a[7]=='X':
        return 1
    elif a[1]==a[4] and a[4]==a[7] and a[7]=='X':
        return 1
    elif a[2]==a[5] and a[5]==a[8] and a[2]=='X':
        return 1
    elif a[3]==a[6] and a[6]==a[9] and a[3]=='X':
        return 1
    elif a[1]==a[5] and a[5]==a[9] and a[1]=='X':
        return 1
    elif a[3]==a[5] and a[5]==a[7] and a[3]=='X':
        return 1
    elif a[1]==a[2] and a[2]==a[3] and a[1]=='O':
        return 0
    elif a[4]==a[5] and a[5]==a[6] and a[4]=='O':
        return 0
    elif a[6]==a[7] and a[7]==a[8] and a[7]=='O':
        return 0
    elif a[1]==a[4] and a[4]==a[7] and a[7]=='O':
        return 0
    elif a[2]==a[5] and a[5]==a[8] and a[2]=='O':
        return 0
    elif a[3]==a[6] and a[6]==a[9] and a[3]=='O':
        return 0
    elif a[1]==a[5] and a[5]==a[9] and a[1]=='O':
        return 0
    elif a[3]==a[5] and a[5]==a[7] and a[3]=='O':
        return 0

print('this is your Tic Tac Game board')
printBoard(ticTacBoard)

for chance in range(1,10):
    if player==0:
        boardPos=int(input('player one, enter where you want to do your move'))
        ticTacBoard[boardPos]='X'
        player=1
    elif player==1:
        boardPos=int(input('player two, enter where you want to do your move'))
        ticTacBoard[boardPos]='O'
        player=0
    printBoard(ticTacBoard)
    if winnerDecide(ticTacBoard)==0:
        print('player two is the winner')
        break
    if winnerDecide(ticTacBoard)==1:
        print('player one is the winner')
        break

if not winnerDecide(ticTacBoard)==1 or winnerDecide(ticTacBoard)==0:
     print("it's a Draw")
