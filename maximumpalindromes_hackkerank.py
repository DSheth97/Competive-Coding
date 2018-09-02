from itertools import permutations
from itertools import combinations_with_replacement
def Permut(lst,n):
    perm=permutations(lst,n)
    c=0
    t=""
    m=""
    for i in list(perm):
        #print(i)
        s=i[::-1]
        if(i==s):
            #print(m)
            t=""
            for j in i:
                t=t+j
            if(t not in m):
                c=c+1
                m=m+t+" "
                print(m,c)
    return c


s=input()
q=int(input())
for z in range(q):
    lr=input().split(" ")
    l=int(lr[0])
    r=int(lr[1])
    lst=list()
    st=s[l-1:r:]
    for i in st:
        lst.append(i)
    x=len(s)
    for j in range(x,0,-1):
        c=Permut(lst,j)
        if(c!=0):
            break
    print(c)
