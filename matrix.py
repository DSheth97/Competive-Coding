'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
n,m = input().strip().split(' ')
n,m = [int(n), int(m)] 

matrix = [[input() for j in range(m)] for i in range(n)]
