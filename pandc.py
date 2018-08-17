import itertools

dice = [2,3]

'''def subsets(n,m):

     perms = itertools.permutations(dice,n)
     for i in perms:
         if sum(i) == m:
             yield perms'''

def subsets(n,m,p):
     s=0
     perms = itertools.permutations(dice,n)
     for i in perms:
         if sum(i) == m:
             yield i
             two=i.count(2)
             thr=i.count(3)
             #print(two,thr)
             s1=(p/100)**two
             s2=(1-(p/100))**thr
             #print("s1,s2=",s1,s2)
             s=s+s1*s2
     if(s!=0):   
         print("%.6f"%s)   


for k in range(10):
    list(subsets(k,5,20))
