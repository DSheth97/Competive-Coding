import itertools
s=input().split(' ')
n=int(s[0])
i=int(s[1])
m=int(s[2])
ls=input().split(' ')
ls=[int(j) for j in ls]
perms = itertools.permutations(ls,m)
c=0
for k in perms:
    flag=0
    #print(k)
    for x in range(m-1):
        '''print("x,k[x]",x,k[x])
        print("x,k[x+1]",x,k[x+1])
        print("x,k[x]+1",x,k[x]+1)
        print("k[x]>k[x+1]",k[x]>k[x+1])
        print("(k[x]+1)!=k[x+1])",(k[x]+1)!=k[x+1])'''
        if(k[x]>k[x+1] or ((k[x]+1)!=k[x+1]) or k[x]>=i):
            flag=1
            #print("FLAG =",flag)
    if(flag==0):
        c=c+1
        #print(c)
print(c)
