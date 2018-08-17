n=int(input())

'''ls=[]
top=-1
def push(x):
    global top
    ls.append(x)
    top=top+1

def pop():
    global top
    if(top==-1):
        print("No Food")
    else:
        print(ls[top])
        top=top-1'''




from sys import maxsize
 
# Function to create a stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack
 
# Stack is empty when stack size is 0
def isEmpty(stack):
    return len(stack) == 0
 
# Function to add an item to stack. It increases size by 1
def push(stack, item):
    stack.append(item)
    #print("pushed to stack " + item)
     
# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        #return str(-maxsize -1) #return minus infinite
         print("No Food")
    else:
        return stack.pop()
 
# Driver program to test above functions    

stack=createStack()


for i in range(n):
    s=input()
    if(s=='1'):
        print(pop(stack))
    else:
        st=s.split(' ')
        push(stack,st[1])
        
