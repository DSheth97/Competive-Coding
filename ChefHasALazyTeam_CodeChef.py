t=int(input())
for i in range(t):
    z=input().split(' ')
    n=int(z[0])
    r=int(z[1])
    x=input().split(' ')
    c=0
    for j in x:
        if int(j)<=r:
            c=c+1
    print(n,c,c)
