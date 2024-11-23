#Q1
'''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5
'''
'''
def square(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,end=' ')
        print()
square(5)
'''
#Q2
'''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''
'''
def square(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=' ')
        print()
square(5)
'''
#Q3
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
'''
def rightTriangle(n):
    dummy=1
    for i in range(1,n+1):
        for j in range(i):
            print(dummy,end=' ')
        print()
        dummy+=1
rightTriangle(5)
'''
#Q4
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
'''
'''
def leftTriangle(n):
    dummy=n
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(dummy,end=' ')
        print()
        dummy-=1
        n-=1
leftTriangle(5)
'''
#Q5
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

'''
'''
def continueNumber(n):
    dummy=1
    for row in range(1,n+1):
        for col in range(row):
            print(dummy,end=' ')
            dummy+=1
        print()
continueNumber(5)
'''
#Q6
'''     1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5
'''
'''
def rightTriangle(n):
    space=n-1
    stars=1
    for row in range(1,n+1):
        dummy=1
        for sp in range(1,space+1):
            print(' ',end=' ')
        for stars in range(1,stars+1):
            print(dummy,end=' ')
            dummy+=1
        print()
        space-=1
        stars+=1
rightTriangle(5)
'''
#Q7
'''
1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1           
'''
'''
def rightTriangle(n):
    space=n-1
    stars=n
    for row in range(1,n+1):
        dummy=1
        for sp in range(1,space+1):
            print(' ',end=' ')
        for stars in range(1,stars+1):
            print(dummy,end=' ')
            dummy+=1
        print()
        space+=1
        stars-=1
       
rightTriangle(5)
'''
#Q8
'''
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5
'''
'''
def halfPyramid(n):
    space=n-1
    num=1
    for r in range(1,n+1):
        for sp in range(1,space+1):
            print(' ',end=' ')
        for col in range(1,num+1):
            print(r,end=' ')
        print()
        space-=1
        num+=2
halfPyramid(5)
'''
#Q9
'''
5 5 5 5 5 5 5 5 5 
  4 4 4 4 4 4 4 
    3 3 3 3 3 
      2 2 2 
        1 
'''
'''
def bottomHalfPyramid(n):
    num=(2*n)-1
    space=0
    num1=n
    for r in range(1,n+1):
        for sp in range(1,space+1):
            print(' ',end=' ')
        for num in range(1,num+1):
            print(num1,end=' ')
        
        print()
        space+=1
        num-=2
        num1-=1
bottomHalfPyramid(5)
'''
#Q10
'''
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 
  4 4 4 4 4 4 4 
    3 3 3 3 3 
      2 2 2 
        1 
'''
'''
def halfPyramid(n):
    space=n-1
    num=1
    for r in range(1,n+1):
        for sp in range(1,space+1):
            print(' ',end=' ')
        for col in range(1,num+1):
            print(r,end=' ')
        print()
        space-=1
        num+=2

def bottomHalfPyramid(n):
    num=(2*n)-3
    space=1
    num1=n-1
    for r in range(1,n+1):
        for sp in range(1,space+1):
            print(' ',end=' ')
        for num in range(1,num+1):
            print(num1,end=' ')
        
        print()
        space+=1
        num-=2
        num1-=1
halfPyramid(5)
bottomHalfPyramid(5)
'''
