'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
fav=[]
ang=[]
for i in range(t):
    n=int(input())
    for j in range (n):
        s=input()
        ls=s.split(' ')
        fav.append(int(ls[0]))
        ang.append(int(ls[1]))
    
    '''print(fav)
    print(ang)
    m1=max(fav)
    #print(m1)
    k1=fav.index(m1)
    fav[k1]=0
    m2=max(fav)
    #print(m2)
    k2=fav.index(m2)
    summ=-sum(ang)+ang[k1]+ang[k2]+m1+m2
    print(summ)'''
    ma=0
    j=0
    for i in range(n):
        for j in range(i+1,n):
            f=fav[i]+fav[j]
            print("fav[i]=",fav[i],end=' ')
            print("fav[j]=",fav[j],end=' ')
            print("f=",f)
            a=-sum(ang)+ang[i]+ang[j]
            print("a=",a)
            l=f+a
            print("l=",l)
            if(l>ma):
                ma=l
    
    print(ma)
