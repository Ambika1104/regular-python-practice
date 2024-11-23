#PATTERN PROGRAMS:

# PATTERN 1:
'''
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end=' ')
    print(end='\n')
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end=' ')
    print()

---->rows   
1,1   1,2   1,3  1,4  1,5
*         *        *       *      *
2,1   2,2   2,3  2,4  2,5
*         *        *       *      *
3,1   3,2   3,3  3,4  3,5
*         *        *       *      *
4,1   4,2   4,3  4,4  4,5
*         *        *       *      *
5,1   5,2   5,3  5,4  5,5
*         *        *       *      *
'''
'''
n=int(input())
for row in range(1,n+1):
    print('* '*n)
'''
# PATTERN 2:
#row to  column
'''
*
   *
        *
              *
                    *
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#PATTERN 3:
# row to col
# row+col to n+1
'''
                    *
               *
            *
        *
    *
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#NOTE : we can print the patterns, by finding out the relationships between row to column and well as (row+col) to (n+1)

#PATTERN 4:
'''
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
'''
'''
n=int(input())
for row in range(1,n+1):
    print('* '*row)
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#PATTERN 5:
'''
                    *
              *     *
         *   *     *
    *   *   *     *
*   *   *   *    *
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col>=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#PATTERN 6:
'''
* * * * *
  * * * *
     * * *
        * *
           *
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#PATTERN 7:
'''
* * * * *
* * * *
* * *
* *
*
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

# GENERIC APROACH:
#PATTERN 1:
'''
*                          star   space
  *                           1        0
    *                          1       1
       *                        1       2
          *                    1        3
                              1         4
'''
'''
n=5
spaces=0
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('* ',end=' ')
    print()
    spaces+=1
'''
#PATEERN 2:
'''
                    *
               *
            *
        *
    *
stars= 1  1 1  1  1
spaces= 4 3 2 1 0
'''
'''
n=5
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('* ',end=' ')
    print()
    spaces-=1
'''

#PATTERN 3:
'''
                    *
              *     *
         *   *     *
    *   *   *     *
*   *   *   *    *
spaces= 4 3 2 1 0
stars= 1 2 3 4 5
'''
'''
n=5
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='  ')
    for st in range(1,stars+1):
        print('*',end='  ')
    print()
    spaces-=1
    stars+=1
'''
# PATTERN 4:
'''
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
spaces= 4 3 2 1 0
stars= 1 2 3 4 5
'''
n=5
spaces=n-1
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='  ')
    for sp in range(1,spaces+1):
        print(' ',end='  ')
    print()
    spaces-=1
    stars+=1

# PATTERN 5:
'''
* * * * *
  * * * *
     * * *
        * *
           *
'''
n=5
spaces=1
stars=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='  ')
    for st in range(1,stars+1):
        print('*',end='  ')
    print()
    spaces+=1
    stars-=1

# PATTERN 6:    
'''
* * * * *
* * * *
* * *
* *
*
'''
n=5
spaces=1
stars=n-1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='  ')
    for sp in range(1,spaces+1):
        print(' ',end='  ')
    print()
    spaces+=1
    stars-=1













