Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=3.0
>>> type(x)
<class 'float'>
>>> y=x
>>> z=3
>>> type(y)
<class 'float'>
>>> type(z)
<class 'int'>
>>> x.is_integer()
True
>>> x.is_integer
<built-in method is_integer of float object at 0x05D51F00>
>>> x.is_integer()
True
>>> x.as_integer_ratio()
(3, 1)
>>> x=5.6
>>> x.is_integer()
False
>>> y=x
>>> 
>>> y.as_integer_ratio()
(3152519739159347, 562949953421312)
>>> y.is_integer()
False
>>> x=4.000
>>> x.is_integer()
True
>>> x=True
>>> type(x)
<class 'bool'>
>>> x=None
>>> type(x)
<class 'NoneType'>
>>> x="PDPU"
>>> type(x)
<class 'str'>
>>> x="pdpu hello world"
>>> x.capitalize()
'Pdpu hello world'
>>> a="the quick brown fox jump over the wall"
>>> a.count("the")
2
>>> a.count("e")
3
>>> x.upper()
'PDPU HELLO WORLD'
>>> x.lower()
'pdpu hello world'
>>> x.title()
'Pdpu Hello World'
>>> x.isupper()
False
>>> x.istitle()
False
>>> x
'pdpu hello world'
>>> x.islower()
True
>>> x.swapcase()
'PDPU HELLO WORLD'
>>> b=3.0
>>> type(b)
<class 'float'>
>>> b.is_integer()
True
>>> b=1
>>> bool(b)
True
>>> b=0
>>> bool(b)
False
>>> b=5
>>> bool(b)
True
>>> c,d=3,6
>>> divmod(c,d)
(0, 3)
>>> divmod(d,c)
(2, 0)
>>> f=divmod(c,d)
>>> f
(0, 3)
>>> 5
5
>>> f=5
>>> bin(5)
'0b101'
>>> g=bin(f)
>>> g
'0b101'
>>> dec(g)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dec(g)
NameError: name 'dec' is not defined
>>> g>>1
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    g>>1
TypeError: unsupported operand type(s) for >>: 'str' and 'int'
>>> li=[1,2,3,4,5,6,1,2,3]
>>> li
[1, 2, 3, 4, 5, 6, 1, 2, 3]
>>> len(a)
38
>>> len(li)
9
>>> li.sort()
>>> li
[1, 1, 2, 2, 3, 3, 4, 5, 6]
>>> li.reverse()
>>> 
>>> li
[6, 5, 4, 3, 3, 2, 2, 1, 1]
>>> li.count(2)
2
>>> sum(li)
27
>>> pi
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> a
'the quick brown fox jump over the wall'
>>> a.append("s")
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.append("s")
AttributeError: 'str' object has no attribute 'append'
>>> a=a+"s"
>>> a
'the quick brown fox jump over the walls'
>>> A=[[1,2,3],[4,5,6],[7,8,9]]
>>> A
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> A[::]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> A[::-1]
[[7, 8, 9], [4, 5, 6], [1, 2, 3]]
>>> A
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> A[-1][-1]
9
>>> A[-1::-1]
[[7, 8, 9], [4, 5, 6], [1, 2, 3]]
>>> A[-1:-1:-1]
[]
>>> A[-1::]
[[7, 8, 9]]
>>> A[[::-1]]
SyntaxError: invalid syntax
>>> 
>>> g="timeline"
>>> g[0:5:-1]
''
>>> g[-8:-3:-1]
''
>>> g[-8:-3:1]
'timel'
>>> g[-3:-8:-1]
'ilemi'
>>> g[-8:-4:-1]
''
>>> 
KeyboardInterrupt
>>> g[-4:-8:-1]
'lemi'
>>> g[-4::-1]
'lemit'
>>> g[-3::-1]
'ilemit'
>>> g[-5::-1]
'emit'
>>> h="pineapple"
>>> h
'pineapple'
>>> for i in h:
	if h.count(i)>1
	
SyntaxError: invalid syntax
>>> for i in h:
	if h.count(i)>1:
		h.remove(i)

		
Traceback (most recent call last):
  File "<pyshell#101>", line 3, in <module>
    h.remove(i)
AttributeError: 'str' object has no attribute 'remove'
>>> for i in h:
	if h.count(i)>1:
		h.replace(i,'')

		
