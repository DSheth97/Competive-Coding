# A utility function to calculate area 
# of triangle formed by (x1, y1), 
# (x2, y2) and (x3, y3)
 
def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) 
                + x3 * (y1 - y2)) / 2.0)
 
 
# A function to check whether point P(x, y)
# lies inside the triangle formed by 
# A(x1, y1), B(x2, y2) and C(x3, y3) 
def isInside(x1, y1, x2, y2, x3, y3, x, y):
 
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC 
    A1 = area (x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC 
    A2 = area (x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB 
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3 
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False
 
# Driver program to test above function
# Let us check whether the point P(10, 15)
# lies inside the triangle formed by 
# A(0, 0), B(20, 0) and C(10, 30)
 



def main():
    n=int(input())
    for i in range(n):
        j=input()
        lst=j.split(' ')
        ls=[int(k) for k in lst]
        if (isInside(ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6],ls[7])):
            print('INSIDE')
        else:
            print('OUTSIDE')
