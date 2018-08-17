def main():
    n=int(input())
    for i in range(n):
        ls=[]
        st=input()
        ls=st.split(' ')
        ls=[int(i) for i in ls]
        X=ls[0]
        Y=ls[1]
        nth=ls[2]
        lst=[]
        l=[]
        z=0
        for j in range(nth):
            if(j<X):
                lst.append(Y)
            else:
                z=0
                for k in range(X):
                #print("lst[",j-1,"]",lst[j-1])
                    z=z+lst[j-1]
                    j=j-1
                #print("z= ",z)
                lst.append(z)
        print(lst[nth-1])
        
main()
'''for p in range(k):
            l.append(lst[p])
            print(l)
        lst[X]=sum(lst)-sum(l)'''
