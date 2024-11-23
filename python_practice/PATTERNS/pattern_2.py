#PATTERN DAY  2:
#Q1.         1. one thing constant   2. one thing depending on rows  3. what's the relationship
'''
    *
  * * *
* * * * *

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

here, rows=3 spaces=2, rows=5 spaces=5
since, row>spaces....we need to go either - or //...here it is  3-1= 2spaces...5-1= 4spaces....n-1
'''
'''
n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=2
'''
#Q2.  1. what is static/constant   2. what is dynamic    3. whats the relationship
'''
* * * * *
  * * *
    *
    
* * * * * * * * *
  * * * * * * *
   * * * * *
     * * *
       *
here, rows=3 stars=5, rows=5 stars=9
since, row <stars....we need to go either + or *...here it is  3*2=6-1=5, 5*2=10-1=9....(n*2)-1
'''
'''
n=int(input())
spaces=0
stars=(n*2)-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=2
'''
'''
n=int(input())
spaces=0
stars=n+(n-1)
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=2
'''

#Q3.
'''
1.check how stars are inc/dec
2.check how spaces are inc/dec
3.check if stars/spaces are static
4.check if stars/spaces are dyanmic
5.checking if it is both inc and dec

in this question:----->
1st half icrementing n 2nd half decrementing

*
* * *
* * * * *
* * *
*

ROW   STARS
1       1  +2
2       3  +2
3       5  -2
4       3  -2
5       1  -2

'''
'''
n=int(input())
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        stars+=2
    else:
        stars-=2
+'''    
# Q4.
'''
    *
  * * *
* * * * *
  * * *
    *

    ROW   STARS
1       1  +2
2       3  +2
3       5  -2
4       3  -2
5       1  -2
    
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

'''
'''
n=int(input())
stars=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1
'''

#NUMBER PATTERN:
'''
1. in row-wise inc and if inc value is taken to next row
   (create dummy outside loop,and inc it in outer loop)
2. in col-wise inc and if inc value is taken to next row
   (create dummy outside loop, and inc it in inner loop)
   
3. in row-wise inc and if it is re-intialized
   (create dummy inside in outer loop, and inc it in outer loop)
4. in col-wise inc and if it is re-intialized
   (create dummy inside in outer loop, and inc it in inner loop)
'''

# Q1.
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
        print(dummy, end=' ')
    print()
    dummy+=1

'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row,end=' ')
    print()
'''

# Q2.
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
        print(dummy, end=' ')
        dummy+=1
    print()
'''

#
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
        print(dummy, end=' ')
        dummy+=1
    print()
'''

#
'''
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(dummy, end=' ')
    dummy+=1   
    print()
'''