'ineale'
'pinappl'
'ineale'
'ineale'
'pinappl'
>>> for i in h:
	if h.count(i)>1:
		h=h.replace(i,'')

		
>>> h
'inal'
>>> k=""
>>> h
'inal'
>>> h
'inal'
>>> h="pineapple"
>>> for i in h:
	if i not in k:
		k+=i

		
>>> k
'pineal'
>>> j=1.3
>>> p=(int)j
SyntaxError: invalid syntax
>>> p=int(j)
>>> p
1
>>> j=5
>>> bin(j)
'0b101'
>>> int(bin(j))
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    int(bin(j))
ValueError: invalid literal for int() with base 10: '0b101'
>>> x=int(input('enter value'))
enter valuex=int(input('enter value'))
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    x=int(input('enter value'))
ValueError: invalid literal for int() with base 10: "x=int(input('enter value'))"
>>> x=int(input('enter value'))
enter value6
>>> def hello:
	
SyntaxError: invalid syntax
>>> def kll:
	
SyntaxError: invalid syntax
>>> def kilj:
	
SyntaxError: invalid syntax
>>> def kill():
	x=int(input('enter value'))
	bin(x)

	
>>> kill
<function kill at 0x06205C00>
>>> kill()
enter value5
>>> def kill():
	x=int(input('enter value'))
	print(bin(x))

	
>>> kill()
enter value5
0b101
>>> def kill():
	x=int(input('enter value'))
	p=bin(x)
	p=p[2::]

	
>>> kill()
enter value5
>>> p
1
>>> def kill():
	x=int(input('enter value'))
	p=bin(x)
	p=p[2::]
	print(p)

	
>>> kill()
enter value5
101
>>> def kill():
	x=int(input('enter value'))
	p=bin(x)
	type(p)
	p=p[2::]
	print(p)
	type(p)

	
>>> kill()
enter value5
101
>>> def kill():
	x=int(input('enter value'))
	p=bin(x)
	print(type(p))
	p=p[2::]
	print(p)
	print(type(p))

	
>>> kill()
enter value5
<class 'str'>
101
<class 'str'>
>>> def kill():
	x=int(input('enter value'))
	p=bin(x)
	print(type(p))
	p=p[2::]
	print(p)
	print(type(p))
	k=int(p)
	print(k)
	print(type(k))

	
>>> kill()
enter value5
<class 'str'>
101
<class 'str'>
101
<class 'int'>
>>> def le():
	x=int(input("Enter a no"))
	y=len(x)
	print(y)

	
>>> le()
Enter a no89765
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    le()
  File "<pyshell#163>", line 3, in le
    y=len(x)
TypeError: object of type 'int' has no len()
>>> def le():
	x=int(input("Enter a no"))
	y=len(str(x))
	print(y)

	
>>> le()
Enter a no89765
5
>>> x
6
>>> x=list(range(1,6,2))
>>> x
[1, 3, 5]
>>> x
[1, 3, 5]
>>> sum(x)
9
>>> x.sum()
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    x.sum()
AttributeError: 'list' object has no attribute 'sum'
>>> for i in range(5):
	print(i*'*')

	

*
**
***
****
>>> for i in range(1,6):
	print(i*'*')

	
*
**
***
****
*****
>>> for i in range(5,0,-1):
	print(i*'*')

	
*****
****
***
**
*
>>> k=" "
>>> for i in range(5,0,-1):
	print(k*(5-i+1),i*'*')

	
  *****
   ****
    ***
     **
      *
>>> for i in range(5,0,-1):
	print(k*(5-i),i*'*')

	
 *****
  ****
   ***
    **
     *
>>> for i in range(5,0,-1):
	print(i,k*(5-i+1),i*'*')

	
5   *****
4    ****
3     ***
2      **
1       *
>>> for i in range(1,5):
	print(k*(5-i),i*'*')

	
     *
    **
   ***
  ****
>>> for i in range(5,0,-1):
	print(k*(5-i+1)," ",i*'*')

	
    *****
     ****
      ***
       **
        *
>>> for i in range(1,6):
	print(k*(5-i+1)," ",i*'*')

	
        *
       **
      ***
     ****
    *****
>>> for i in range(1,6):
	print(k*(5-i+1),i*' *')

	
       *
      * *
     * * *
    * * * *
   * * * * *
>>> l=54321
>>> for i in range(5):
	l[:i+1:]

	
