#calling outer function while passing int as an argument & returning int as value
'''
def outer(arg):
    print('outer started')
    print(arg)
    def inner():
        print('inner started')
        print('inner ended')
    print('outer ended')
    inner()
    return 100
result=outer(11)
print(result)
'''

#calling outer fun with int as an arg & returning inner FA
'''
def outer(arg):
    print('outer started')
    print(arg)
    def inner():
        print('inner started')
        print('inner ended')
    print('outer ended')
    return inner
result=outer(11) #result=inner FA
print(result)
result()
'''

#nested fun with 1 arg & passing hello FA as arg value & returning inner FA
'''
def outer(arg):
    print('outer started')
    print(arg)
    def inner():
        print('inner started')
        arg()
        print('inner ended')
    print('outer ended')
    return inner
def hello():
    print('hello started')
    print('hello ended')
result=outer(hello) #result=inner FA
print(result)
result()
'''

#DECORATORS:
'''
def outer(arg):
    print('outer started')
    print(arg)
    def inner():
        print('inner started')
        arg()
        print('inner ended')
    print('outer ended')
    return inner
@outer
def hello():
    print('hello started')
    print('hello ended')
hello()
'''
#using decorators to find the time taken by the fibonacci series to execute particular no.of terms
def timeDecorator(arg):
    def inner():
        import time
        IT1=time.time()
        arg()
        FT1=time.time()
        print(f'Actual Time for fibo = {FT1-IT1}')

        IT2=time.time()
        prime()
        FT2=time.time()
        print(f'Actual Time for prime = {FT2-IT2}')
        
    return inner

@timeDecorator
def fibo():
    a=int(input('enter fv= '))
    b=int(input('enter sv= '))
    n=int(input('enter number of terms= '))
    if n==1:
          print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b)
        for i in range(n-1):
            c=a+b
            print(c)
            a,b=b,c

def prime():
    ll=int(input('enter starting= '))
    ul=int(input('enter ending= '))
    for n in range(ll,ul+1):
     if n>1:
         for i in range(2,n//2+1):
             if n%i==0:
                 break
         else:
            print(n)
    
fibo()



















