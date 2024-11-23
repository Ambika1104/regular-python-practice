a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("a is max")
            else:
                print("e is max")
        else:
            if d>e:
                print("d is max")
            else:
                print("e is max")
    else:
        if c>d:
            if c>e:
                print("c is max")
            else:
                print("e is max")
        else:
            if d>e:
                print("d is max")
            else:
                print("e is max")
else:
     if b>c:
        if b>d:
            if b>e:
                print("b is max")
            else:
                print("e is max")
        else:
            if d>e:
                print("d is max")
            else:
                print("e is max")
     else:
        if c>d:
            if c>e:
                print("c is max")
            else:
                print("e is max")
        else:
            if d>e:
                print("d is max")
            else:
                print("e is max")
