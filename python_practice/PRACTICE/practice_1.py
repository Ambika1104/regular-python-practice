'''
hy=int(input('enter human year '))
dy=0
for i in range(1,3):
    dy=dy+10.5
for j in range(3,hy+1):
    dy=dy+4
print('dog year = ',dy)
'''


'''
hy=int(input())
dy=0
if hy<3:
    onetwo=10.5*hy
    dy=onetwo
else:
    rest=21+(hy-2)*4
    dy=rest
print(dy)
'''
hy=int(input())
dy=0
if hy<3:
    dy+=10.5
else:
    dy+=21+((hy-2)*4)
print(dy)



