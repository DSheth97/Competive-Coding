#import gmpy
import math
'''n=int(input())
s=input()
lst=s.split(' ')
st=10**(n-1)
en=10**n
for i in range(m-1):'''
n = int(input().strip())
known = list(map(int,input().strip().split(' ')))
print(known)
'''
digits = n+(n-1)
for i in range(32,100000000):
    sq = str(pow(i,2))
    if(len(sq)<digits):
        continue
    if(len(sq)>digits):
        break
    found = []     
    for j in range(0,len(sq),2):
        found.append(int(sq[j]))
    if(known==found):
        print(i)
        break'''
st=int(10**(n-2))
print(st)
en=int((10**(n-1)))
print(en)
found=[]
temp=0
for j in range(0,(n*2)-1):
        if(j%2==0):
            found.append(known[temp])
            temp=temp+1
        else:
            found.append('a')
print(found)
for i in range(st,en):
    k=[int(t) for t in str(i)]
    #print(k)
    q=0
    for m in range(1,(n*2)-1,2):
        found[m]=k[q]
        q=q+1
    #print(found)
    #found=map(str,found)
    #num=''.join(found)
    #num=int(num)
    found=[str(z) for z in found]
    num=int(''.join(found))
    print(num)
    if(math.sqrt(num).is_integer()==True):
        print(int(math.sqrt(num)))
        break
