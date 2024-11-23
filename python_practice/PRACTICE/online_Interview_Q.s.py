# 1. TAKING EXACTLY n VALUE FROM THE USER AND ADDING IT TO THE LIST:
'''
n=int(input())
l=[]
for i in range(n):
      value=int(input())
      l.append(value)
print(l)
'''

# 2. INFINITE LOOP:
''' 1. infinite loop can be created by using while loop
    2. this infinite loop should be terminated by using break statement'''
#taking integer inputs from the user and adding it to the list until the given value is less than zero(0)
'''
l=[]
while True:
    value=int(input())
    if value<0:
              break
    l.append(value)
print(l)
'''
'''OR'''
'''
l=[]
while True:
    value=int(input())
    if value>=0:
        l.append(value)
    else:
        break
print(l)
'''

#WAPTP 1st 100 PRIME NO.s
'''
c=0
n=2
while c<100:
    for i in range(2,(n//2)+1):
        if n%i==0:
            break
    else:
            c+=1
            print(n)
    n+=1
'''




#WAPTP 100th PRIME NO.
'''
c=0
n=2
while c<100:
    for i in range(2,(n//2)+1):
        if n%i==0:
            break
    else:
            c+=1
            if c==100:
                print(n)
    n+=1
'''

#WAPTP PRIME NO.s PRESENT BETWEEN 1 TO 100
'''
for n in range(1,101):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                break
        else:
            print(n)
            '''

#WAPTP FIRST 10 ARMSTRONG NO
'''
c=0
n=100
while True:
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
    if summ==n:
        c+=1
        print(n)
    n+=1
    if c==10:
        break
        '''
    
#WAPTP 10TH ARMSTRONG NO
'''
c=0
n=100
while True:
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
    if summ==n:
        c+=1
    n+=1
    if c==10:
        print(n)
        break
'''
#WAPTP 1st 10 PERFECT NO.
'''
n=1
c=0
while True:
    sum=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum+=i
    if sum==n:
        c+=1
        print(n)
    n+=1
    if c==10:
        break
        '''
#WAPTP 4th PERFECT NO.
'''
n=1
c=0
while True:
    sum=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum+=i
    if sum==n:
        c+=1
    n+=1
    if c==4:
        print(n)
        break
        '''

#WAP 1ST 10 DISARIUM NO
'''
c=0
n=100
while True:
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
        l-=1
    if summ==n:
        c+=1
        print(n)
    n+=1
    if c==10:
        break
'''
#WAPTP 10TH DASIRIUM NO
'''
c=0
n=5
while True:
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
        l-=1
    if summ==n:
        c+=1
        if c==10:
            print(n)
            break
    n+=1
    '''
#WAPTP 1ST 10 HARSHAD NO
'''
c=0
n=10
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem
    if n%summ==0:
         c+=1
         print(n)
    if c==10:
        break
    n+=1
    '''
#WAPTP 10th HARSHAD NO
'''
c=0
n=10
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem
    if n%summ==0:
         c+=1
    if c==10:
        print(n)
        break
    n+=1
'''
#WAPTP SPECIAL NO
#SPECIAL NO:IT IS SUM OF FACTORIAL OF INDIVIDUAL DIGIT OF THE GIVEN NUMBER. eg: 145= (1!)+(4!)+(5!)=1+24+120=145
'''
n=int(input())
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    dummy//=10
    summ=summ+fact
if summ==n:
    print(n)
'''

#WAPTP SPECIAL NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
for n in range(ll,ul+1):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        dummy//=10
        summ=summ+fact
    if summ==n:
        print(n)
'''

#WAPTP 1ST 10 SPECIAL NO
'''
c=0
n=1
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        dummy//=10
        summ+=fact
    if summ==n:
        c+=1
        print(n)
        if c==10:
            break
    n+=1
'''
#WAPTP 4TH SPECIAL NO
'''
c=0
n=1
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        dummy//=10
        summ+=fact
    if summ==n:
        c+=1
        if c==4:
            print(n)
            break
    n+=1
'''



#2 conditions:
'''
1. stopping the loop when condition is false
2. breaking the infinite loop with external value/condition
'''

#WAPTP 1st 10 ARMSTRONG NO (while inside while)
#special no. 145 , if or not... in range....10th special no..


















