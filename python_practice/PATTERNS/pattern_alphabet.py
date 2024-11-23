#Q1.
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
for row in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    stars+=1 
'''

#Q2.
'''
ABCDE
ABCD
ABC
AB
A
'''
'''
n=int(input())
stars=n
for row in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    stars-=1
'''

#Q3.
'''
ABCDE
 ABCD
  ABC
   AB
    A
'''
'''
n=int(input())
stars=n
spaces=0
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    stars-=1
    spaces+=1
'''

#Q4.
'''
ABCDE
 BCDE
  CDE
   CD
    E
'''
'''
n=int(input())
stars=n
spaces=0
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    stars-=1
    spaces+=1
'''

#Q5.
'''
ABCDE
 FGHI
  JKL
   MN
    O
'''
'''
n=int(input())
stars=n
spaces=0
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    stars-=1
    spaces+=1
'''

#Q6.
'''
A A A A A 
  B B B B 
    C C C 
      D D 
        E 
'''
'''
n=int(input())
stars=n
spaces=0
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
    print()
    stars-=1
    spaces+=1
'''

#sireesha Q.
'''
n=int(input())
stars=n
spaces=0
dummy=(n//2)+1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
    if row<n//2:
        dummy-=1
        stars-=2
        spaces+=1
    else:
        dummy+=1
        stars+=2
        spaces-=1
    print()
'''

#interview Q.S
#Q1.
'''
1
  2
   3
  4
 5
'''
'''
1
 2
  3
   4
  5
 6
7
'''
'''
n=int(input())
spaces=0
stars=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
            print(' ',end=' ')
    for st in range(1,stars+1):
            print(dummy,end=' ')
    if row<n//2+1:
        spaces+=1
    else:
        spaces-=1
    print()
'''

#Q2.
'''
1
 2
  3
 5
4
'''
'''
1
 2
  3
   4
  7
 6
5
'''
'''
n=int(input())
spaces=0
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
            print(' ',end=' ')
    for st in range(1,stars+1):
            print(dummy,end=' ')
    if row<n//2+1:
        spaces+=1
        dummy+=1
    elif row==n//2+1:
        spaces-=1
        dummy=dummy+n//2  #or dummy=n
    else:
        spaces-=1
        dummy-=1
        
    print()
'''
#Q3.
'''
1
 3
  5
 4
2
'''
'''
1
 3
  5
   7
  6
 4
2
'''
'''
n=int(input())
spaces=0
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
            print(' ',end=' ')
    for st in range(1,stars+1):
            print(dummy,end=' ')
    if row<n//2+1:
        spaces+=1
        dummy+=2
    elif row==n//2+1:
        spaces-=1
        dummy-=1
    else:
        spaces-=1
        dummy-=2
    print()
'''

#Q4.
'''
2
 3
  5
 7
11
'''
'''
2
 3
  5
   7
  11
 13
17
'''
'''
l=[]
n=2
c=0
noofprime=int(input())
while c<noofprime:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        l.append(n)
        c+=1
    n+=1
print(l)

r=noofprime
spaces=0
stars=1
for ip in range(0,len(l)):
    dummy=l[ip]
    for sp in range(1,spaces+1):
            print(' ',end=' ')
    for st in range(1,stars+1):
            print(dummy,end=' ')
    if ip<noofprime//2:
        spaces+=1
    else:
        spaces-=1
    print()
'''

#Q5.
'''
2
 3
  5
  8
13
'''
'''
2
 3
  5
   8
   13
  21
34










            


























