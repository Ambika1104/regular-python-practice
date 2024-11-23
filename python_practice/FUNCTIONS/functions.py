# Q1.WAPTP ARMSTRONG NO. IN A GIVEN RANGE:
'''
def armstrongNo(n):
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ=summ+rem**l
    return summ

def isArmstrong(n):
    summ=armstrongNo(n)
    if summ==n:
        return True
    else:
        return False

def armstrongNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isArmstrong(i):
            print(i)

armstrongNumbers(1,1000)
'''

# Q2.WAPTP DISARIUM NO. IN A GIVEN RANGE:
'''
def disariumNo(n):
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ=summ+rem**l
        l-=1
    return summ

def isDisarium(n):
    summ=disariumNo(n)
    if summ==n:
        return True
    else:
        return False

def disariumNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isDisarium(i):
            print(i)

disariumNumbers(1,1000)
'''

# Q3.WAPTP PERFECT NO. IN A GIVEN RANGE:
'''
def pefectNo(n):
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    return summ

def isPerfect(n):
    summ=pefectNo(n)
    if summ==n:
        return True
    else:
        return False

def perfectNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isPerfect(i):
            print(i)

perfectNumbers(1,1000)
'''

# Q4.WAPTP HARSHAD NO. IN A GIVEN RANGE:
'''
def harshadNo(n):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem
    return summ

def isHarshad(n):
    summ=harshadNo(n)
    if n%summ==0:
        return True
    else:
        return False

def harshadNumber(ll,ul):
    for i in range(ll,ul+1):
        if isHarshad(i):
            print(i)

harshadNumber(1,1000)
'''
# Q5.WAPTP SPECIAL NO. IN A GIVEN RANGE:
'''
def specialNo(n):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        summ+=fact
    return summ

def isSpecial(n):
    summ=specialNo(n)
    if summ==n:
        return True
    else:
        return False

def specialNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isSpecial(i):
            print(i)

specialNumbers(1,1000)
'''
#no need to make unncessary functions
'''
def isSpecialNo(n):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        summ+=fact
    if summ==n:
        return True
    else:
        return False

def specialNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isSpecialNo(i):
            print(i)

specialNumbers(1,1000)
'''


#PATTERNS:--->
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



# 14-10-24
#----------

#fibonacci series:-->
'''
def fibo(fv=0,sv=1,n=10):
    if n==1:
        print(fv)
    elif n==2:
        print(sv)
    else:
        print(fv,sv,sep='\n')
        for i in range(n-2):
            tv=fv+sv
            print(tv)
            fv,sv=sv,tv
fibo()
'''

'''
def fibo(fv=0,sv=1,n=10):
    if n==1:
        print(fv)
    elif n==2:
        print(sv)
    else:
        print(fv,sv,end=' ')
        for i in range(n-2):
            tv=fv+sv
            print(tv, end=' ')
            fv,sv=sv,tv
fibo()
'''

'''
def fibo(fv=0,sv=1,n=5):
    for i in range(n):
        print(fv)
        fv,sv=sv,fv+sv
fibo(2,3,5)
'''



#interview Q.no 5
'''
fibonacci series:-->

2
  3
   5
  8
13


2
  3
    5
      8
    13
  21
34
'''
'''
n=int(input())
fv=2
sv=3
l=[]
for i in range(n):
    l.append(fv)
    fv,sv=sv,fv+sv

spaces=0
stars=1
for ip in range(0,len(l)):
    dummy=l[ip]
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if ip<=n//2-1:
            spaces+=1
        else:
            spaces-=1
    print()
'''




