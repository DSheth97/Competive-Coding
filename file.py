'''f=open("sample.txt","w+")
f.write("Hello world\n")
f.write("Dhruvil here\n")
f.write("ICT 16")
print(f.readline())
f.close
'''
with open("sample.txt") as f:
    data=f.readlines()
    print(data)

'''

s=input()
ls=s.split('#')
ls=[float(i) for i in ls]
print(sum(ls))
'''
