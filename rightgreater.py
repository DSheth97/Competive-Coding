n=int(input())
x=input().split(' ')
l=len(x)
lst=list()
m=int(x[l-1])
for i in range(l-1,-1,-1):
    if(int(x[i])>=m):
        lst.append(int(x[i]))
        m=int(x[i])

for i in range(len(lst)-1,-1,-1):
    print(int(lst[i]))
