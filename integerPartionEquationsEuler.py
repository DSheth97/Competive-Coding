import math
t=int(input())
for i in range(t):
    x=input().split(' ')
    a=int(x[0])
    b=int(x[1])
    y=a/b
    ck=0
    intsol=0
    for k in range(1,10000000):
        f=math.sqrt(1+(4*k))
        if(f.is_integer()==False):
            continue
        s1=(1+f)/2
        s2=(1-f)/2
        if(s1>0):
            ck=ck+1
            if(((math.log2(s1)).is_integer())==True):
                intsol=intsol+1
        if(s2>0):
            ck=ck+1
            if(((math.log2(s1)).is_integer())==True):
                intsol=intsol+1
        if(intsol/ck<y):
            print(k)
            break
