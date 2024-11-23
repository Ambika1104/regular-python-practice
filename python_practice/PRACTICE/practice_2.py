# WAPTP fibonacci series: third no= first no + second no : 0   1   1   2   3   5   8   13   21
'''
n=int(input())
n1=0
n2=1
summ=0
while summ<=n:
    print(summ)
    summ=n1+n2
    n1=n2
    n2=summ
'''

end=int(input())
n1=2
n2=3
summ=2
while summ<=end:
    print(summ)
    summ=n1+n2
    n1=n2
    n2=summ

    
