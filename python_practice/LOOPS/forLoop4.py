# Q1. WAPTP EVEN NUMBERS IN A GIVEN RANGE

'''
LL=int(input())
UL=int(input())
for n in range(LL,UL+1):
    if n%2==0:
        print(n)

OR

#reducing the looping by half, complexity decreases and efficiency increases

LL=int(input())
UL=int(input())
if LL%2!=0:
    LL=LL+1
for n in range(LL,UL+1,2):
    print(n)

 ITERATION:--- ex: LL=5, UL=10
1.taking int as input for lower limit and upper limit
2.checking if the lower limit is a even no. or not, if not then lower limit will be incremented by 1
3.extracting each number between  lower limit and upper limit (included)
 Iteration1: taking 6 and checking its even or not
                     since 6 is a even no., it will get printed (o/p: 6)
Iteration2: taking 7 and checking its even or not
                     since 7 is not a even no., it will not get printed (o/p: 6)
Iteration3: taking 8 and checking its even or not
                     since 8 is a even no., it will get printed (o/p: 6,8)
Iteration4: taking 9 and checking its even or not
                    since 9 is not a even no., it will not get printed (o/p: 6,8)
Iteration5:  taking 10 and checking its even or not
                    since 10 is a even no., it will get printed (o/p: 6,8,10)
4. at last even digits between 5 and 10 will get printed, i.e., 6,8,10
'''

#FOR WITH RANGE AND CDT
'''
s='hello'
   for ip in range(len(s)):
       print(ip,s[ip])
 '''
# Q1. WAPTP  INDEX POSITIONS OF ALL THE VOWELS PRESENT IN GIVEN STRING

'''
s=input()
for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
     print(ip)

 ITERATION:--- ex: s=ambi
1.taking string as an input
2.extracting each and every element from string (from 0 to length of the string)
3. checking if that element is a vowel or not
 Iteration1:taking a and checking if its a vowel or not
                    since the condition is true, its ip will get printed (o/p: 0)
Iteration2: taking m and checking if its a vowel or not
                    since the condition is false, its ip will not get printed (o/p: 0)
Iteration3: taking b and checking if its a vowel or not
                    since the condition is false, its ip will not get printed (o/p: 0)
Iteration4: taking i and checking if its a vowel or not
                    since the condition is true, its ip will get printed (o/p: 0,3)
4. at last vowels's ip will get printed (o/p: 0,3)
'''

#Q2. WAPTP THE ELEMENTS WHICH ARE PRESENT IN EVEN INDEX POSITIONS

'''
s=input()
for ip in range(len(s)):
    if ip%2==0:
        print(s[ip])

OR

s=input()
for ip in range(0,len(s),2):
    print(s[ip])

ITERATION:--- ex: s=amb
1.taking string as an input
2.extracting each and every element from string (from 0 to length of the string)
3. checking if that element is present at even ip or not, is its present then it will get printed
 Iteration1:taking a and checking if its present at  even ip or not
                    since the condition is true, a will get printed (o/p: a)
Iteration2: taking m and checking if its present at  even ip or not
                    since the condition is false, a will not get printed (o/p: a)
Iteration3: taking b and checking if its present at  even ip or not
                    since the condition is true, a will get printed (o/p: a,b)
4. at last elements at even ip will be printed (o/p: a,b)
'''

# Q3.FIND THE SUM OF INDEX POSTIONS OF THE DIGITS PRESENT IN THE GIVEN STRING

'''
s=input()
sum=0
for ip in range(0,len(s)):
    if s[ip].isdigit():
        sum+=ip
print(sum)

OR

s=input()
sum=0
for ip in range(0,len(s)):
    if s[ip] in '0123456789':
        sum+=ip
print(sum)

ITERATION:--- ex: s=a11
1.taking string as an input
2. taking sum=0, because the string may not contain any digit into it
2.extracting each and every element from string (from 0 to length of the string)
3. checking if that element is digit or not, is its digit...its ip will be added to sum
 Iteration1:taking a and checking if its digit or not
                    since the condition is false, a's ip will not be added to sum (sum=0)
Iteration2: :taking 1 and checking if its digit or not
                    since the condition is true, 1's ip will be added to sum (sum=0+1=1)
Iteration3: taking 1 and checking if its digit or not
                    since the condition is true, 1's ip will be added to sum (sum=1+2=3)
4. at last sum value will be printed (sum=3)
'''

# Q4. FIND THE SUM OF INDEX POSITIONS OF EVEN NUMBERS

'''
s=input()
sum=0
for ip in range(0,len(s)):
    if s[ip].isdigit() and int(s[ip])%2==0:
        sum+=ip
print(sum)

OR

s=input()
sum=0
for ip in range(len(s)):
    if s[ip] in '02468':
        sum+=ip
print(sum)

ITERATION:--- ex: s='234'
1.taking string as an input
2. taking sum=0, because the string may not contain any even no. in it
3.extracting each and every element from string (from 0 to length of the string)
4. checking if that element is an even digit or not, is its an even digit...its ip will be added to sum
 Iteration1:taking 2 (ip=0) and checking if its an even no. or not
                    since the condition is true, it's ip will be added to sum (sum=0+0=0)
Iteration2: :taking 3  (ip=1)  and checking if its an even no. or not
                    since the condition is false, it's ip will not be added to sum (sum=0)
Iteration3: :taking 4  (ip=2)  and checking if its an even no. or not
                    since the condition is true, it's ip will be added to sum (sum=0=2=2)
5. at last sum value will be printed (sum=2)
'''

