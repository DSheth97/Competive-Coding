def check(n):
    print(n)
    r=n%10
    s=0
    n=n//10
    while(n>9):
        rem=n%10
        print("rem=",rem,end='')
        s=s+rem
        print("s=",s)
        n=n//10
        print(n)
    print(n,"+",r,"=",n+r)
    print("s= ",s)
    if((n+r)==(s)):
        print("YES")
    else:
        print("NO")

#check(12345)
check(10021)
