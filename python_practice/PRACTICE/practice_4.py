class a:
    x=10
    def __init__(self,v):
        self.av=v
        print("class a")
class b:
    y=10
    def __init__(self,b):
        self.bb=b
        print("class b")
    def obj1(self):
        print(f"the value of bb is {self.bb}")
    @classmethod
    def details(cls):
        print("anything")
class c(a,b):
    pass
oc=c(66)
oc.details()
oc.obj1()
print(c.mro())
