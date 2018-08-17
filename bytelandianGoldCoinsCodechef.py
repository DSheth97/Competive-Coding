def result(t):
    '''if(a==0 and b==0 and c==0):
        return 0'''
    a=t//2
    b=t//3
    c=t//4
    s=a+b+c
    print(a,b,c,s,t)
    if(a==0 and b==0 and c==0):
        return 0
    if(t>=s):
        return(t)
    else:
        return (result(a)+result(b)+result(c))
    #print(a,b,c,s,t)

inputs=[]
c=0
while True:
    if(c==10):
        break
    inp=input()
    if(inp=="" or int(inp)>1000000000 or int(inp)<0):
        break
    inputs.append(int(inp))
    c=c+1

for i in inputs:
    p=result(i)
    if(p>i):
        print(p)
    else:
        print(i)