Traceback (most recent call last):
  File "<pyshell#200>", line 2, in <module>
    l[:i+1:]
TypeError: 'int' object is not subscriptable
>>> for i in range(5):
	l[:(i+1):]

	
Traceback (most recent call last):
  File "<pyshell#202>", line 2, in <module>
    l[:(i+1):]
TypeError: 'int' object is not subscriptable
>>> for i in range(5):
	l[0:i:1]

	
Traceback (most recent call last):
  File "<pyshell#204>", line 2, in <module>
    l[0:i:1]
TypeError: 'int' object is not subscriptable
>>> l="54321"
>>> for i in range(5):
	l[:i+1:]

	
'5'
'54'
'543'
'5432'
'54321'
>>> for i in range(5,0,-1):
	print(i)

	
5
4
3
2
1
>>> for i in range(5):
	print(l[:i+1:])

	
5
54
543
5432
54321
>>> l='54321'
>>> p='12345'
>>> for i in range(1,6):
	print(k*(6-i),l[-1:-i:-1],0,p[:i:])

	
       0 1
     1 0 12
    12 0 123
   123 0 1234
  1234 0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-1:-i:-1],0,p[:i-1:])

	
        0 
      1 0 1
     12 0 12
    123 0 123
   1234 0 1234
  12345 0 12345
>>> for i in range(1,7):
	print(k*(7-i),p[-1:-i:-1],0,p[:i-1:])

	
        0 
      5 0 1
     54 0 12
    543 0 123
   5432 0 1234
  54321 0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-1:-i:-1],0,p[:i-1:])

	
        0 
      1 0 1
     12 0 12
    123 0 123
   1234 0 1234
  12345 0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-i:-1:-1],0,p[:i-1:])

	
        0 
       0 1
      0 12
     0 123
    0 1234
   0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-i:-1:1],0,p[:i-1:])

	
        0 
      2 0 1
     32 0 12
    432 0 123
   5432 0 1234
  5432 0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-i::1],0,p[:i-1:])

	
       1 0 
      21 0 1
     321 0 12
    4321 0 123
   54321 0 1234
  54321 0 12345
>>> for i in range(0,7):
	print(k*(7-i),l[-i:-1:1],0,p[:i:])

	
        5432 0 
        0 1
      2 0 12
     32 0 123
    432 0 1234
   5432 0 12345
  5432 0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-i:-1:1],0,p[:i-1:])

	
        0 
      2 0 1
     32 0 12
    432 0 123
   5432 0 1234
  5432 0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-i+1::],0,p[:i-1:])

	
       54321 0 
      1 0 1
     21 0 12
    321 0 123
   4321 0 1234
  54321 0 12345
>>> 
KeyboardInterrupt
>>>  for i in range(1,7):
	print(k*(7-i),l[-i+1:0:],0,p[:i-1:])
	
SyntaxError: unexpected indent
>>> for i in range(1,7):
	print(k*(7-i),l[-i+1:0:],0,p[:i-1:])

	
        0 
       0 1
      0 12
     0 123
    0 1234
   0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-i+1:-1:],0,p[:i-1:])

	
       5432 0 
       0 1
     2 0 12
    32 0 123
   432 0 1234
  5432 0 12345
>>> for i in range(1,7):
	print(k*(7-i),l[-i+1:1:],0,p[:i-1:])

	
       5 0 
       0 1
      0 12
     0 123
    0 1234
  5 0 12345
>>> 
KeyboardInterrupt
>>> for i in range(1,7):
	print(k*(7-i),l[-i+1:-1:],0,p[:i-1:])

	
       5432 0 
       0 1
     2 0 12
    32 0 123
   432 0 1234
  5432 0 12345
>>> q="they stumble who run fast"
>>> for i in q:
	if i is " ":
		print(q[:i:])

		
Traceback (most recent call last):
  File "<pyshell#253>", line 3, in <module>
    print(q[:i:])
TypeError: slice indices must be integers or None or have an __index__ method
>>> for i in q;
SyntaxError: invalid syntax
>>> for i in q:
	print(i)

	
t
h
e
y
 
s
t
u
m
b
l
e
 
w
h
o
 
r
u
n
 
f
a
s
t
>>> for i in q:
	if i is not " ":
		print(i,end="")
	else:
		print()

		
