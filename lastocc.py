'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
s=input()
c=input()
v=int(input())
p=s.rfind(c)
f=p+v-1

'''if(f>len(s)):
    if(s[l-1:l-1-v:-1].count(c)!=):
        
    else:
        print(len(s))
elif(p==-1):
    print(len(s))
else:
    print(f)
'''
ls=[i for i in s]
tmp=ls
print("temp ",tmp)
l=len(ls)
for j in range(l,v-1,-1):
    print("LIST before insertion",ls)
    print(s[l-1:l-1-v:-1])
    c1=ls[l-1:l-1-v:-1].count(c)
    print("C1 = ",c1)
    ls.insert(j,c)
    print("LIST after insertion",ls)
    c2=ls[l-1:l-1-v:-1].count(c)
    print("C2 =",c2)
    if(c2==c1+1 and c1!=0):
        print(j)
        break
    else:
        ls=tmp
        print(tmp)
