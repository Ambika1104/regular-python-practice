''' BUSINESS:-->
B                    C
1lakh   1       1 crore
1lakh   2       1 crore
1lakh   3       1 crore
1lakh   4       1 crore
1lakh   5       1 crore    ---->fraud
1lakh   6       1 crore
1lakh   7       1 crore
1lakh   8       1 crore
1lakh   9       1 crore
1lakh   10     1 crore

1. STOP REMAINING  ALL BUSINESS--> TERMINATE REMAINING LOOP EXECUTION:BREAK
2. STOP ONLY THAT BUSINESS---> SKIP CURRENT ITERATION: CONTINUE
'''

#SPECIAL STATEMENTS OF PYTHON:

#BREAK: break is used for terminating the execution of loop. 

# CASE 1: first performing operation and then writing breaking condition
# OP: 1 2 3 4 5
'''for n in range(1,11):
    print(i)
    if i==5:
        break
    
i=1
while i<11:
    print(i)
    if i==5:
        break
    i+=1'''

'''ITERATION:
1. first value will be printed and then condition will be checked
2. if the conditions will be true break will terminate the other statements and come out of the loop
3. iteration1: i=1, 1 is printed, condition is false, i value is incremented, again entering the loop
    iteration2: i=2, 2 is printed, condition is false, i value is incremented, again entering the loop
    iteration3: i=3, 3 is printed, condition is false, i value is incremented, again entering the loop
    iteration4: i=4, 4 is printed, condition is false, i value is incremented, again entering the loop
    iteration5: i=5, 5 is printed, condition is true, break will terminate the loop
4. at last these values of i will be printed: i= 1 2 3 4 5 '''

# CASE 2: first writing breaking condition and then performing operation
# OP: 1 2 3 4 
'''for i in range(1,11):
    if i==5:
        break
    print(i)

i=1
while i<11:
     if i==5:
        break
    print(i)
    i+=1 '''

'''ITERATION:
1.  first condition will be checked and then value will be printed
2. if the conditions will be true break will terminate the other statements and come out of the loop
3. iteration1: i=1, condition is false, 1 is printed, i value is incremented, again entering the loop
    iteration2: i=2,  condition is false, 2 is printed, i value is incremented, again entering the loop
    iteration3: i=3, condition is false, 3 is printed, i value is incremented, again entering the loop
    iteration4: i=4, condition is false, 4 is printed, i value is incremented, again entering the loop
    iteration5: i=5, condition is true, 5 is not printed, break will terminate the loop
4. at last these values of i will be printed: i= 1 2 3 4 '''

#ERROR for continue with for and while: printing for all values of i in for loop and  infifnte looping with checking i==5 condition in wnile
'''for i in range(1,11): #op: 1 to 10
    print(i)                       #printing values of i
    if i==5:                      #checking condition but i=5 is already printed
        continue
    

i=1 # op: 1 to 4 ...in loop with 5
while i<11:
     if i==5:                  #checking condition
        continue
     print(i)                  # pritining till i=4, getting in loop with i=5, bcoz when i=5,continue will skip that iteration...
     i+=1                    #increment statement is also skipped, the value i will always be 5, and it will get stuck in loop for cheking again n again for i=5 (no incremention)'''
     
#CONTINUE: continue is used to skip the current execution of loop
'''NOTE: we can use break n continue only with the loops
                with continue we cannot perform operation, 1st we need condition checking'''


#first writing skipping condition and then performing operation
# OP: 1 2 3 4 6 7 8 9 10

'''for i in range(1,11):
    if i==5:
        continue
    print(i)

i=1
while i<11:
     if i==5:
         i+=1
        continue
     print(i)
     i+=1'''

'''ITERATION:
1. first condition will be checked and then value will be printed
2. if the conditions will be true continue will skip that current iteration and will continue with next iterations
3. iteration1: i=1, condition is false, 1 is printed, i value is incremented, again entering the loop
    iteration2: i=2,  condition is false, 2 is printed, i value is incremented, again entering the loop
    iteration3: i=3, condition is false, 3 is printed, i value is incremented, again entering the loop
    iteration4: i=4, condition is false, 4 is printed, i value is incremented, again entering the loop
    iteration5: i=5, condition is true, 5 is not printed, continue will go for next iteration, i value is incremented
    iteration6: i=6, condition is false, 6 is printed, i value is incremented, again entering the loop
    ...
    iteration10: i=10, condition is false, 10 is printed, i value is incremented, again entering the loop
    i=10, condition not satisified, nto entering the for/while block
4. at last these values of i will be printed: i= 1 2 3 4 6 7 8 9 10 '''


