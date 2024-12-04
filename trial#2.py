def user_board():
    f = [['~' for k in range(8)] for k in range(8)]
    for i in range(8):
        f[i][0]=str(chr(64+i))
        for j in range(8):
            f[0][0]=' '
            f[0][j]=str(j)
    return f

def game():
    front=user_board()
    for row in front:
        print(' '.join (row))
    return True

game()