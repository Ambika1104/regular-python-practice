# Q1. WAPTP TO CHECK THE GIVEN NO. IS PRIME OR NOT: using while-else
'''prime---> need to be greater than 1 and divisible by only 1and itself'''

'''
n=int(input())
i=2
if n>1:
    while i<(n//2)+1:                                                                                 #n//2+1---> 10//2=5,    i<5..it will only check till less than 5...so +1 ia need OR give i<=n//2 (= sign)
        if n%i==0:
            print(f'{n} is not a prime number')
            break
        i+=1
    else:
        print(f'{n} is a prime number')                                                #when loop is not terminated, else block will get executed
else:
    print(f'{n} is not a prime number')
'''
'''
ITERATION:
1.taking input as int from the user
2.intiallizing i=2 (bcoz 1 is factor of all no.s)
3.taking n>1, bcoz 1 and no.s below it, are not prime no.s (prime no.s starts from 2)
4. checking if n is divisible by any no. between 2 and half of its value or not
5. if n is divisible by any no. between 2 and half of its value, then its not a prime no and it will be printed as 'its not a prime no' and loop will terminate
6.if n is not divisible by any no. between 2 and half of its value, then loop will keep on running...
   since it will not terminate anywhere then else block of while-else will be excuted as 'its a prime no'
7. if the no. is 1 or smaller than one then if block condition is not satisfied and else block will be executed as 'its not a prime no'
8. if the n=2 or 3, else block of while-else will be executed (while loop will not run for 2,3... control will directly goto else block of while-else)

9. eg: 5
    7>1 -->true, entered into if block
    now checking if 7 is divisible by 2,3
    7%2==0    false
    7%3==0    false
    condition is false
    no termination of while block
    else block of while-else will be executed
    7 is a prime no

    eg: 6
    6>1 --> true, enters into if block
    now checking if 6 is divisible by 2,3 or not
    since 2 divides 6,  enters into if block
    '6 is not prime no' will get printed
    loop will terminate
'''    

# Q2. WAPTP TO CHECK THE GIVEN NO. IS PRIME OR NOT: using for-else

'''
n=int(input())
if n>1:
    for i in range(2,(n//2)+1):                                                          #for 2 & 3-->it will check from 2 to 2, loop will not work..it will automatically go to 'else' part of for-else, 
        if n%i==0:                                                                                #& print that its a prime no
            print(f'{n} is not a prime number')
            break
    else:
        print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')
'''

'''
ITERATION:
1.taking input as int from the user
2.taking n>1, bcoz 1 and no.s below it, are not prime no.s (prime no.s starts from 2)
3.starting the for loop with 2, till half of its value
4. checking if n is divisible by any no. between 2 and half of its value or not
5. if n is divisible by any no between 2 and half of its value, then its not a prime no and it will be printed as 'its not a prime no' and loop will terminate
6.if n is not divisible by any no. between 2 and half of its value, then loop will keep on running...
   since it will not terminate anywhere then else block of for-else will be excuted as 'its a prime no'
7. if the no. is 1 or smaller than 1 then if block condition is not satisfied and else block will be executed as 'its not a prime no'
8. if the n=2 or 3, else block of for-else will be executed (for loop will not run for 2,3... control will directly goto else block of for-else)
9. eg: 5
    7>1 -->true, entered into if block
    now checking if 7 is divisible by 2,3
    7%2==0    false
    7%3==0    false
    condition is false
    no termination of while block
    else block of for-else will be executed
    7 is a prime no

    eg: 6
    6>1 --> true, enters into if block
    now checking if 6 is divisible by 2,3 or not
    since 2 divides 6,  enters into if block
    '6 is not prime no' will get printed
    loop will terminate
 '''

# Q3. WAP TO REVERSE A GIVEN STRING WITHOUT USING SLICING
# with slicing
'''
s=input()
print(s[::-1])
'''

# with normal approach
'''
s=input() 
rev=''
for ele in s:
    rev=ele+rev
print(rev)
'''
'''
ITERATION: eg: amb
1.taking string as input from user
2.taking an empty string as rev (to store the reverse of original string)
3. extracting each and every element from the string
4. storing ectracting element before reverse in rev(empty string)
 iteration1: taking a and adding it to rev (op: rev=a)
 iteration2: taking m and adding it to rev (op: rev=ele+rev --> rev=m+a=ma)
 iteration3: taking b and adding it to rev (op: rev=ele+rev=b+ma=bma)
5.finally we get the reversed string : bma
'''

# with index positions
'''
s=input()
rev=''
for ip in range(-1,-(len(s)+1),-1):
    rev+=s[ip]
print(rev)
'''
    
#actual programming:
'''1. nested loop or one loop
2. for loop or while loop
3. for loop with cdt, range or cdt+range'''