'''

MORE EXAMPLES:
--------------
def sellVegies():
    print('tamatoo onions chillies potato')
    print('lady finger')
    print('carrot drum-sticks')

def sellFruits():
    print('jamapallu jamapalloy papaya')
    print('mangoes banana')
    print('pineapple grapes')

sellFruits()    #if one f/n is created before another f/n, there is no such rule that we cannot call
sellVegies()    #the 2nd f/n before the 1st f/n


       
example:
       def add(a,b):
           print('performing addition operation')
           print('a avlue is',a)
           print('b avlue is',b)
           print(a+b)
        add(23,45)

        #add()#error
        #add(89)#error
        #add(89,78,67)#error 
        #add(23,45)#output a=23, b=45 and sum is 68

   
example:
      def add(a,b):
           print('performing addition operation')
           print('a avlue is',a)
           print('b avlue is',b)
           print(a+b)
      add(a=23,b=45) #output a=23, b=45, and sum is 68

eg: def add(a,b,/):
                    print('a value is',a)
                    print('b value is',b)
                    print(a+b)

            add(23,45) #output a=23, b=45, and sum is 68
            add(a=22,b=90) #error


eg: def add(*,a,b):
                    print('a value is',a)
                    print('b value is',b)
                    print(a+b)

            add(23,45) #error 
            add(a=22,b=90)#output a=22, b=90, and sum is 112

  
eg:
        def add(a=89,b=67):
            print('a value is',a)
            print('b value is',b)
            print(a+b)

        add()           #a=89,b=67
        add(100)        #a=100,b=67
        add(123,234)    #a=123,b=234
        add(123,456,78) #error
        

eg: def add(a,b=10):              #def add(b=10,a):  --->error
                print('a value is',a)
                print('b value is',b)
                print(a+b)
                
            add(34,46) #a=34,b=46



eg: def add(*args):
            print(args)
            print(type(args)) #add(10,20,30) -->(10,20,30) <class 'tuple'>  60
            summ=0
            for i in args:
                summ+=i
            print(summ)

        add()  #0
        add(100) #100
        add(123,234) #357


eg: def add(**kwargs):
                   print(kwargs)
                   print(type(kwargs)) #{.....}  <class 'dict'> 
                   summ=0
                   for i in kwargs:
                       summ+=kwargs[i]
                   print(summ)

                add()
                add(a=10) #{'a':10}  10  (don't give key into string, bcoz variable dont accept any spcial char)
                add(a=10,b=90,c=100) #200

eg:
                       def function(a,b=90,*args,**kwargs):
                           print(a)
                           print(b)
                           print(args)
                           print(kwargs)
                        function(78,56,999,12,22,67,9,87,name='nikky',age=10)
                        #a=78 b=56 args=(999,12,22,67,9,87) kwargs={'name'='nikky','age':10}



#examples:
      ----------
      #example 1
       def function():
           return 'hai',78
        
       res=function()
       print(res)

       #example 2
        def add():
            a=10
            b=20
            return a+b
        
        print(add())

        #example 3
         def lifeCycle(age):
             if age in range(0,13):
                 return 'child'
             elif age in range(13,20):
                 return 'teenage'
             elif age in range20,50):
                 return 'adult'
             else
                 return 'lengend'
                
         lc=lifeCycle(11)
         print(lc)
'''
         
'''             
# Q1.printing the even no.s in a given range by using functions.
def isEven(n):
    if n%2==0:
        return True
    else:
        return False

def evenNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isEven(i):
            print(i)
               
evenNumbers(1,10)
 
# Q2.printing the prime no.s in a given range by using functions.        
def isPrime(n):
    if n>1:
        for num in range(2,(n//2)+1):
            if n%num==0:
                return False
        else:
            return True
    else:
        return False

def primeNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isPrime(i):
            print(i)
               
primeNumbers(1,10)

#ITERATIONS: eg: ll=10, ul=20
1.isPrime and primeNumbers functions are defined
2.then primeNumbers function is called
3.inside primeNumbers function, for loop will run from ll to ul
4.after that isPrime function is called inside this for loop
5.iteration 1: here for 1st iteration, i=10, this 10 will be assigned to n in isPrime f/n (n=10)
               since 10>1 -->  true
               for loop will run from 2 to 6
                 1. 10%2==0 --> true
               isPrime will return false to primeNumbers function
               since this doesnt satisfies the condition of if cond, i=10 will not be printed
               and hence it is not a prime no.
       
  iteration 2: here for 2nd iteration, i=11, this 11 will be assigned to n in isPrime f/n (n=11)
               since 11>1 -->  true
               for loop will run from 2 to 6
                 1. 11%2==0 --> false
                 2. 11%3==0 --> false
                 3. 11%4==0 --> false
                 4. 11%5==0 --> false
                 5. 11%6==0 --> false
               since for block is no where getting satisfied else block will execute
               isPrime will return true to primeNumbers function
               since this does satisfies the condition of if cond, i=11 will be printed
               and hence it is a prime no.

# Q3.waptp paliprime no.s in a given range

def isPalindrome(n):
    s=str(n)
    if s==s[::-1]:
        return True
    else:
        return False
    
def isPrime(m):
    if m>1:
        for num in range(2,(m//2)+1):
            if m%num==0:
                return False
        else:
            return True
    else:
        return False

def isPaliPrime(j):
    if isPrime(j) and isPalindrome(j):
        return True
    else:
        return False

def paliPrimeNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isPaliPrime(i):
            print(i)
            
paliPrimeNumbers(1,1000)

'''
'''OR'''
'''
def reverse(n):
    dummy=n
    rev=0
    while dummy>0:
        rem=dummy%10
        rev=rev*10+rem
        dummy//=10
    return rev
    
def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

def isPaliPrime(n):
    rev=reverse(n)
    if isPrime(n) and rev==n:
        return True
    else:
        return False

def paliPrimeNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isPaliPrime(i):
            print(i)
            
paliPrimeNumbers(1,1000)
'''
# Q4. waptp emirp no. in a given range
''' emirp is a no. which is prime n well as itrs reverse also prime, but it should not be palindrome
  eg: 13--> prime, 31--> prime, but 13 is not palindrome
      17--> prime, 71--> prime, but 17 is not palindrome'''

'''
def reverse(n):
    dummy=n
    rev=0
    while dummy>0:
        rem=dummy%10
        rev=rev*10+rem
        dummy//=10
    return rev
    
def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

def isEmirp(n):
    rev=reverse(n)
    if isPrime(n) and isPrime(rev) and rev!=n:
        return True
    else:
        return False

def emirpNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isEmirp(i):
            print(i)

emirpNumbers(1,1000)
'''



