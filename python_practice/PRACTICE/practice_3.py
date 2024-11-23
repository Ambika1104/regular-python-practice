# WAPTP THE FOLLOWING USING WHILE LOOP

# 1. FIRST EVEN 'N' NUMBERS:
'''n=2
while n<=20:
    print(n)
    n+=2'''

# 2. FIRST ODD 'N' NUMBERS:
'''n=1
while n<=20:
    print(n)
    n+=2'''

#3. FIRST NATURAL 'N' NUMBERS:
'''n=1
while n<=10:
    print(n)
    n+=1'''

# 4. FIRST NATURAL 'N' NUMBERS:
'''n=0
while n<10:
    print(n)
    n+=1'''

# 5. WAPTP FIRST 10 INTEGERS AND THEIR SQUARES
'''n=1
sq=1
while n<=10:
    sq=n*n
    print(n,sq)
    n+=1'''

# 6. WAPTP THE SERIES 10,20,30...300
'''n=10
while n<=300:
    print(n)
    n+=10'''

# 7. WAPTP THE SERIES 105,98,91,...7
'''n=105
while n>=7:
    print(n)
    n-=7'''

# 8. WAPTP FIRST 10 NATURAL NUMBER IN REVERSE ORDER
'''n=10
while n>=1:
    print(n)
    n-=1'''

# 9. WAPTP SUM OF 1st 10 NATURAL NO.s
'''n=0
sum=0
while n<=10:
    sum+=n
    n+=1
print(sum)'''

# 10. WAPTP  SUM OF 1ST 10 EVEN NO.s
'''n=2
sum=0
while n<=20:
    sum+=n
    n+=2
print(sum)'''

# 11. WAPTP TABLE OF A NO. ENTERED BY THE USER
'''n=int(input())
i=1
table=0
while i<=10:
    table=n*i
    print(f'{n}*{i}={table}')
    i+=1'''

# 12. WAPTP ALL EVEN NO.s THAT FALLS BETWEEN 2 NO.S GIVEN BY USER
'''n1=int(input())
n2=int(input())
while n1<=n2:
    print(n1)
    n1+=2'''

# 13. WAP TO CHECK WHETHER A NO. IS PRIME OR NOT
'''n=int(input())
i=2
c=0
while i<n//2:
    if n%i!=0:
        c=0
    else:
        c+=1
    i+=1
if c==0:
    print(f'{n} is a prime number')'''
    
    

# 14. WAP TO FIND SUM OF DIGITS OF A NO. ACCEPTED FROM USER
'''n=int(input())
s=str(n)
sum=0
ip=0
while ip<len(s):
    sum+=int(s[ip])
    ip+=1
print(sum)'''

    
# 15. WAP FIND PRODUCT OF DIGITS OF A NO. ACCEPTED BY USER
'''n=int(input())
s=str(n)
product=1
ip=0
while ip<len(s):
    product*=int(s[ip])
    ip+=1
print(product)'''

#WAP TO REVERSE THE NO. ACCEPTED FROM USER

