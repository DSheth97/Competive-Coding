s= input("enter string")
#a=s.split("")
a=[i for i in s]
r=zip(a,a)
print(list(r))
m="".join(list(r))
print(m)