#Q5. WAP TO FIND THE SUM OF EVEN DIGITS PRESENT IN EVEN INDEX POSITIONS (even ip having even digit, sum=digit)

'''
s=input()
sum=0
for ip in range(0,len(s)):
    if ip%2==0 and s[ip] in '02468':
        sum+=int(s[ip])
print(sum)

OR

s=input()
sum=0
for ip in range(0,len(s),2):
    if s[ip] in '02468':
        sum+=int(s[ip])
print(sum)

ITERATION:--- ex: s='134'
1.taking string as an input
2. taking sum=0, because in the string even ip may not contain any even no.s
3.extracting each and every element from string (from 0 to length of the string)
4. checking if at even ip the element is even or not, if its an even no. then it will added to sum
 Iteration1:taking 1  (ip=0)  and checking if its at even ip or not and if its an even no or not
                    since the condition is false, the element will not be added to sum (sum=0)
Iteration2: :taking 3  (ip=1)  and checking if its at even ip or not and if its an even no or not
                    since the condition is false, the element will not be added to sum (sum=0)
Iteration3: :taking 4  (ip=2)  and checking if its at even ip or not and if its an even no or not
                    since the condition is true, the element will be added to sum (sum=0+4=4)
5. at last sum value will be printed (sum=4)
'''



#HOMEWORK>>>

# 1. WAP TO FIND SUM OF EVEN IP OF EVEN DIGITS  (even ip having even no, sum=ip)
'''
s=input()
sum=0
for ip in range(0,len(s),2):
    if s[ip] in '02468':
        sum+=ip
print(sum)

ITERATION:--- ex: s='134'
1.taking string as an input
2. taking sum=0, because in the string even ip may not contain any even no.s
3.extracting each and every element from string (from 0 to length of the string)
4. checking if at even ip the element is even or not, its its an even no. then its ip will be added to sum
 Iteration1:taking 1  (ip=0) and checking if its at even ip or not and if its an even no or not
                    since the condition is false, its ip will not be added to sum (sum=0)
Iteration2: :taking 3  (ip=1) and checking if its at even ip or not and if its an even no or not
                    since the condition is false, its ip will not be added to sum (sum=0)
Iteration3: taking 4  (ip=2)  and checking if its at even ip or not and if its an even no or not
                    since the condition is true, its ip will be added to sum (sum=0+2=2)
5. at last sum value will be printed (sum=2)
'''

# 2. WAP TO FIND SUM OF ODD IP OF EVEN DIGITS    (odd ip having even no, sum=ip)
'''
s=input()
sum=0
for ip in range(1,len(s),2):
    if s[ip] in '02468':
        sum+=ip
print(sum)

ITERATION:--- ex: s='345'
1.taking string as an input
2. taking sum=0, because in the string odd ip may not contain any even no.s
3.extracting each and every element from string (from 0 to length of the string)
4. checking if at odd ip  the element is an even no. or not if yes, then its ip will be added to sum
 Iteration1:taking 3  (ip=0) and checking if its at odd ip or not and if its an even no or not
                    since the condition is false, its ip will not be added to sum (sum=0)
Iteration2: :taking 4  (ip=1) and checking if its at odd ip or not and if its an even no or not
                    since the condition is true, its ip will be added to sum (sum=0+1=1)
Iteration3: taking 5  (ip=2)  and checking if its at odd ip or not and if its an even no or not
                    since the condition is false, its ip will not be added to sum (sum=1)
5. at last sum value will be printed (sum=1)
'''

# 3. WAP TO FIND SUM OF ODD DIGITS OF ODD IP      (odd digits on odd ip, sum=digit)
'''
s=input()
sum=0
for ip in range(1,len(s),2):
    if s[ip] in '13579':
        sum+=int(s[ip])
print(sum)

ITERATION:--- ex: s='134'
1.taking string as an input
2. taking sum=0, because in the string odd ip may not contain any odd no.s
3.extracting each and every element from string (from 1 to length of the string having updation value=2)
4. checking if at odd ip the element is odd or not, if its an odd no. then it will added to sum
 Iteration1:taking 1  (ip=0)  and checking if its at odd ip or not and if its anodd no or not
                    since the condition is false, the element will not be added to sum (sum=0)
Iteration2: :taking 3  (ip=1)  and checking if its at odd ip or not and if its anodd no or not
                    since the condition is true, the element will be added to sum (sum=0+3=3)
Iteration3: taking 4  (ip=2)  and checking if its at odd ip or not and if its an odd no or not
                    since the condition is false, the element will not be added to sum (sum=3)
5. at last sum value will be printed (sum=3)
'''



































