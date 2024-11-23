
#to calculate the length of string 
'''
s=input('enter your string: ')
c=0
for i in s:
    c+=1
print(c)
'''
#to find the 2nd max no.in a given length
'''
l=[1,3,4,2,2,3,21,4,24,56]
print(l)
s=set(l)
print(s)
L=list(s)
print(L)
L.sort()
print(L)
print(L[-2])#2nd max no.
print(L[1])#min no.
'''
'''
l=[1,3,4,2,2,3,21,4,24,56]
s=set(l)
sorted(s)
print(s)
'''
'''
l=[1,3,4,2,2,3,21,4,24,21,101,12,56]
L=list(set(l))
L.sort()
print(L[-2])
'''

#to convert number to binary
def numToBin(n):
    if n>1:
        numToBin(n//2)
    print(n%2, end='')

#numToBin(7)
#numToBin(int(input()))

'''if __name__=='__main__':
    val=8
    numToBin(val)

if __name__=='__main__':
    val=int(input())
    numToBin(val)
'''

#octal to decimal conversion
def octToDec(n):
    dummy=n
    base=1
    decNum=0
    while(dummy>0):
        rem=dummy%10
        dummy//=10
        decNum+=rem*base
        base*=8
    print(decNum)
octToDec(67)


def octToDec(n):
    dummy=n
    base=0
    decNum=0
    while(dummy>0):
        rem=dummy%10
        dummy//=10
        decNum+=rem*(8**base)
        base+=1
    print(decNum)
octToDec(67)


def octToDec(n):
    dummy=n
    s=str(n)
    l=0
    decNum=0
    for i in s:
        rem=dummy%10
        dummy//=10
        decNum+=rem*(8**l)
        l+=1
    print(decNum)
octToDec(67)















    











