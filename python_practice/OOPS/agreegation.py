#SCENERIO TWO: When objects have dynamic/different properties -->
'''
class Car:
    def __init__(self,n,c,no):
        self.cname=n
        self.ccolor=c
        self.cnumber=no
    def start(self):
        print('inserted te key')
    def accelerating(self):
        print('pressed the accelerator')
    def stop(self):
        print('applied the break')
    def car_details(self):
        print('name of the car is {self.cname}')
        print('color of the car is {self.ccolor}')
        print('number of the car is {self.cnumber}')

class Driver:
    def __init__(self,dn,di,da,de):
        self.dname=dn
        self.did=di
        self.dage=da
        self.dexp=de
        
        n=input('Enter the car name: ')
        c=input('Enter the car color: ')
        no=input('Enter the car number: ')

        CCO=Car(n,c,no)
        self.dcar=CCO
        
    def driving(self):
        print('driver has enter into the car')
        self.dcar.start()
        self.dcar.accelerating()
        self.dcar.stop()
        print('driver has came out of the car')
        
JK=Driver('Jeon Jungkook',7,27,5)
JK.driving()
'''

class Player:
    def __init__(self,pn,pa,pco,pm,pr,pw):
        self.pname=pn
        self.page=pa
        self.pcountry=pco
        self.pmatches=pm
        self.pruns=pr
        self.pwickets=pw

class Team:
    def __init__(self,n):
        self.nop=n
        self.pl=[]

        for po in range(self.nop):
            pn=input("enter player name: ")
            pa=int(input("enter player age: "))
            pco=input("enter player country: ")
            pm=int(input("enter player matches: "))
            pr=int(input("enter player runs: "))
            pw=int(input("enter player wickets: "))

            PlayerObject=Player(pn,pa,pco,pm,pr,pw)

            self.pl.append(PlayerObject)

    def max_runs(self):
        MRPO=self.pl[0]
        for po in self.pl:
            if po.pruns>MRPO.pruns:
                MRPO=po
        return MRPO.pname

    def max_wickets(self):
        MWPO=self.pl[0]
        for po in self.pl:
            if po.pwickets>MWPO.pwickets:
                MWPO=po
        return MWPO.pname

india=Team(2)
print(f'Maximun runs scorer palyer is {india.max_runs()}')
print(f'Maximun wickets taker palyer is {india.max_wickets()}')
        











            
    
















        
        
