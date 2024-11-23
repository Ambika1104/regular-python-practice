'''
class Bank:
    Bank_name='SBI'
    Bank_ifsc=1234
    Bank_roi=7

    def __init__(self,cn,cag,cb,cacc,cp):
        self.cname=cn
        self.cage=cag
        self.cbalance=cb
        self.caccount=cacc
        self.cpin=cp

    def customer_details(self):
        print(f'Name of the customer is : {self.cname}')
        print(f'Age of the customer is : {self.cage}')
        print(f'Balance of the customer is : {self.cbalance}')
        print(f'Account of the customer is : {self.caccount}')
        print(f'Pin of the customer is : {self.cpin}')

    def withdraw(self):
        pin=int(input('enter your pin'))
        if self.cpin==pin:
            amount=int(input('enter the amount you want to withdraw'))
            if self.cbalance>=amount:
                self.cbalance-=amount
                print('withdrawl is successful')
            else:
                print('insufficient balance')
        else:
            print('pin is wrong')

    def deposite(self):
        amount=int(input('enter the amount you want to deposite'))
        self.cbalance+=amount
        print('deposite is successful')
        
    @classmethod
    def bank_details(cls):
        print(f'Name of the bank is : {cls.Bank_name}')
        print(f'ifsc of the bank is : {cls.Bank_ifsc}')
        print(f'roi of the bank is : {cls.Bank_roi}')
        
    @classmethod
    def change_roi(cls):
        new_roi=int(input('enter new roi= '))
        cls.Bank_roi=new_roi
        print('roi is changed successfully')

jk=Bank('Jungkook Jeon',27,30000,1234567890,1307)
ak=Bank('Ambika Kumari',23,33000,987654321,1101)


#jk.withdraw()
#print(Bank.customer_details(jk))
#ak.deposite()
#print(ak.customer_details())
jk.change_roi()
print(Bank.bank_details())
print(jk.bank_details())
print(ak.bank_details())
'''

class School:
    Sname='JSP'
    Slocation='Bangalore'
    Sprincipal='ABC'

    def __init__(self,cn,ca,cc):
        self.studentName=cn
        self.studentAge=ca
        self.studentClass=cc
33
    @classmethod
    def school_details(cls):
        print(f'Name of the school is : {cls.Sname}')
        print(f'Location of the school is : {cls.Slocation}')
        print(f'Principal of the school is : {cls.Sprincipal}')

    def student_details(self):
        print(f'Name of the student is : {self.studentName}')
        print(f'Age of the student is : {self.studentAge}')
        print(f'Class of the student is : {self.studentClass}')
        
    @classmethod
    def change_location(cls):
        new_location=input('enter new location: ')
        cls.Slocation=new_location
        print('Location is changed successfully')

    def update_class(self):
        new_class=int(input('enter new class: '))
        self.studentClass=new_class
        print('class is updated successfully')
        

jk=School('Jungkook Jeon',11,7)
ak=School('Ambika Kumari',11,7)


#jk.school_details()
#School.school_details()


#print(School.student_details(ak))
#ak.student_details()

'''
jk.change_location()
print(School.school_details())
print(jk.school_details())
print(ak.school_details())

School.change_location()
print(School.school_details())
print(jk.school_details())
print(ak.school_details())
'''
'''
ak.update_class()
print(jk.student_details())
print(ak.student_details())

School.update_class(ak)
print(jk.student_details())
print(ak.student_details())
'''






























            
