#NUMBER PATTERN:
'''
SCENRIOS:
    1.ROW WISE INCREMENTATION (we have to increment or decrement in outer loop)
                             (outside of inner loop)
                             
            a. re-initialization                    :(variable creation should be inside outer loop
            b. inc/dec value is carried to next row :(variable should be created outside the outer loop)

                                  
    2.COLUMN WISE INCREMENTATION (we have inc/dec in inner loop(star loop))
    
            a. re-initialization                       :(variable creation should be inside outer loop
            b. inc/dec value is carried to next column :(variable should be created outside the outer loop)
'''
#Q1.
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''

#Q2.
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')    
    print()
    dummy+=1
'''

#Q3.
'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''

#Q4.
'''
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
6 7 8 9 10
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n):
        print(dummy,end=' ')
        dummy+=1
    print()
'''
#Q5.
'''
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''

#Q6.
'''
1 6 11 16 21
2 7 12 17 22
3 8 13 18 23
4 9 14 19 24
5 10 15 20 25
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=5
    print()
'''

#Q7.
'''
1 2 3 4 5
2 4 6 8 10
3 4 5 6 7
4 6 8 10 12
5 6 7 8 9
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        if row%2!=0:
            dummy+=1
        else:
            dummy+=2
    print()
'''


# number + star pattern
#Q1.
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=1
    for num in range(1,row+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''

#Q2.    
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    for num in range(1,row+1):
        print(dummy,end=' ')
    dummy+=1    
    print()
'''



#Q3.
'''

    1
   22
  333
 4444
55555
'''
'''
n=int(input())
spaces=n-1
for row in range(1,n+1):
    num=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,row+1):
        print(row,end=' ')
    print()
    spaces-=1
'''    


#Q4.
'''
     1
    12
   123
  1234
 12345
 '''
'''    
n=int(input())
num=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(num,end=' ')
    print()
    spaces-=1
    num+=1    
'''
'''
n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    spaces-=1
    stars+=1  
'''
#Q5.
'''
     1
    21
   321
  4321
 54321
'''
'''
n=int(input())
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,row+1):
        print(row,end=' ')
        row-=1
    print()
    spaces-=1
'''

#Q6.
'''
     1
    1
   1
  1
 1
'''
'''
n=int(input())
spaces=n-1
for row in range(1,n+1):
    num=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(num,end=' ')
    print()
    spaces-=1 
'''

#Q7.
'''
1
 1
  1
   1
    1
'''
'''
n=int(input())
spaces=0
for row in range(1,n+1):
    num=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(num,end=' ')
    print()
    spaces+=1  
'''
#Q8.
'''
     1
    2
   3
  4
 5
'''
'''
n=int(input())
spaces=n-1
for row in range(1,n+1):
    num=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(row,end=' ')
    print()
    spaces-=1
'''

#Q9.
'''
1
 2
  3
   4
    5
'''
'''
n=int(input())
spaces=0
for row in range(1,n+1):
    num=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(row,end=' ')
    print()
    spaces+=1
'''

#Q10.
'''
1
21
321
4321
54321
'''
'''
n=int(input())
for row in range(1,n+1):
    for num in range(1,row+1):
        print(row,end=' ')
        row-=1
    print()
'''

#Q11.
'''
12345
1234
123
12
1
'''
'''
n=int(input())
num=n
for row in range(1,n+1):
    dummy=1
    for num in range(1,num+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    num-=1
'''

#Q12.
'''
54321
4321
321
21
1
'''
'''
n=int(input())
for row in range(1,n+1):
    num=n
    for number in range(1,num+1):
        print(num,end=' ')
        num-=1
    print()
    n-=1
'''

#Q13.
'''
12345
 1234
  123
   12
    1
'''
'''
n=int(input())
spaces=0
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    spaces+=1
    n-=1
'''

#Q14.
'''
54321
 4321
  321
   21
    1
'''
'''
n=int(input())
spaces=0
for row in range(1,n+1):
    dummy=n
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,n+1):
        print(dummy,end=' ')
        dummy-=1
    print()
    spaces+=1
    n-=1
'''

#Q15.
'''
11111
 2222
  333
   44
    5
'''
'''
n=int(input())
spaces=0
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,n+1):
        print(dummy,end=' ')
    print()
    spaces+=1
    n-=1
    dummy+=1
'''

#Q16.
'''
55555
 4444
  333
   22
    1
'''
'''
n=int(input())
spaces=0
for row in range(1,n+1):
    dummy=n
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,n+1):
        print(dummy,end=' ')
    print()
    spaces+=1
    n-=1
'''

#Q17.
'''
55555
4444
333
22
1
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=n
    for num in range(1,n+1):
        print(dummy,end=' ')
    print()
    n-=1
'''

#Q18.
'''
11111
2222
333
44
5
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=n
    for num in range(1,n+1):
        print(row,end=' ')
    print()
    n-=1
'''
#Q20.
'''
    1
   222
  33333
 4444444
555555555
'''
'''
n=int(input())
spaces=n-1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,dummy+1):
        print(row,end=' ')
    print()
    spaces-=1
    dummy+=2
'''

#Q20.
'''
555555555
 4444444
  33333
   222
    1
'''
'''
n=int(input())
spaces=0
dummy=(n*2)-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,dummy+1):
        print(n,end=' ')
    print()
    spaces+=1
    dummy-=2
    n-=1
'''
#Q21.
'''
    1
   222
  33333
   444
    5
'''
'''
n=int(input())
dummy=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for num in range(1,dummy+1):
        print(row,end=' ')
    print()
    if row<=n//2:
        dummy+=2
        spaces-=1
    else:
        dummy-=2
        spaces+=1
'''
#Q22.
'''
    1
   222
  33333
 4444444
555555555
 4444444
  33333
   222
    1
'''
'''
n=int(input())
dummy=1
num=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for number in range(1,dummy+1):
        print(num,end=' ')
    print()
    if row<=n//2:
        dummy+=2
        spaces-=1
        num+=1
    else:
        dummy-=2
        spaces+=1
        num-=1
'''   
