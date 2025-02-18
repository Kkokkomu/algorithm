import sys

input = sys.stdin.readline

board = []
for _ in range(3):
    board.append(list(map(int, input().split())))

blank = []
c1 = 0
c2 = 0
for i in range(3):
    for j in range(3):
        if board[i][j] == 1:
            c1+=1
        elif board[i][j] ==  2:
            c2+=1
        else:
            blank.append((i,j))

def chk(turn):
    ene = 1 if turn==2 else 1

    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) or (board[0][i] == board[1][i] == board[2][i]):
            return True
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return True

def dfs(cur):
    ene = 1 if cur==2 else 1

    mn = 2
    if chk(cur):
        return -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = cur
                mn = min(mn, dfs(ene))
                board[i][j] = 0
    if mn == 1:
        return -1
    elif mn == 2 or mn == 0:
        return 0
    else:
        return 1

if c1 == c2:
    me = 1
else:
    me = 2

if not blank:
    print('D')
else:
    answer = dfs(me)
    if answer == 1:
        print('W')
    elif answer == 0:
        print('D')
    else:
        print('L')