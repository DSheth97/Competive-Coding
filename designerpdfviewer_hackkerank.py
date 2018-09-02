lst=input().split(" ")
s=input()
m=0
for i in s:
    t=int(lst[(ord(i)-97)])
    if(m<t):
        m=t
print(m*len(s))