they
stumble
who
run
fast
>>> k="Wheresoever you go, go with all your heart"
>>> s=k.index('g')
>>> p=k.index('G')
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    p=k.index('G')
ValueError: substring not found
>>> s=min(s,p)
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    s=min(s,p)
TypeError: '<' not supported between instances of 'str' and 'int'
>>>  k="Wheresoever you go, go with all your heart"
>>> s=k.index('g')
>>> p=k.index('a')
SyntaxError: unexpected indent
>>> k="Wheresoever you go, go with all your heart"
>>> s=k.index('g')
>>> p=k.index('a')
SyntaxError: multiple statements found while compiling a single statement
>>> k="Wheresoever you go, go with all your heart"
>>> s=k.index('g')
>>> p=k.index('a')
>>> s=min(s,p)
>>> print(k[s::])
go, go with all your heart
>>> s
16
>>> s=’12.5#4.56#7.22'
SyntaxError: invalid character in identifier
>>> s="12.5#4.56#7.22"
>>> li=s[for i in s if s is not '#']
SyntaxError: invalid syntax
>>> li
[6, 5, 4, 3, 3, 2, 2, 1, 1]
>>> 5 in li
True
>>> a= [‘a’,’b’,’c’]
>>> for i,j in enumerate(a):
print i,j
SyntaxError: invalid character in identifier
>>> a
'the quick brown fox jump over the walls'
>>> c
3
>>> c=['a','b','c']
>>> for i,j in enumerate(c):
	print(i,j)

	
0 a
1 b
2 c
>>> 
>>> s
'12.5#4.56#7.22'
>>> lis=[s for i in s if s is not '#']
>>> lis
['12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22', '12.5#4.56#7.22']
>>> s=s.replace("#"," ")
>>> 
>>> s
'12.5 4.56 7.22'
>>> l
'54321'
>>> l="12+2"
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    int(l)
ValueError: invalid literal for int() with base 10: '12+2'
>>> lis=[i for i in s if s is not ' ']
>>> lis
['1', '2', '.', '5', ' ', '4', '.', '5', '6', ' ', '7', '.', '2', '2']
>>> s
'12.5 4.56 7.22'
>>> lis=[[i for i in s if s is not " "]]
>>> lis
[['1', '2', '.', '5', ' ', '4', '.', '5', '6', ' ', '7', '.', '2', '2']]
>>> lis=[i for i in s if i is not ' ']
>>> lis
['1', '2', '.', '5', '4', '.', '5', '6', '7', '.', '2', '2']
>>> lis=[s[:i:] for i in s if i is not ' ']
Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    lis=[s[:i:] for i in s if i is not ' ']
  File "<pyshell#305>", line 1, in <listcomp>
    lis=[s[:i:] for i in s if i is not ' ']
TypeError: slice indices must be integers or None or have an __index__ method
>>> lis=[s[:s.index(i):] for i in s if i is not ' ']
>>> lis
['', '1', '12', '12.', '12.5 ', '12', '12.', '12.5 4.5', '12.5 4.56 ', '12', '1', '1']
>>> k
'Wheresoever you go, go with all your heart'
>>> l
'12+2'
>>> l=[]
>>> for i in s:
	if s is " ":
		t=s[0:s.index(" "):]
		l.append(t)
		s=s.replace(t,'')
print(l)
SyntaxError: invalid syntax
>>> for i in s:
	if s is " ":
		t=s[0:s.index(" "):]
		l.append(t)
		s=s.replace(t,'')

		
>>> l
[]
>>> s
'12.5 4.56 7.22'
>>> for i in s:
	if s is " ":
		t=s[0:s.index(" "):]
		print(t)
		l.append(t)
		s=s.replace(t,'')

		
>>> l
[]
>>> s
'12.5 4.56 7.22'
>>> for i in s:
	if i is " ":
		t=s[0:s.index(" "):]
		l.append(t)
		s=s.replace(t,'')

		
>>> l
['12.5', '']
>>> for i in s:
	if i is " ":
		t=s[0:s.index(" "):]
		print(t)
		l.append(t)
		print(l)
		s=s.replace(t,'')
		print(s)

		

['12.5', '', '']
 4.56 7.22

['12.5', '', '', '']
 4.56 7.22
