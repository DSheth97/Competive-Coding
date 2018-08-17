'''You
dhruvil3
0 / 10 0 / 10 
Murtaz
murtaz1
TIME LEFT:  0 0 :  2 0 :  4 0
HRS MIN SEC
PROBLEM STATEMENT Points: 30
Monk has to visit a land where strange creatures, known as Pokemons, roam around in the wild. Each Pokemon in the land will attack any visitor. They can only be pacified by feeding them their favorite food.

The Pokemon of type X eats one food item of type X.

Monk knows that he will encounter N ponds on the way. At each pond, he will find a food item and then encounter a Pokemon. The i'th pond has the food item of type Ai and the Pokemon of type Bi.

The monk can feed the item at the i'th pond to the Pokemon at the pond if the type matches. Monk may have to carry some food items with him before leaving so as to feed all the Pokemons. Help him find the number of items he must carry, to be to able to pass through the land safely.

Input:
The first line contains T, denoting the number of test cases. Then, T test cases follow.
The first line of each test case contains an integer N. Then, N lines follow.
Each line consists of 2 space-separated integers Ai and Bi.

Output: For each test case, print the answer in a new line.

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 105
1 ≤ Ai, Bi ≤ 106

SAMPLE INPUT 
1
5
1 1
2 2
3 4
4 3
2 4
SAMPLE OUTPUT 
1
Explanation
At First Pond he gets item of type1 and feeds it to the Pokemon of type1.
At Second Pond he gets item of type 2 and feeds it to the Pokemon of type2.
At Third Pond he gets item of type 3 ,but the Pokemon is of type4 . Hence, he has to bring a food item of type 4 with him.
At Fourth Pond he gets item of type 4. He already has a item of type 3 and feeds it to the Pokemon. 
At Fifth Pond he gets items of type 2. He already has a item of type 4 and feeds it to the Pokemon at this pond.

Time Limit: 2.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Swift-4.1, Visual Basic
ACTIVITY
murtaz1 has compiled the code.
8/12/2018, 8:29:00 PM
Save


23:14
 Provide custom input
Log ID: 52373974 / Aug 12, 2018 08:28 PM IST
RESULT: Sample Test Cases Passed
Time (sec)

0.111309

 
Memory (KiB)

64

 
Language

Python 3

Input
1
5
1 1
2 2
3 4
4 3
2 4
Your Code's Output
1
Expected Correct Output
1
Compilation Log
Compiled successfully.
Execution Log
No execution log!
 Finish and Quit Run   Submit
?



# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
x=list()
y=list()
c=0
for i in range(t):
    n=int(input())
    c=0
    for i in range(n):
        x=input().split(' ')
        y.append(int(x[0]))
        if int(x[1]) in y:
            y.remove(int(x[1]))
        else:
            c=c+1
    print(c)
    del y[:]
