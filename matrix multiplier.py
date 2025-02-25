i = [int(s) for s in input().split()]
r1 = i[0]
c1 = i[1]
r2 = i[1]
c2 = i[2]

a = [[int(s) for s in input().split()] for _ in range(r1)]
b = [[int(s) for s in input().split()] for _ in range(r2)]
p = [[0 for _ in range(c2)] for _ in range(r1)] 

for i in  range(r1):
    for j in range(c2):
        for me in range(c1):
            p[i][j]+=a[i][me]*b[me][j]

    
print(' ')
for row in p:
    print(' '.join([str(i) for i in row]))
