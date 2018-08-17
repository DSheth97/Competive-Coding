def sq(x):
    return x*x
l=[[1,2,3],[4,5,6],[7,8,9]]
print(len(l))
for i in range(len(l)):
    result=map(sq,l[i])
    print(list(result))
    
