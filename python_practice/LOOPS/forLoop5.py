# PRACTICE Q. print all no between 200 and 400 whose each digit is a even no.
'''
for n in range(100,401,1):
    s=str(n)
    if s[0] in '02468' and s[1] in '02468' and s[2] in '02468':
        print(n)
        

OR

for n in range(100,401,1):
    s=str(n)
    if int(s[0])%2==0 and int( s[1])%2==0 and int(s[2])%2==0:
        print(n,end=',')
'''   

# Q1. WAPTP MAXIMUM NO. IN A GIVEN LIST AND ITS IP
'''
l=eval(input())
maxno=l[0]
maxip=0
for ip in range(1,len(l)):
    if l[ip]>maxno:
        maxno=l[ip]
        maxip=ip
print(f'maximum no is {maxno}, and its ip is {maxip}')
'''
'''
ITERATION:--- ex: l=[23,11,111]
1.taking list as input
2.asuming that my 1st element is the maximun number, so taking maxno=1st ele in list with maxip as its ip
3.extracting each and element from list starting from ip=1
4.if my next element in list is greater than my max no taken then my new max no will be that number
    taking 23 and considering it as maxno with its maxip=0
 Iteration1: taking 11 and comparing it with the my maxno
                      since the condition is false, maxno and maxip will remain same (maxno=23, maxip=0)
Iteration2: taking 111 and comparing it with the my maxno
                      since the condition is true, maxno and maxip will be updated with new values (maxno=111, maxip=2)
5. at last the maxno with its ip will be get printed ,i.e., maxno=111, maxip=2
'''



# Q2. WAPTP HOW MANY TIMES THE GIVEN SUBSTRING IS PRESENT IN SPECIFIED STRING

'''if we need to extract multiple elts, that means we need to go for slicing... for this we need ip values
...and for ip we need to go for FORLOOP with CDT and range'''

'''
ms=input()
ss=input()
c=0
for ip in range(len(ms)-len(ss)+1):
    if ms[ip:ip+len(ss)]==ss:
        c+=1
print(c)        
'''
'''
ITERATION:--- ex: ms=amb, ss=am
1.taking main string and sub string as input
2.asuming that my ss is not present in the ms , not even once
3.extracting element/s from the ms as per specified ss
4.if my specified ss is present in the ms, then for how many times it is present..it will be counted to c
   (since len of my ss is 2, 2 elements at once will be extracted from ms)
 Iteration1: taking am and comparing it with ss
                     since it satisfies the condition
                     c will be incremented with 1 (c=0+1=1)
Iteration2: taking mb and comparing it with ss
                     since it doen't satisfies the condition
                     c will not be incremented with 1 (c=1)
5. at last c value will be printed as 1, that means 'am' is pesent for once in 'amb' (c=1)
'''



# Q3. WAPTP AN ELEMENT SWAPPED WITH ITS ADJACENT ELEMENT IN FOLLOWING WAY
# EG:  I/P:-- [11,22,33,44,55,66]    O/P:-- [22,11,44,33,66,55]
'''
l=eval(input())
for ip in range(0,len(l),2):
    l[ip],l[ip+1]=l[ip+1],l[ip]
print(l)
'''
'''
ITERATION:--- ex: [11,22,33,44,55,66]
1.taking list as input
2.extracting element from the list till its length with 2 updation value
3.now performing 'swapping variable with each other' method
   ip value will get replaced with its ip+1 value
 Iteration1: taking ip=0 and ip=0+1=1 
                      their value will get swapped with each other [l=22,11,33,44,55,66]
Iteration2:  taking ip=2 and ip=2+1=3 
                      their value will get swapped with each other [l=22,11,44,33,55,66]
Iteration3:  taking ip=4 and ip=4+1=5 
                      their value will get swapped with each other [l=22,11,44,33,66,55]
5. at last swapped list will get printed, i.e., l=[22,11,44,33,66,55]
'''



# Q4. WAPTP AN ELEMENT SWAPPED WITH ITS ADJACENT ELEMENT IN FOLLOWING WAY
# EG:  I/P:-- [11,22,33,44,55,66]    O/P:-- [66,55,44,33,22,11]
'''
l=eval(input())
for ip in range(len(l)//2):
    l[ip],l[-ip-1]=l[-ip-1],l[ip]
print(l)
'''
'''
ITERATION:--- ex: [11,22,33,44,55,66]
1.taking list as input
2.extracting element from the list till half of its length
3.now performing 'swapping variable with each other' method
   ip value will get replaced with its (-ip-1) value
 Iteration1: taking ip=0 and ip=-0-1=-1 
                      their value will get swapped with each other [l=66,22,33,44,55,11]
Iteration2:  taking ip=1 and ip=-1-1=-2 
                      their value will get swapped with each other [l=66,55,33,44,22,11]
Iteration3:  taking ip=2 and ip=-2-1=-3 
                      their value will get swapped with each other [l=66,55,44,33,22,11]
5. at last swapped list will get printed, i.e., l=[66,55,44,33,22,11]
'''






























