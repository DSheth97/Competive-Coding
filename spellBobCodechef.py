t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    b1=0
    b2=b3=o1=o2=o3=0
    l1=s1[0]+s2[0]
    l2=s1[1]+s2[1]
    l3=s1[2]+s2[2]
    if 'b' in l1:
        b1=b1+1
    if 'o' in l1:
        o1=o1+1
    if 'b' in l2:
        b2=b2+1
    if 'o' in l2:
        o2=o2+1
    if 'b' in l3:
        b3=b3+1
    if 'o' in l3:
        o3=o3+1
    if(b1+b2+o3==3 or b1+o2+b3==3 or o1+b2+b3==3):
        print('yes')
    else:
        print('no')
