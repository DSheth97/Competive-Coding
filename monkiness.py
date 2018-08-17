n=int(input())
for k in range(n):
    l=int(input())
    a1=input()
    b1=input()
    m=0
    a=a1.split(' ')
    b=b1.split(' ')
    a=[int(p) for p in a]
    b=[int(p) for p in b]
    for j in range(l-1,-1,-1):
        for i in range(l):
            if(j>=i and b[j]>=a[i] and m<j-i):
                m=j-i
                #print(m)
                break
    print(m)
        
