# Python program to find minimum possible 
# time by the car chassis to complete
 
def carAssembly (a, t):
     
    NUM_STATION = len(a[0])
    T1 = [0 for i in range(NUM_STATION)]
    T2 = [0 for i in range(NUM_STATION)]
    #print("a[0][0]",a[0][0])
    #print("a[1][0]",a[1][0])
    T1[0] = a[0][0] # time taken to leave
                           # first station in line 1
    T2[0] = a[1][0] # time taken to leave
                           # first station in line 2
 
    # Fill tables T1[] and T2[] using
    # above given recursive relations
    for i in range(1, NUM_STATION):
        '''print("T1[i]",T1[i])
        print("T2[i]",T2[i])
        print(T1[i-1] + a[0][i])
        print(t)
        print(t[1][i-1])'''
        T1[i] = min(T1[i-1] + a[0][i],
                    T2[i-1] + t[1][i-1] + a[0][i])
        T2[i] = min(T2[i-1] + a[1][i],
                    T1[i-1] + t[0][i-1] + a[1][i] )
 
    # consider exit times and return minimum
    return min(T1[NUM_STATION - 1],
               T2[NUM_STATION - 1])

n=int(input())
for i in range(n):
    l=int(input())
    tr1=[int(x) for x in input().split()]
    tr2=[int(x) for x in input().split()]
    c1=[int(x) for x in input().split()]
    c2=[int(x) for x in input().split()]
    a=[tr1,tr2]
    #print(a)
    t=[c1,c2]
    print(carAssembly(a, t))
    
    
