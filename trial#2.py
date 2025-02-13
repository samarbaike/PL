n=0
back=int(input())
front=int(input())
while True:
    if back<front:
        n+=1
    m=int(input())
    back, front=front, m
    if m==0:
        break

print(n)