def findsum(A):
    ctr=1
    s=0
    for i in A:
        if i=='S':
            s=s+ctr
        elif i=='C':
            ctr=ctr*2
    return s



def checkcombo(A):
    x=A.find('C')
    if(x==-1):
        return 0
    else:
        A=A[::-1]
        y=A.replace('SC','CS',1)
        y=y[::-1]
        #print(y," inside replace")
        return y



g=0     
def check(D,A):
    global g
    x=findsum(A)
    #print(x)
    if D>=x:
        #print("g in D>=x is : ",g)
        return g
    else:
        if checkcombo(A)==0:
            return -1
        else:
            z=checkcombo(A)
            #print("z= ",z)
            g=g+1
            #print("g= ",g)
            return check(D,z)

def main():
    n=int(input())
    k=1
    for i in range(n):
        #D=int(input())
        A=str(input())
        pos=A.index(' ')
        D=int(A[:pos])
        A=A[(pos+1):]
        #print("D = ",D)
        #print("A = ",A)
        print("Case #",end="")
        print(k,end="")
        print(": ",end="")
        k=k+1
        global g
        g=0
        y=check(D,A)
        if(y==-1):
            print("IMPOSSIBLE")
        else:
            print(y)
            
    

main()
