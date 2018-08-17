'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

n=input()
ls=n.split(' ')
t=int(input())
k=input()
ok=k.split(' ')
ok=[int(j) for j in ok]
key=int(ls[0])
lock=int(ls[1])
c=0



#tk=keys.split(' ')
tk=[key for i in range(t)]
print(tk)



def fun(ok,tk,lock,t):
    global c
    if(min(tk)>lock):
        return -1
    elif c>0:
        return c
    for i in range(t):
        for j in range(t):
            print("tk[i] ",tk[i],end=' ')
            print("ok[j] ",ok[j],end=' ')
            print("lock = ",lock)
            print(tk)
            print(ok)
            if(tk[i]*ok[j]==lock):
                print(c)
                break
            break
    #print(i)
    if(i+1>=t):
        #print(tk)
        #print(ok)
        for k in range(len(ok)):
            tk[k]=ok[k]*tk[k]
        c=c+1
        fun(ok,tk,lock,t)
        











'''def cal(ok,tk,lock):
    global c
    if(min(tk)>lock):
        return -1
    else:
        print(tk)
        for i in range(len(ok)):
            f
            if(ok[i]*tk[i]==lock):
                c=c+1
                break
        if(i>=len(ok)):
            for k in range(len(ok)):
                tk[k]=o[k]*tk[k]
            cal(ok,key,lock) '''   


z=fun(ok,tk,lock,t)
if(z==-1):
    print(z)
print(c)

            
                
    
        
