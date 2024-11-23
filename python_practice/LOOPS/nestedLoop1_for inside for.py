#NESTED LOOPING STATEMENTS:-->

#1. FOR LOOP INSIDE FOR LOOP

# case 1: running the loop completely
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
'''

# case 2: breaking the inner loop with outer loop value
'''
for i in range(1,6):
    for j in range(1,6):
        if i==3:
            break
        print(i,j)
'''

# case 3: breaking the inner loop with inner loop value
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if j==3:
            break
'''

# case 4: breaking the outer loop with outer loop value
'''-->first breaking condition and then operation'''
'''
for i in range(1,6):
    if i==3:
        break
    for j in range(1,6):
        print(i,j)
'''

'''--> first operation and then breaking condition'''
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if i==3:
        break
'''

# case 5: breaking the outerr loop with inner loop value
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if j==5:
        break
'''



# NOTE-->
'''loop runs for all values, because no where the inner loop is coming out with j=3 (always j=5),
so condition is never satisfied so loop will run completely for all values.'''
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if j==3:
        break
 '''

