'''PROBLEM STATEMENT Points: 30
As the Monk is also taking part in the CodeMonk Series, this week he learned about hashing. Now he wants to practice some problems. So he came up with a simple problem. Firstly, he made a hash function F such that:

F(x) = x % 10

Now using this function he wants to hash N integers and count the number of collisions that will occur while hashing the integers.

Input:
The first line contains an integer T, denoting the number of test cases.
The first line of each test case contains an integer N, denoting the number of integers to hash.
The next line contains N space separated integers, denoting the integer X to hash.

Output:
For each test case, print the number of collisions that will occur while hashing the integers.

Constraints:
1 <= T <= 10
1 <= N <= 100
0 <= X <= 105

SAMPLE INPUT 
2
3
1 2 3
4
1 1 2 3
SAMPLE OUTPUT 
0
1
Explanation
In the first case, there will be no collisions as each integer will be hashed to a different index.
F(1) = 1 % 10 = 1
F(2) = 2 % 10 = 2
F(3) = 3 % 10 = 3

In the second case, there will be 1 collision at index 1 as the first two integers will hash to the same index.

Time Limit: 1.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Swift-4.1, Visual Basic
'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
#lst=""
for i in range(t):
    c=0
    lst=""
    l=int(input())
    x=input().split(' ')
    
    for j in x:
        m=str(int(j)%10)
        if m in lst:
            c=c+1
        else:
            lst=lst+" "+m
    lst=""        
    print(c)
