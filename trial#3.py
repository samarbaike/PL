def sink_whole_ship(x, y, back, front):
    if back[x+1][y]=='O' and back[x+2][y]==' ':
        back[x+1][y]=front[x+1][y]='●'
        back[x][y]=front[x+1][y]='●'
        return back, front
    elif back[x-1][y]=='O'and back[x-2][y]==' ':
        back[x-1][y]=front[x-1][y]='●'
        back[x][y]=front[x][y]='●'
        return back, front
    elif back[x][y+1]=='O' and back[x][y+2]==' ':
        back[x][y+1]=front[x][y+1]='●'
        back[x][y]=front[x+1][y]='●'
        return back, front
    elif back[x][y-1]=='O'and back[x][y-2]==' ':
        back[x][y-1]=front[x][y-1]='●'
        back[x][y]=front[x][y]='●'
        return back, front