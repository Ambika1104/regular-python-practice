# Q1. FINDING THE LENGTH OF THE GIVEN STRING
'''
s=input()
c=0
for k in s:
    c+=1
print(f'the length of {s} is',c)

ITERATION:--- ex: s=amb
1.taking string as input
2.assuming string is empty
3.if the string in not empty, extracting each element from string
4.for each element extracted, c value will be incremented
 Iteration1: taking 1st element 'a'
             for this, c will be incremented by one (c=1)
Iteration2: taking 2nd element 'm'
             for this, c will again be incremented by one (c=2)
Iteration3: taking 3rd element 'b'
             for this, c will again be incremented by one (c=3)
5.at last, c value will be printed as 3, c=3
since 'amb' contains three elements in it, its length is 3
'''




# Q2. FINDING SUBSTRING IN MAIN STRING
'''
s=input()
ss=input()
c=0
for ele in s:
    if ele==ss:
        c+=1
print(f'the no. of times {ss} is present in {s} is',c)

ITERATION:--- ex: s:amb, ss=a
1.taking string as input
2.taking substring as input from the user
3.assuming string doesn't contain given substring in it
4.extracting each element from string
5.checking if that element is equal to substring or not
 Iteration1: taking a and checking if lhs is equal to rhs or not
             since a is equal to a
             c will be incremented by one (c=1)
Iteration2: taking m and checking if lhs is equal to rhs or not
             since a is not equal to m
             c will not be incremented by one (c=1)
Iteration3: taking b and checking if lhs is equal to rhs or not
             since a is not equal to b
             c will not be incremented by one (c=1)
6. at last c value will be printed as 1, c=1.
'''




# Q3. FINDING VOWELS IN A STRING
'''
s=input()
s1=s.lower()
v={'a','e','i','o','u'}
c=0
for ele in s1:
    if ele in v:
        c+=1
print(c)

ITERATION:--- ex: s=amb
1.taking string as input
2.assuming string doesn't contain any vowels in it
3.extracting each element from string
4.checking if that element is present in v or not
 Iteration1: taking a and checking if its in v or not
             since a lies in v as one of its element
             c will be incremented by one (c=1)
Iteration2: taking m and checking if its in v or not
             since m doesn't lies in v as one of its element
             c will not be incremented by one (c=1)
Iteration3: taking b and checking if its in v or not
             since b doesn't lies in v as one of its element
             c will not be incremented by one (c=1)
5.at last, c value will be printed as 1, c=1
since 'amb' contains only one vowel in it, i.e., 'a'
'''



# Q4. FINDING CONSONANTS IN GIVEN STRING
'''
s=input().lower()
c=0
v=['a','e','i','o','u']
n=['0','1','2','3','4','5','6','7','8','9']
for ele in s:
    if ele not in n:
        if ele not in v:
            c+=1
print(f'the no.of consonants in {s} is',c)            

OR

s=input().lower()
#v=['a','e','i','o','u']
v='aeiou'
c=0
for ele in s:
    if ele.isalpha() and ele not in v:
        c+=1
print(c)

ITERATION:--- ex: s=amb
1.taking string as input and coberting it into lowercase
2.assuming string doesn't have any consonants in it
3.extracting each and every element from it
4.checking if the element is an alphabet but not an vowel
 Iteration1: taking a and checking if its an alphabet or not, since its an alphabet, the 1st condition is true
             next chcking if it lies in v or not, a lies in v, so 2nd condition is false
             c will not be incremented by one (c=0)
Iteration2: taking m and checking if its an alphabet or not, since its an alphabet, the 1st condition is true
            next chcking if it lies in v or not, m  doesn't lies in v, so 2nd condition is also true
            c will be incremented by one (c=1)
Iteration3: : taking b and checking if its an alphabet or not, since its an alphabet, the 1st condition is true
            next chcking if it lies in v or not, m  doesn't lies in v, so 2nd condition is also true
            c will be incremented by one (c=2)             
5.at last, c value will be printed as 2, c=2
since 'amb' contains two consonants in it, c=2
'''



# PRACTICE QUESTIONS
'''
Q1. COUNTING EVEN AND ODD NO.S IN THE GIVEN SERIES
s=eval(input())
ce=0
co=0
for ele in s:
    if ele%2==0:
        ce+=1
    else:
        co+=1
print(' count of even no. is:',ce)
print('count of odd no. is:',co)



Q2. FINDING DISTINCT ELEMENT IN AN ARRAY
s=eval(input())
dis=list()
for ele in s:
    if not ele in dis:
        dis.append(ele)
print(dis)

OR

s=eval(input())
dis=set()
for ele in s:
    if not ele in dis:
        dis.add(ele)
print(dis)


        
Q3. WAP TO PRINT NUMBER OF DIGITS, ALPHABETS AND SPECIAL CHARACTERS IN IT
s=input()
cd=0
ca=0
cs=0
for ele in s:
    if ele.isalpha():
        ca+=1
    elif ele.isdigit():
        cd+=1
    else:
        cs+=1
print('the count of alphabets are:',ca)
print('the count of digits are:',cd)
print('the count of special char are:',cs)

'''
