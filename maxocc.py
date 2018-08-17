s=input()
ls=[x for x in s]
ls.sort()
m=0
#print(ls)
for i in range(len(ls)):
    c=ls.count(ls[i])
    '''print("c",c)
    print("m",m)
    print("ls[i]",ls[i])'''
    if(c>m):
        m=c
        v=ls[i]

print(v,m)
