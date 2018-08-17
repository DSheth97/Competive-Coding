import math
n=int(input())

lst=[]
for i in range(n):
    lst.append(int(input()))

for j in lst:
    print(math.factorial(j))
