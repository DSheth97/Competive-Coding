def Crossword(matrix,word):
    r=len(matrix)
    c=len(matrix[0])
    print(r,c)
    s=""
    flag=0
    for i in range(r):
        for j in range(c):
            #print(matrix[i][j])
            #print(i,j)
            s=s+matrix[i][j]
            print(s)

        if word in s:
            #print("ound")
            flag=1
            break
        else:
            s=""
    s=""
    if flag==0:
        for j in range(c):
            for i in range(r):
                #print(matrix[i][j])
                #print(j,i)
                s=s+matrix[i][j]
            print(s)
            if word in s:
                flag=1
                break
            else:
                s=""

    if flag==1:
        print("Found")
    else:
        print("Not Found")

m=[['a','b','c','d'],['e','f','g','h'],['i','j','k','l']]
print(m)
w='gk'
Crossword(m,w)
