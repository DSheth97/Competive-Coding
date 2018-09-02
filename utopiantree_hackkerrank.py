def utopianTree(n):
    c=1
    for i in range(n+1):
        if(i==0):
            c=1
        elif(i%2==0):
            c=c+1
        else:
            c=2*c
    return c

print(utopianTree(5))
print(utopianTree(0))
print(utopianTree(1))
print(utopianTree(4))
