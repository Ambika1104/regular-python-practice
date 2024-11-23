class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def __ge__(self,secondobject):
        area1=self.length*self.breadth
        area2=secondobject.length*secondobject.breadth
        return area1>=area2
R1=Rectangle(300,200)
R2=Rectangle(500,150)
print(R1>=R2)
