s=str(input())
l=len(s)
t=s[l//2:l]+s[0:l//2]
print(t)
x=(l-1)*2
for i in range(0,l):
    print(" "*(x),end="")
    print(t[0:i+1],end="")
    print("$",end="")
    x=x-2;
print()
