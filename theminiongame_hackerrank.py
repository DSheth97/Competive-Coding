import re
def minion_game(string):
    kevin=0
    stuart=0
    vowels="AEIOU"
    l=len(string)
    for i in range(l):
        if string[i] in vowels:
            kevin=kevin+l-i
        else:
            stuart=stuart+l-i
                #prog=re.compile(s)
                #result=prog.findall(string)
                #print("Kevin",kevin)
                #print("Kevin",kevin)
    if(kevin>stuart):
        print("Kevin",kevin)
    elif(kevin<stuart):
        print("Stuart",stuart)
    else:
        print("Draw")
        
minion_game("BANAASA")
'''s="BANANA"
vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if(kevsc > stusc):
    print("Kevin", kevsc)
elif (kevsc < stusc):
    print("Stuart", stusc)
else:
    print("Draw")
'''
