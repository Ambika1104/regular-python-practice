# Q.1 COUNTING DIGITS IN A GIVEN STRING
''' 
s=input()
c=0
for ele in s:
    if ele.isdigit():
        c+=1
print(c)

OR

s=input()
c=0
n='0123456789'
for ele in s:
    if ele in n:
        c+=1
print(c)

OR

s=input()
c=0
for ele in s:
    if ele in '0123456789':
        c+=1
print(c)

ITERATION:--- ex: a01
1.taking string as input
2.assuming string doesn't have any digit in it
3.extracting each element from string
4.checking if that element is digit or not
 Iteration1: taking a and performing isdigit method
             since a is not a digit, the output is false
             c will not store any count in it (c=0)
Iteration2: taking 0 and performing isdigit method
             since 0 is a digit, the output is true
             c will store one count in it (c=1)
Iteration3: taking 1 and performing isdigit method
             since 1 is a digit, the output is true
             c will store one count in it (c=2)
5. at last c value will be printed as 2, c=2.
'''



# COUNTING EVEN NO.S IN A GIVEN SERIES
'''
s=eval(input())
c=0
for ele in s:
    if ele%2==0:
        c+=1
print(c)
'''




 # Q2. COUNTING EVEN NO.S IN A GIVEN STRING: without and with build-in methods
'''
s=input()
c=0
for ele in s:
    if ele in '02468':
        c+=1
print(c)        

OR

s=input()
c=0
for ele in s:
    if ele.isdigit() and int(ele)%2==0:
        c+=1
print(c)

ITERATION:--- ex: a12
1.taking input from the user
2.assuming there is no even no. in the given string
3.extracting each and every element from the given string
4.checking if the element is in '02468' or not
Iteration 1: taking a as element and checking if it lies in '02468' or not
             since a doesn't lies in '02468'
             c will not store any value in it (c=0)
Iteration 1: taking 1 as element and checking if it lies in '02468' or not
             since 1 doesn't lies in '02468'
             c will not store any value in it (c=0)
Iteration 1: taking 2 as element and checking if it lies in '02468' or not
             since 2 lies in '02468'
             c willstore a value in it (c=1)
5.hence c will be priting at last having value 1, c=1             
'''



# Q.3. WAP TO FIND SUM OF DIGITS PRESENT IN A GIVEN STRING
'''
s=input()
sum=0
for ele in s:
    if ele.isdigit():
        sum+=int(ele)
print(sum)

OR

s=input()
add=0
for ele in s:
    if ele in '0123456789':
        add+=int(ele)
print(add)

ITERATION:--- ex: a34
1.taking string as input
2.assuming there is no digit in the given string, so the sum is 0
3.extracting each element from string
4.checking if that element is digit or not
5.if its a digit, it will typcasted to int and its value will be added to the sum value
 Iteration1: taking a and performing isdigit method
             since a is not a digit, the output is false
             sum will not store anything to it (sum=0)
Iteration2: taking 3 and performing isdigit method
             since 3 is a digit, the output is true
             '3' will be typecasted to int 3 and will be added to sum value (sum=0+3=3)
Iteration3:: taking 4 and performing isdigit method
             since 4 is a digit, the output is true
             '4' will be typecasted to int 4 and will be added to sum value (sum=3+4=7)
6. at last sum value will be printed as 7, sum=2.
'''



# Q.4. WAP TO PRINT NUMBER OF SPECIAL CHARACTERS PRESENT IN THE GIVEN STRING
'''
s=input()
sc=0
for ele in s:
    if not ele.isalnum():
        sc+=1
print(sc)

OR

s=input()
sc=0
for ele in s:
    if ele.isalnum()==False:
        sc+=1
print(sc)

ITERATION:--- ex: @#1
1.taking string as input
2.assuming given string doesn't have any special character in it
3.extracting each element from string
4.checking if that element is a special character or not
 Iteration1: taking @ and performing isalnum method
             since @ is not an alphabet or digit, the output is false(its an special character)
             sc will store a count in it (sc=1)
Iteration2: taking # and performing isalnum method
             since # is not an alphabet or digit, the output is false(its an special character)
             sc will store a count in it (sc=2)
Iteration3: taking 1 and performing isalnum method
             since 1 is an alphabet, the output is true
             sc will not store any count in it (sc=2)
5. at last sc value will be printed as 2, sc=2.
'''

































