#PASS:
'''1. pass is used for creating empty blocks (without any semantical error)
   2. pass acts as the placeholder for statements which are to be written in future
   3. pass can be utilized in loops, conditions, in functions as well as in classes

Examples:

def finction():
    pass

if 10>1:
    pass

for i in range(1,10):
    pass
    
class A:
    pass
'''
# FOR ELSE BLOCK:
# 1.if loop is terminated else block will not get executed (if break, no else)
# 2.if loop is not terminted else block will get executed    (if no break else)

''' SYNTAX:
for var in range():
    statements
    if condition:
        break
else:
    statements of else block
    

Example:
-----> for termnating of loop

for i in range(1,11):   #op: 1 2 3 4 5
    print(i)
    if i==5:
        break
else:
    print('else block')

ITERATION:
1. first value will be printed and then condition will be checked
2. if the conditions will be true break will terminate the other statements and come out of the loop
3. if the loop is terminated, else block will not get executed. if loop doesn't terminate, else will get executed
4. iteration1: i=1, 1 is printed, condition is false, i value is incremented, again entering the loop
    iteration2: i=2, 2 is printed, condition is false, i value is incremented, again entering the loop
    iteration3: i=3, 3 is printed, condition is false, i value is incremented, again entering the loop
    iteration4: i=4, 4 is printed, condition is false, i value is incremented, again entering the loop
    iteration5: i=5, 5 is printed, condition is true, break will terminate the loop, else block will not get executed
5. at last these values of i will be printed: i= 1 2 3 4 5
    

-----> for not termnating of loop

for i in range(1,11):   #op: 1 to 10 + else block
    print(i)
    if i==15:
        break
else:
    print('else block')

ITERATION:
1. first value will be printed and then condition will be checked
2. if the conditions will be true break will terminate the other statements and come out of the loop
3. if the loop is terminated, else block will not get executed. if loop doesn't terminate, else will get executed
4. iteration1: i=1, 1 is printed, condition is false, i value is incremented, again entering the loop
    iteration2: i=2, 2 is printed, condition is false, i value is incremented, again entering the loop
    iteration3: i=3, 3 is printed, condition is false, i value is incremented, again entering the loop
    iteration4: i=4, 4 is printed, condition is false, i value is incremented, again entering the loop
    ...
    iteration10: i=10, 10 is printed, condition is false, i value is incremented
    i=10, condition not satisfied, will not enter into for block
5. no where the whole execution of the will breaking condition is true, therefore the lopp is not terminated
     that means else block will also get executed
6. at last these values of i will be printed: i= 1 2 3 4 5 6 7 8 9 10 + else block
'''

#WHILE ELSE BLOCK:
# 1.if loop is terminated else block will not get executed (if break, no else)
 # 2.if loop is not terminted else block will get executed    (if no break else)
'''
SYNTAX:
while condition:
    statements
    if condition:
        break
else:
    statements of else block

Example:
-----> for termnating of loop

i=1
while i<11:
    print(i)
    if i==5:
        break
    i+=1
else:
    print('inside else block')

ITERATION:
1. first value will be printed and then condition will be checked
2. if the conditions will be true break will terminate the other statements and come out of the loop
3. if the loop is terminated, else block will not get executed. if loop doesn't terminate, else will get executed
4. iteration1: i=1, 1 is printed, condition is false, i value is incremented, again entering the loop
    iteration2: i=2, 2 is printed, condition is false, i value is incremented, again entering the loop
    iteration3: i=3, 3 is printed, condition is false, i value is incremented, again entering the loop
    iteration4: i=4, 4 is printed, condition is false, i value is incremented, again entering the loop
    iteration5: i=5, 5 is printed, condition is true, break will terminate the loop, else block will not get executed
5. at last these values of i will be printed: i= 1 2 3 4 5


-----> for not termnating of loop

i=1
while i<11:
    print(i)
    if i==15:
        break
    i+=1
else:
    print('inside else block')


ITERATION:
1. first value will be printed and then condition will be checked
2. if the conditions will be true break will terminate the other statements and come out of the loop
3. if the loop is terminated, else block will not get executed. if loop doesn't terminate, else will get executed
4. iteration1: i=1, 1 is printed, condition is false, i value is incremented, again entering the loop
    iteration2: i=2, 2 is printed, condition is false, i value is incremented, again entering the loop
    iteration3: i=3, 3 is printed, condition is false, i value is incremented, again entering the loop
    iteration4: i=4, 4 is printed, condition is false, i value is incremented, again entering the loop
    ...
    iteration10: i=10, 10 is printed, condition is false, i value is incremented
    i=10, condition not satisfied, will not enter into while block
5. no where the whole execution of the will breaking condition is true, therefore the lopp is not terminated
     that means else block will also get executed
6. at last these values of i will be printed: i= 1 2 3 4 5 6 7 8 9 10 + else block '''
