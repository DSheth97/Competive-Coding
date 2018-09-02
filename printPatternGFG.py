def printPat1(n):
    t=n
    while(t>0):
        for i in range(n,0,-1):
            for j in range(t):
                print(str(i),end=' ')
        print("$",end='')
        t=t-1

printPat1(3)

'''def printPat(n):
    for i in range(n,0,-1):
        for j in range()'''
