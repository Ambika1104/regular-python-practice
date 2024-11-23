#WAPTP THE SUM OF INDIVIDUAL DIGITS OF A GIVEN NUMBER
         #how to extract each digit from a no, without using typecasting: 1. get the remainder    2. reduce the no.
'''
n=int(input())
dummy=n
summ=0
while dummy>0:
    rem=dummy%10  # getting the remainder
    dummy//=10           # reducing the number
    summ+=rem
print(summ)
'''
'''
ITERATION:
1. taking input from user eg:123
2.storing it in a dummy variable
3. processing the dummy variable until it is 0
      a. getting the last no. of the digit by performing modulus operation
      b. now reducing the no. using floor division and stroing it again in dummy variable
      c. stroing the rem into summ
      iteration 1: rem=123%10=3
                            dummy=123//10=12
                            summ=0+3=3
     iteration 2: rem=12%10=2
                            dummy=12//10=1
                            summ=3+2=5
     iteration 3: rem=1%10=1
                            dummy=1//10=0
                            summ=5+1=6                          
4. at last printing the value of summ
'''

#NOTE: sometimes we need 'n' to be used again, so we go for a dummy variable and all processing is done on it only. in the above question we don't need a dummy variable.

# Q2. WAPTP THE SUM OF INDIVIDUAL DIGITS OF A GIVEN NO IS EVEN OR NOT
'''
n=int(input())
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem
if summ%2==0:
    print('summ is even')
else:
    print('summ is not even')
'''
'''
ITERATION:
1. taking input from user eg:123
2.storing it in a dummy variable
3.taking summ=0, the no entered by user maybe 0
4.processing the dummy variable until it is 0, extracting each and every digit from the given number
      a. getting the last no. of the digit by performing modulus operation
      b. now reducing the no. using floor division and stroing it again in dummy variable
      c. stroing the rem into summ
      iteration 1: rem=123%10=3
                            dummy=123//10=12
                            summ=0+3=3
     iteration 2: rem=12%10=2
                            dummy=12//10=1
                            summ=3+2=5
     iteration 3: rem=1%10=1
                            dummy=1//10=0
                            summ=5+1=6                          
5. at last, checking the value of summ is even or not... summ=6=--> its an even no, op is 'summ is even'
'''

#Q3. WAPTP GIVEN NO. IS ARMSTRONG NO. OR NOT
'''ARMSTRONG NO: if the no is equals to the sum of individual digits to the power of no of digits present in it. eg: 153=1**3 + 5**3 + 3**3'''

'''
n=int(input())
dummy=n
summ=0
s=str(n)
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem**len(s)
if summ==n:
    print(f'{n} is a armstrong no')
else:
    print(f'{n} is not a armstrong no')
'''
'''OR'''

'''
n=int(input())
dummy=n
summ=0
l=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem**l
if summ==n:
    print(f'{n} is a armstrong no')
else:
    print(f'{n} is not a armstrong no')
'''
'''
ITERATION:
1. taking input from user eg:153
2.storing it in a dummy variable
3. converting the no. into string and storing its length into l
4.taking summ=0, the no entered by user maybe 0
5.processing the dummy variable until it is 0, extracting each and every digit from the given number
      a. getting the last no. of the digit by performing modulus operation
      b. now reducing the no. using floor division and stroing it again in dummy variable
      c. stroing the rem with power as l's value (l=3)
      iteration 1: rem=153%10=3
                            dummy=153//10=15
                            summ=0+3**3=27
     iteration 2: rem=15%10=5
                            dummy=15//10=1
                            summ=27+5**3=27+125=152
     iteration 3: rem=1%10=1
                            dummy=1//10=0
                            summ=152+1**3=152+1=153                          
6. at last, checking the value of summ is equal to n or not, since summ=n, i.e., 153=153...n=153 is an armstrong number.
'''

#WITHOUT TYPECASTING-->
'''
n=int(input())
L=0
dummy1=n
while dummy1>0:
    rem=dummy1%10
    dummy1//=10
    L+=1
    
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem**L
if summ==n:
    print(f'{n} is an armstrong no')
else:
    print(f'{n} is not an armstrong no')
'''

# Q4. WAPTP GIVEN NO. IS DISARIUM NO OR NOT
'''DISARIUM NO: if the no is equals to the sum of the individual digits to the power of its positions. eg: 135=1**1+3**2+5**3'''

'''
n=int(input())
dummy=n
summ=0
l=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem**l
    l-=1
if summ==n:
    print(f'{n} is a disarium no')
else:
    print(f'{n} is not a disarium no')
'''
'''
ITERATION:
1. taking input from user eg:135
2.storing it in a dummy variable
3. converting the no. into string and storing its length into l
4.taking summ=0, the no entered by user maybe 0
5.processing the dummy variable until it is 0, extracting each and every digit from the given number
      a. getting the last no. of the digit by performing modulus operation
      b. now reducing the no. using floor division and stroing it again in dummy variable
      c. stroing the rem with power as l's value (l=3) and reducing the value of l by 1 in every iteration (i.e., l-=1)
      iteration 1: rem=135%10=5
                            dummy=135//10=13
                            summ=0+5**3=125
     iteration 2: rem=13%10=3
                            dummy=13//10=1
                            summ=125+3**2=125+9=134
     iteration 3: rem=1%10=1
                            dummy=1//10=0
                            summ=134+1**1=134+1=135                         
6. at last, checking the value of summ is equal to n or not, since summ=n, i.e., 135=135...n=135 is a disarium number.
'''


# Q5. WAPTP GIVEN NO IS HARSHAD NO (niven no) OR NOT
'''HARSHAD NO: an integer that is divisible by the sum of its digits. eg: 21=2+1=3   21%3=0'''

'''
n=int(input())
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem
if n%summ==0:
    print(f'{n} is a harshad no')
else:
    print(f'{n} is not a harshad no')
'''
'''
ITERATION:
1. taking input from user eg:21
2.storing it in a dummy variable
3.taking summ=0, the no entered by user maybe 0
4.processing the dummy variable until it is 0, extracting each and every digit from the given number
      a. getting the last no. of the digit by performing modulus operation
      b. now reducing the no. using floor division and stroing it again in dummy variable
      c. stroing the rem with power as l's value (l=3) and reducing the value of l by 1 in every iteration (i.e., l-=1)
      iteration 1: rem=21%10=1
                            dummy=21//10=2
                            summ=0+1=1
     iteration 2: rem=2%10=2
                            dummy=2//10=0
                            summ=1+2=3                  
5. at last, checking the value of summ is dividing n completely or not... since 21%3=0, there n=21 is a harshad number.
'''





























