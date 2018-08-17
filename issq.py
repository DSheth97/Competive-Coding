n=input("No. ?")
flag=0
for i in range(10**5):
    z=i*i
    if(z==int(n)):
        flag=1
        break
if flag==1:
    print("YES")
else:
    print("NO")
