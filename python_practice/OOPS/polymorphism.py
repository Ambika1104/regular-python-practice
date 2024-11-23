class Bank_v1:
    bank_name='SBI'
    bank_roi=7
    bank_branch='Mysore'

    def __init__(self,cn,ca,cacc,cb):
        self.cname=cn
        self.cage=ca
        self.caccount=cacc
        self.cbalance=cb
           
    def customer_details(self):
        print(f'Name of the customer is : {self.cname}')
        print(f'Age of the customer is : {self.cage}')
        print(f'Account of the customer is : {self.caccount}')
        print(f'Balance of the customer is : {self.cbalance}')
        
    @classmethod
    def bank_details(cls):
        print(f'Name of the bank is : {cls.bank_name}')
        print(f'roi of the bank is : {cls.bank_roi}')
        print(f'branch of the bank is : {cls.bank_branch}')
        
    def withdraw(self):
        amount=self.get_int_value()
        if self.cbalance>=amount:
            self.cbalance-=amount
            print('withdrawl is successful, your avilable balance is: ',self.cbalance)
        else:
            print('insufficient balance')
       

    def deposite(self):
        amount=self.get_int_value()
        self.cbalance+=amount
        print('deposite is successful')

    @staticmethod
    def get_int_value():
        intval=int(input('enter the value: '))
        return intval
        
jk=Bank_v1("Jungkook Jeon",27,1234,100000)



class Bank_v2(Bank_v1):
    bank_name='SBI'
    bank_roi=7
    bank_branch='Bangalore'
    bank_mobile=8985338785

    def __init__(self,cn,ca,cacc,cb,cp,cad):
        self.cname=cn
        self.cage=ca
        self.caccount=cacc
        self.cbalance=cb
        self.cpin=cp
        self.caadhar=cad

    def customer_details(self):
        print(f'Name of the customer is : {self.cname}')
        print(f'Age of the customer is : {self.cage}')
        print(f'Account of the customer is : {self.caccount}')
        print(f'Balance of the customer is : {self.cbalance}')
        print(f'Aadhar of the customer is : {self.caadhar}')

    @classmethod
    def bank_details(cls):
        print(f'Name of the bank is : {cls.bank_name}')
        print(f'roi of the bank is : {cls.bank_roi}')
        print(f'branch of the bank is : {cls.bank_branch}')
        print(f'mobile no of the bank is : {cls.bank_mobile}')

    def withdraw(self):
        pin=int(input("enter pin: "))
        if self.cpin==pin:
            amount=self.get_int_value()
            if self.cbalance>=amount:
                self.cbalance-=amount
                print('withdrawl is successful, your avilable balance is: ',self.cbalance)
            else:
                print('insufficient balance')
        else:
            print('pin is wrong')

    @classmethod
    def change_roi(cls):
        new_roi=cls.get_int_value()
        cls.bank_roi=new_roi
        print(f'roi is changed successfully, new pin is {cls.bank_roi}')

    def change_pin(self):
        pin=int(input("enter original pin"))
        if self.cpin==pin:
            new_pin=self.get_int_value()
            self.cpin=new_pin
            print(f'pin is changed successfully, new pin is {self.cpin}')

ak=Bank_v2("Ambika Kumari",23,4321,200000,1101,1997)
'''
jk.deposite()
ak.deposite()

jk.withdraw()
ak.withdraw()

jk.customer_details()
ak.customer_details()
jk.bank_details()
ak.bank_details()
'''
ak.change_pin()
ak.change_roi()





    

