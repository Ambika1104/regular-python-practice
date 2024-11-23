#Q1. WAP TO PRINT SUM OF NUMBERS PRESENT IN THE GIVEN LIST

'''
l=eval(input())
sum=0
for ele in l:
    if type(ele)==int:
        sum+=ele
print(sum)

OR

l=eval(input())
sum=0
for ele in l:   
    if isinstance(ele,int):
        sum+=ele
print(sum)


ITERATION:--- ex: [10,20,'hai','1', [2,2] ]
1.taking list as input
2.assuming list is doesn't contain any number DT as its element, sum=0
3.extracting each element from list
4.checking if that element is number type or not, if its a number it will be added to sum
 Iteration1: taking 10 and checking its type
                    since 10 is a numberdatatype
                    sum will add 10 to it (sum=0+10=10)
Iteration2: taking 20 and checking its type
                    since 20 is a number datatype
                    sum will add 20 to it (sum=0+20=20)
Iteration3: taking 'hai' and checking its type
                    since 'hai' is not a number datatype
                    sum will not add 'hai' to it (sum=20)
Iteration4: taking '1' and checking its type
                    since '1' is not a number datatype, its a string of number
                    sum will not add '1' to it (sum=20)
Iteration5: taking [2,2] and checking its type
                    since [2,2] is not a number datatype, its a list
                    sum will not add [2,2] to it (sum=20)
5. at last sum value will be printed as 20, sum=20.
'''


#isinstance(): it is a function which is used for checking if the specified element is a object of specified class of not. The output format is a boolean value.

#Q2. WAP TO PRINT THE FREQUENCY OF EACH AND EVERY CHARACTER PRESENT IN A GIVEN STRING

'''
>>>with count method:
s=input()
for ele in s:
    print(ele,s.count(ele))
    
>>>with set and count method: 
s=input()
for ele in set(s):
    print(ele,s.count(ele))
    
>>>with dictionary and count method:
s=input()
d={}
for ele in s:
    d[ele]=s.count(ele)
print(d)

>>>with dictionary and logic:
s=input()
d={}
for ele in s:
    if ele not in d:
        d[ele]=1
    else:
        d[ele]=d[ele]+1
print(d)

ITERATION:--- ex: 'kookie'
1.taking string as input
2.taking an empty dictionary to store all the element with its frequency of occurance
3.extracting each element from string
4.checking if that element is in dict or not, if its not in dict--> it will be created with value as 1,
   if its already in dict--> then take that ele and update its value and increment it by 1
Iteration1: taking k and checking if its in d or not
                    since k is not in d
                    it will be created with value 1 (d={k:1})
Iteration2: : taking o and checking if its in d or not
                    since o is not in d
                    it will be created with value 1 (d={k:1,o:1})
Iteration3: taking o and checking if its in d or not
                    since o is already in d
                    we will take o and inc its value by 1 and its value will be 2 (d={k:1,o:2})
Iteration4: taking k and checking if its in d or not
                    since k is already in d
                    we will take k and inc its value by 1 and its value will be 2 (d={k:2,o:2})
Iteration5 :taking i and checking if its in d or not
                    since i is not in d
                    it will be created with value 1 (d={k:2,o:2,i:1})
Iteration6 :taking e and checking if its in d or not
                    since e is not in d
                    it will be created with value 1 (d={k:2,o:2,i:1,e:1})
5. at last dict will be printed with element and no.of times its printed (d={k:2,o:2,i:1,e:1})
'''


#RANGE FUNCTION:

'''
o/p: 1,25   25,10    -1,-10     -110,-90

list(range(1,26,1))
list(range(25,9,-1))
list(range(-1,-11,-1))
list(range(-110,-89,1))
'''


#FOR LOOP WITH RANGE:>>>

#Q1. WAP TO PRINT SUM OF 1ST N NUMBERS

'''
n=int(input())
sum=0
for i in range(1,n+1):
      sum+=i
print(sum)

ITERATION:--- ex: 3
1.taking int as input
2. taking sum=0, because if there is no input or the given input is 0
3.extracting each element from 1 to n
4.adding that element to sum
 Iteration1: taking 1 and adding it to sum (sum=0+1=1)
 Iteration2: taking 2 and adding it to sum (sum=1+2=3)
 Iteration3: taking 3 and adding it to sum (sum=2+3=5)
5. at last sum value will be printed as 5, sum=5
'''

#Q2.WAP TO PRINT FACTORIAL OF THE GIVEN NUMBER

'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

ITERATION:--- ex: 3
1.taking int as input
2. taking fact=1, because 0! (0 factorial) is equal=1
3.extracting each element from 1 to n+1 (because n should be included)
4.multiplying that element to fact
 Iteration1: taking 1 and multipying it to fact (fact=1*1=1)
 Iteration2: taking 2 and multipying it to fact (fact=1*2=2)
 Iteration3: taking 3 and multipying it to fact (fact=2*3=6)
5. at last fact value will be printed as 6, fact=6
'''   

#Q3.WAP TO PRINT GIVEN NUMBER IS PERFECT NUMBER OR NOT

'''NOTE:if the given is equals to sun of the divisors
of given numbers then we call it as perfect numbers, eg: 6--> 1,2,3 (1+2+3=6)
6 is perfect number because sum of its divisors is 6'''

'''
n=int(input())
sum=0
for i in range(1,n):
      if n%i==0:
          sum+=i
if sum==n:
      print(f'{n} is a perfect number)
else:
    print(f'{n} is not a perfect number)

 ITERATION:--- ex: 6
1.taking int as input
2. taking sum=0, because the number cannot be a perfect number too
3.extracting each element from 1 to n 
4.checking if n is completely multiplied by how many no.s from 1 to n,
   all those numbers who divides n completely will be added to sum
 Iteration1: taking 1, it divides 6 completely so it will be added to sum (sum=0+1=1)
 Iteration2: taking 2, it divides 6 completely so it will be added to sum (sum=1+2=3)
 Iteration3: taking 3, it divides 6 completely so it will be added to sum (sum=3+3=6)
 Iteration4: taking 4, it doesn't divides 6 completely so it will not be added to sum (sum=6)
 Iteration5: taking 5, it doesn't divides 6 completely so it will not be added to sum (sum=6)
 5. at last sum value will be printed as 6, sum=6
 6. after that sum will be copared to the value of n, if the condition is true...
     that means that no. is a perfect number, and it will get printed (o/p: 6)
'''







Q. WAP TO PRINT ALL PERFECT NO.S IN THE GIVEN RANGE

n=int(input())
sum=0
for i in range(1,n):
    for j in range(1,n):
        if j%i==0:
            sum+=j
    if sum==n:
        print(list(n))
             
      

































        


        
