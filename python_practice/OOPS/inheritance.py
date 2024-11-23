class Bank_v1:
    bank_name='SBI'
    bank_roi=7
    bank_branch='Hydrabad'

    def __init__(self,cn,cacc,cb,cp):
        self.cname=cn
        self.caccount=cacc
        self.cbalance=cb
        self.cpin=cp
        
    def customer_details(self):
        print(f'Name of the customer is : {self.cname}')
        print(f'Account of the customer is : {self.caccount}')
        print(f'Balance of the customer is : {self.cbalance}')
        print(f'Pin of the customer is : {self.cpin}')

    @classmethod
    def bank_details(cls):
        print(f'Name of the bank is : {cls.bank_name}')
        print(f'roi of the bank is : {cls.bank_roi}')
        print(f'branch of the bank is : {cls.bank_branch}')
        
    def withdraw(self):
        pin=int(input('enter your pin'))
        if self.cpin==pin:
            amount=int(input('enter the amount you want to withdraw'))
            if self.cbalance>=amount:
                self.cbalance-=amount
                print('withdrawl is successful, your avilable balance is: ',self.cbalance)
            else:
                print('insufficient balance')
        else:
            print('pin is wrong')

    def deposite(self):
        amount=int(input('enter the amount you want to deposite'))
        self.cbalance+=amount
        print('deposite is successful')
        
jk=Bank_v1("Jungkook Jeon",1234,100000,1307)



class Bank_v2(Bank_v1):
    bank_branch='Bangalore'
    bank_mobile=8888888888

    @classmethod
    def change_roi(cls):
        new_roi=cls.get_int_value()
        cls.bank_roi=new_roi
        print('roi is changed successfully')

    @classmethod
    def change_pin(cls):
        new_pin=cls.get_int_value()
        cls.bank_pin=new_pin
        print('pin is changed successfully')

    @staticmethod
    def get_int_value():
        intval=int(input('enter the value: '))
        return intval

ak=Bank_v2("Ambika Kumari",4321,200000,1101)


'''
#modifying parent class porperty by using parent class(changed in: parent & its objects, child & its objects)
Bank_v1.bank_roi=8
print(Bank_v1.bank_roi)
print(jk.bank_roi)
print(Bank_v2.bank_roi)
print(ak.bank_roi)

#modifying parent class porperty by using parent class object (changed in: parent class object)

jk.bank_roi=8
print(Bank_v1.bank_roi)
print(jk.bank_roi)
print(Bank_v2.bank_roi)
print(ak.bank_roi)

#modifying parent class porperty by using child class (changed in: child class & its objects)
Bank_v2.bank_roi=8
print(Bank_v1.bank_roi)
print(jk.bank_roi)
print(Bank_v2.bank_roi)
print(ak.bank_roi)
'''
#modifying parent class porperty by using child class object (changed in: child class object)
ak.bank_roi=8
print(Bank_v1.bank_roi)
print(jk.bank_roi)
print(Bank_v2.bank_roi)
print(ak.bank_roi)





'''
ak.change_roi()
print(Bank_v1.bank_roi)
print(jk.bank_roi)
print(Bank_v2.bank_roi)
print(ak.bank_roi)

Bank_v2.change_roi()
print(Bank_v1.bank_roi)
print(jk.bank_roi)
print(Bank_v2.bank_roi)
print(ak.bank_roi)   

Bank_v1.withdraw(ak)
print(ak.bank_cbalance)
'''










    

