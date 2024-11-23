#Q1.
'''
    1
   212
  32123
 4321234
543212345

in row no. 3: --> dummy=3, stars=5
st=1, dummy=3 -->2
st=2, dummy=2 -->1

st=3, dummy=1 -->2
st=4, dummy=2 -->3
st=5, dummy=3 -->..4

'''
'''

n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if st<=stars//2:
            dummy-=1
        else:
            dummy+=1
    print()
    spaces-=1
    stars+=2
'''
#or
'''
n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if st<row:
            dummy-=1
        else:
            dummy+=1
    print()
    spaces-=1
    stars+=2
'''

#Q2.
'''
55555
54444
54333
54322
54321
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=n
    for col in range(1,n+1):
        print(dummy,end=' ')
        if row>col:
            dummy-=1
    print()
'''

#Q3.
'''
    A
   BAB
  CBABA
 DCBABCD
EDCBABCDE
'''
'''
n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        if st<=stars//2:
            dummy-=1
        else:
            dummy+=1
    print()
    spaces-=1
    stars+=2
'''

#Q4.
'''
E E E E E 
E D D D D 
E D C C C 
E D C B B 
E D C B A
'''
'''
n=int(input())
for row in range(1,n+1):
    dummy=n
    for col in range(1,n+1):
        print(chr(64+dummy),end=' ')
        if row>col:
            dummy-=1
    print()
'''

#Q5.
'''
        A 
      A B 
    A B C 
  A B C D 
A B C D E
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
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    spaces-=1
    stars+=1  
'''

#Q6.
'''
E D C B A B C D E 
  E D C B C D E 
    E D C D E 
      E D E 
        E 

n=int(input())
spaces=0
stars=(n*2)-1
for row in range(1,n+1):
    dummy=n
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        if st<=stars//2:
            dummy-=1
        else:
            dummy+=1
    print()
    spaces+=1
    stars-=2
'''

#Q7.
'''
EDCBABCDE
 DBCABCD
  CBABC
   BAB
    A
'''
'''
n=int(input())
spaces=0
stars=(n*2)-1
for row in range(1,n+1):
    dummy=n
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        if st<=stars//2:
            dummy-=1
        else:
            dummy+=1
    print()
    spaces+=1
    stars-=2
    n-=1
'''






#PQ1.
'''
    1
   232
  34543
 4567654
567898765
'''  
'''
n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if st<=stars//2:
            dummy+=1
        else:
            dummy-=1
    print()
    spaces-=1
    stars+=2
'''

#PQ2.
'''
5432112345
54322345
543345
5445
55
'''
'''
n=int(input())
stars=(n*2)
for row in range(1,n+1):
    dummy=n
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if st<stars//2:
            dummy-=1
        elif st==stars//2:
            dummy=row
        else:
            dummy+=1
    print()
    stars-=2
'''

#PQ3.
'''
543212345
5432345
54345
545
5
n=int(input())
stars=(n*2)-1
for row in range(1,n+1):
    dummy=n
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if st<=stars//2:
            dummy-=1
        else:
            dummy+=1
    print()
    stars-=2
'''

#PQ4.
'''
1
3  2
6  5  4
10 9  8  7
'''
'''
n=4
x=1
space=0
for i in range(1,n+1):
    row=' '
    for j in range(1,i+1):
        row=str(x)+row
        x+=1
    print(row)
'''
'''
    1
   32
  543
 7654
98765
'''
















