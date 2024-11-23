# Q1. WAPTP SUM OF 1ST 'N' NUMBERS
'''
n=int(input())
i=1
sum=0
while i<n+1:
    sum+=i
    i+=1
print(sum)
'''
# Q2. WAPTP FACTORIAL OF THE GIVEN NUMBER
'''
n=int(input())
i=1
fact=1
while i<n+1:
    fact*=i
    i+=1
print(fact)
'''
# Q3. WAPTP GIVEN NO. IS PERFECT NO.OR NOT
'''
n=int(input())
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')
'''
# Q4. WAPTP EVEN NO.s IN A GIVEN RANGE
'''
ll=int(input())
ul=int(input())
while ll<=ul:
    if ll%2==0:
        print(ll)
    ll+=1
'''
# Q5. WAPTP IP OF ALL VOWELS PRESENT IN GIVEN STRING

'''s=input().lower()
ip=0
while ip<len(s):
    if s[ip] in 'aeiou':
        print(ip)
    ip+=1'''

# Q6. WAPTP ELT PRESENT IN EVEN IPs
'''
s=input()
ip=0
while ip<len(s):
    if ip%2==0:
        print(s[ip])
    ip+=1
'''
# Q7. WAPTP SUM OF DIGITS PRESENT IN GIVEN STRING
'''
s=input()
sum=0
ip=0
while ip<len(s):
    if s[ip] in '0123456789':
        sum+=int(s[ip])
    ip+=1
print(sum)
'''
# Q8. WAPTP SUM OF IPs OF EVEN NO.s
'''
s=input()
sum=0
ip=0
while ip<len(s):
    if s[ip] in '02468':
        sum+=ip
    ip+=1
print(sum)
'''
# Q9. WAPTP SUM OF EVEN NOs PRESENT AT EVEN IPs
'''
s=input()
sum=0
ip=0
while ip<len(s):
    if ip%2==0 and s[ip] in '02468':
        sum+=int(s[ip])
    ip+=1
print(sum)
'''
# Q10. WAPTP SUM OF EVEN IPs HAVING EVEN NOs
'''
s=input()
sum=0
ip=0
while ip<len(s):
    if ip%2==0 and s[ip] in '02468':
        sum+=ip
    ip+=1
print(sum)
'''
# Q11. WAPTP SUM OF ODD IPs HAVING EVEN NOs
'''
s=input()
sum=0
ip=0
while ip<len(s):
    if ip%2!=0 and s[ip] in '02468':
        sum+=ip
    ip+=1
print(sum)
'''
# Q12. WAPTP SUM OF ODD NOs AT ODD IPs
'''
s=input()
sum=0
ip=0
while ip<len(s):
    if ip%2!=0 and s[ip] in '13579':
        sum+=int(s[ip])
    ip+=1
print(sum)
'''
# Q13. WAPTP MAX NO. IN A GIVEN LIST AND ITS IP
'''
l=eval(input())
ip=0
maxno=l[0]
maxip=0
while ip<len(l):
    if l[ip]>maxno:
        maxno=l[ip]
        maxip=ip
    ip+=1
print(maxno,maxip)
'''

# Q14. WAPTP HOW MANY TIMES THE GIVEN SUBSTRING IS PRESENT IN GIVEN STRING
'''
ms=input()
ss=input()
ip=0
c=0
while ip<(len(ms)-len(ss)+1):
    if ms[ip:ip+len(ss)]==ss:
        c+=1
    ip+=1
print(c)
'''
# Q15. WAPTP SWAPPED ELEMENT IN THE FOLLOWING WAY:
# IP:[11,22,33,44,55,66]   OP:[22,11,44,33,66,55]
'''
l=eval(input())
ip=0
while ip<len(l):
    l[ip],l[ip+1]=l[ip+1],l[ip]
    ip+=2
print(l)
'''
# Q16. WAPTP SWAPPED ELEMENT IN THE FOLLOWING WAY
# IP:[11,22,33,44,55,66]   OP:[66,55,44,33,22,11]
'''
l=eval(input())
ip=0
while ip<len(l)//2:
    l[ip],l[-ip-1]=l[-ip-1],l[ip]
    ip+=1
print(l)
'''

# PRACTICE Q.S :

'''UL=int(input())
LL=int(input())
if LL%2!=0 :
    LL-=1
else:
    LL=LL
while UL<LL+1:
    print(LL)
    LL-=2'''

'''
UL=int(input())
LL=int(input())
while UL<=LL:
    if LL%2==0 :
        print(LL)
    LL-=1
'''
'''
n=int(input())
i=1
sum=0
while i<n+1:
    sum+=i
    i+=1
print(sum)
'''
    
    
    

















