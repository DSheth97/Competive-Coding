maxi=0
a=list()

def process(line):
    global maxi
    global a
    lst=line.split(',')
    s=lst[3]
    s=s[:len(s)-1:]
    q=float(s)
    
    if(q>maxi):
        maxi=q
        del a[:]
        a.append(lst[0])
        a.append(lst[1])
        a.append(lst[2])
        a.append(lst[3])
        print(maxi)
    elif(q==maxi):
        a.append(lst[0])
        a.append(lst[1])
        a.append(lst[2])
        a.append(lst[3])
        print(maxi)


with open ("C:/Users/admin/Desktop/3D_spatial_network.txt") as f:
    for line in f:
        process(line)
    print(a)
f.close()
