n=int(input())
stars=n*2
for row in range(1,n+1):
    dummy=n
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if st<stars//2:        
            dummy-=1
        elif st==stars//2:
            dummy=row
        else:
            dummy+=1
    print()
    stars-=2
    
    
