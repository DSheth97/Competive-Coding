n=int(input())
for i in range(n):
    s=input()
    ls=s.split(' ')
    r=int(input())
    x1=int(ls[0])
    y1=int(ls[1])
    x2=int(ls[2])
    y2=int(ls[3])
    d1=(((x1**2)+(y1**2))**.5)
    d2=(((x2**2)+(y2**2))**.5)
    '''if d1>r and d2>r:
        print("SAFE")
    elif d1<r and d2>r or d1>r and d2<r:
        print("JUST MISSED")
    else:
        print("REPLANNING")'''
    m=(y2-y1)/(x2-x1)
    c=y1-(m*x1)
    if((r**2)*((m**2)+1)==c**2):
        print("JUST MISSED")
    else:
        if d1>r and d2>r and d1+d2>r:
            print("SAFE")
        else:
            print("REPLANNING")
