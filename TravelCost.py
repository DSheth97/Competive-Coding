'''

You
dhruvil3
0 / 9 0 / 9 
Chelsea
chelsea.bartley
TIME LEFT:  0 0 :  0 0 :  0 0
HRS MIN SEC
PROBLEM STATEMENT Points: 30
Walter White is on a tour to sell meth. There are N cities.

Each city has a id between 1 and N (both inclusive).

You are given cost matrix.

In cost matrix, the  element in the  row denotes the cost of travelling between cities with  i and j.

 and 

Given the path taken by Walter, print the cost of travelling.

Walter is at city with  1 right now.

Input:

First N lines contain names of cities. Each name consists of alphabets only and not more than  alphabets. No two cities have the same name.

City with name in the  line has id i.

Next line contains P, the number of cities he visits.

Each of the next P line denotes the name of the cities he is going to visit, in sequence.

Output:

Print the total cost of travelling assuming he starts from city with id 1.

Constraints:




SAMPLE INPUT 
3
delhi
bengaluru
hyderabad
0 10 20
10 0 55
20 55 0
4
bengaluru
delhi
hyderabad
bengaluru
SAMPLE OUTPUT 
95
Time Limit: 3.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Swift-4.1, Visual Basic
ACTIVITY
Save


1:1
 Provide custom input
 Finish and Quit Run   Submit
?

'''
n=int(input())
a=list()
k=0
c=list()
v=list()
for i in range(n):
    a.append(input())
for j in range(n):
    x=input()
    c[k]=x.split(' ')
    k=k+1
q=int(input())
for p in range(n):
    v.append(input())
print(a)
print(c)
print(v)
