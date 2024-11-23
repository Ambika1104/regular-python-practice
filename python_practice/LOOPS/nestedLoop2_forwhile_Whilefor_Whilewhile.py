# FOR LOOP INSIDE WHILE LOOP: ------->

# 1. running the loop completely
'''
i=1
while i<6:                            #1,1 to 5,5
    for j in range(1,6):
        print(i,j)
    i+=1
'''
# 2. breaking the inner loop with inner loop value
'''
i=1
while i<6:                            #1,1 to 1,3   &   2,1 to 2,3.......5,1 to 5,3
    for j in range(1,6):
        print(i,j)
        if j==3:
            break
    i+=1
'''
# 3. breaking the inner loop with outer loop value
'''
i=1
while i<6:                            #1,1 to 1,5   &   2,1 to 2,5    & 3,1   &   4,1 to 4,5    &   5,1 to 5,3
    for j in range(1,6):
        print(i,j)
        if i==3:
            break
    i+=1
'''
# 4. breaking the outer loop with outer loop value
#case(i): first performing operation then breaking condition
'''
i=1
while i<6:                            #1,1 to 3,5
    for j in range(1,6):
        print(i,j)
    if i==3:
            break   
    i+=1
'''
#case(i): first performing operation then breaking condition
'''
i=1
while i<6:                            #1,1 to 2,5
    if i==3:
            break
    for j in range(1,6):
        print(i,j)
    i+=1
'''
# 5. breaking the outer loop with inner loop value
'''
i=1
while i<6:                            #1,1 to 1,5
    for j in range(1,6):
        print(i,j)
    if j==5:
        break
    i+=1
'''


# WHILE LOOP INSIDE FOR LOOP:------>

#1. running the loop completely
'''
for i in range(1,6):  #all
    j=1
    while j<6:
        print(i,j)
        j+=1
'''
# 2.breaking the inner loop with inner loop value
'''
for i in range(1,6):     #1,1 to 1,3   &  2,1 to 2,3....5,1 to 5,3
    j=1
    while j<6:
        print(i,j)
        if j==3:
            break
        j+=1
'''
# 3.breaking the inner loop with outer loop value
'''
for i in range(1,6):   #1,1 to 1,5   &  2,1 to 2,5  &  3,1  &  4,1 to 4,5  &  5,1 to 5,5
    j=1
    while j<6:
        print(i,j)
        if i==3:
            break
        j+=1
'''
# 4.breaking the outer loop with outer loop value
#case(i): first performing operation then breaking condition
'''
for i in range(1,6):   #1,1 to 1,5   &  2,1 to 2,5  &  3,1 to 3,5
    j=1
    while j<6:
        print(i,j)
        j+=1
    if i==3:
         break
'''
#case(ii): first breaking condition then performing operation 
'''
for i in range(1,6):   #1,1 to 1,5   &  2,1 to 2,5
    if i==3:
         break
    j=1
    while j<6:
        print(i,j)
        j+=1
'''
# 5.breaking the outer loop with inner loop value
'''
for i in range(1,6):   #1,1 to 1,5
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==6:
        break
'''

# WHILE LOOP INSIDE WHILE LOOP:----->
#1. running the loop completely
'''
i=1
while i<6:             #all
    j=1
    while j<6:
        print(i,j)
        j+=1
    i+=1
'''
#2. breaking the inner loop with inner loop value
'''
i=1
while i<6:             #1,1 to 1,3  &  2,1 to 2,3  &  3,1 to 3,3  &  4,1 to 4,3  &  5,1 to 5,3
    j=1
    while j<6:
        print(i,j)
        if j==3:
            break
        j+=1
    i+=1
'''
#3. breaking the inner loop with outer loop value
'''
i=1
while i<6:             #1,1 to 1,5  &  2,1 to 2,5  &  3,1  &  4,1 to 4,5  &  5,1 to 5,5
    j=1
    while j<6:
        print(i,j)
        if i==3:
            break
        j+=1
    i+=1
'''
#4. breaking the outer loop with outer loop value
#case(i): first performing operation then breaking condition
'''
i=1
while i<6:             #1,1 to 3,5
    j=1
    while j<6:
        print(i,j)
        j+=1
    if i==3:
        break
    i+=1
'''
#case(ii): first breaking conditions then performing operation
'''
i=1
while i<6:             #1,1 to 2,5
    if i==3:
        break
    j=1
    while j<6:
        print(i,j)
        j+=1
    i+=1
'''
#5. breaking the outer loop with inner loop value
'''
i=1
while i<6:             #1,1 to 1,5
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==6:
        break
    i+=1
'''
















    
#WAPTP PRIME NO.s IN A GIVEN RANGE (can be done using any nested looping)
'''
ll=int(input())
ul=int(input())
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                break
        else:
            print(n)
'''

#WAPTP EVERY 2nd PRIME NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
count=0
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                break
        else:
            count+=1
            if count%2==0:
                print(n)
'''
'''
ll=int(input())
ul=int(input())
list=[]
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                break
        else:
            list.append(n)
print(list[1::2])
'''
                
#WAPTP EVERY 3rd PRIME NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
count=0
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                break
        else:
            count+=1
            if count%3==0:
                print(n)
'''


#WAPTP ARMSTRONG NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
for n in range(ll,ul+1):
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        summ+=rem**l
        dummy//=10
    if n==summ:
        print(n)
'''
        
#WAPTP EVERY 2nd ARMSTRONG NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
c=0
for n in range(ll,ul+1):
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        summ+=rem**l
        dummy//=10
    if n==summ:
        c+=1
        if c%2==0:
            print(n)
'''


#WAPTP PERFECT NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
for n in range(ll,ul+1):
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if summ==n:
        print(n)
'''
#WAPTP EVERY 2nd PERFECT NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
c=0
for n in range(ll,ul+1):
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if summ==n:
        c+=1
        if c%2==0:
            print(n)
'''


#WAPTP DISARIUM NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
for n in range(ll,ul+1):
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        summ+=rem**l
        l-=1
        dummy//=10
    if summ==n:
        print(n)
'''
#WAPTP EVERY 2nd DISARIUM NO. IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
c=0
for n in range(ll,ul+1):
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        summ+=rem**l
        l-=1
        dummy//=10
    if summ==n:
        c+=1
        if c%2==0:
            print(n)
'''


#WAPTP HARSHAD NO IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
for n in range(ll,ul+1):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        summ+=rem
        dummy//=10
    if n%summ==0:
        print(n)
'''

#WAPTP EVERY 2nd HARSHAD NO IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
c=0
for n in range(ll,ul+1):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        summ+=rem
        dummy//=10
    if n%summ==0:
        c+=1
        if c%2==0:
            print(n)
'''













        
