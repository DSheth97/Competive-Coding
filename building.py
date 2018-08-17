'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
'''def fun(ls):
    s=0
    print(ls)
    if(ls[0]>ls[1]):
        s=s+1
        print(s)
    if(ls[len(ls)-1]<ls[len(ls)-2]):
        s=s+1
        print(s)
    for i in range(1,len(ls)-1):
        if ls[i]>ls[i-1] and ls[i]<ls[i+1]:
            s=s+2
            print(s)
    print(s)'''
    
    
    
def fun2(ls,l):
    c=0
    s=0
    for i in range(1,l-1):
        c=0
        for j in range(0,l):
            #print("For : ",ls[i])
            if(ls[i]<ls[j]):
                c=c+1
                #print("c increased to",c)
                #print("i<j",c)
                
            if(i==j):
                left=c
                #print("left=",left)
                c=0
        right=c
        #print("right=",right)
        s=s+min(left,right)
        #print(min(left,right))
    print(s)


t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    ls=s.split(' ')
    l=[int(j) for j in ls]
    #print(l)
    fun2(l,n)
