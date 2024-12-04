def find_max(list):
    max_number=list[0][0]
    for i in range(len(list)):
        if list[i][0] >= max_number:
            max_number=list[i][0]
            max_player=list[i]
    return max_player

leaderboard=[(13, 'samar'), (34, 'muhammed'), (43, 'baiaman')]
l=[]
print('Leaderboard:')
for i in range(len(leaderboard)):
    n=find_max(leaderboard)
    l.append(n)
    leaderboard.remove(n)
for row in l:
    print(' '.join(str(item) for item in row))