>>> s
' 4.56 7.22'
>>> s="12.5 4.56 7.22"
>>> l
['12.5', '', '', '']
>>> l=[]
>>> ;
SyntaxError: invalid syntax
>>> l
[]
>>> l=s.split()
>>> l
['12.5', '4.56', '7.22']
>>> sum(l)
Traceback (most recent call last):
  File "<pyshell#340>", line 1, in <module>
    sum(l)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> l=int(l)
Traceback (most recent call last):
  File "<pyshell#341>", line 1, in <module>
    l=int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> s="12.5#4.56#7.22"
>>> s
'12.5#4.56#7.22'
>>> l=[]
>>> l=s.split('#')
>>> l
['12.5', '4.56', '7.22']
>>> l=[int(l) for i in l]
Traceback (most recent call last):
  File "<pyshell#347>", line 1, in <module>
    l=[int(l) for i in l]
  File "<pyshell#347>", line 1, in <listcomp>
    l=[int(l) for i in l]
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> l=[int(i) for i in l]
Traceback (most recent call last):
  File "<pyshell#348>", line 1, in <module>
    l=[int(i) for i in l]
  File "<pyshell#348>", line 1, in <listcomp>
    l=[int(i) for i in l]
ValueError: invalid literal for int() with base 10: '12.5'
>>> l=[float(i) for i in l]
>>> l
[12.5, 4.56, 7.22]
>>> sum(l)
24.279999999999998
>>> def pattern():
	x=int(input("Enter lines"))
	k=" "
	for i in range(1,x+1):
		if(i%2!=0):
			print(k*(x-i),i*'#')
		else:
			print(k*(x-i),i*'!')

			
>>> pattern()
Enter lines4
    #
   !!
  ###
 !!!!
>>> pattern()
Enter lines5
     #
    !!
   ###
  !!!!
 #####
>>> def dup(x):
	for i in x:
		print(i*2)

		
>>> dup("apple")
aa
pp
pp
ll
ee
>>> def dup(x):
	for i in x:
		print(i*2,end="")

		
>>> dup("Apple")
AAppppllee
>>> C=[1,2,3]
>>> D=[4,5,6]
>>> l
[12.5, 4.56, 7.22]
>>> li
[6, 5, 4, 3, 3, 2, 2, 1, 1]
>>> lis
['', '1', '12', '12.', '12.5 ', '12', '12.', '12.5 4.5', '12.5 4.56 ', '12', '1', '1']
>>> lis=[sum(i,j) for i in 
KeyboardInterrupt
>>> lis=[sum(i,j) for i in C for j in D]
Traceback (most recent call last):
  File "<pyshell#376>", line 1, in <module>
    lis=[sum(i,j) for i in C for j in D]
  File "<pyshell#376>", line 1, in <listcomp>
    lis=[sum(i,j) for i in C for j in D]
TypeError: 'int' object is not iterable
>>> lis=[(i,j) for i in C for j in D]
>>> lis
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
>>> bool("None")
True
>>> bool(0)
False
>>> bool(1)
True
>>> bool(4)
True
>>> long("False")
Traceback (most recent call last):
  File "<pyshell#383>", line 1, in <module>
    long("False")
NameError: name 'long' is not defined
>>> float("False")
Traceback (most recent call last):
  File "<pyshell#384>", line 1, in <module>
    float("False")
ValueError: could not convert string to float: 'False'
>>> st=3.4e0
>>> float(str)
Traceback (most recent call last):
  File "<pyshell#386>", line 1, in <module>
    float(str)
TypeError: float() argument must be a string or a number, not 'type'
>>> float(st)
3.4
>>> st
3.4
>>> st=3.4e10
>>> st
34000000000.0
>>> 3.4e2
340.0
>>> 3.4E2
340.0
>>> 3.4E-2
0.034
>>> 4E2
400.0
>>> st="4E2"
>>> st
'4E2'
>>> int(st)
Traceback (most recent call last):
  File "<pyshell#397>", line 1, in <module>
    int(st)
ValueError: invalid literal for int() with base 10: '4E2'
>>> float(st)
400.0
>>> false
Traceback (most recent call last):
  File "<pyshell#399>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> hex(st)
Traceback (most recent call last):
  File "<pyshell#400>", line 1, in <module>
    hex(st)
TypeError: 'str' object cannot be interpreted as an integer
>>> st="101"
>>> int(st)
101
>>> st
'101'
>>> int(st,2)
5
>>> int(st,8)
65
>>> 
KeyboardInterrupt
>>> int(st,16)
257
>>> st
'101'
>>> 
