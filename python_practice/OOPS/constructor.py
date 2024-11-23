class Employee:
    cname='ABC'
    clocation='Bangalore'
    emp_count=0
    def __init__(self,en,ea,er,es):
        self.ename=en
        self.eage=ea
        self.erole=er
        self.esalary=es
        Employee.emp_count+=1
    def __str__(self):
        return self.ename
    def __del__(self):
        Employee.emp_count-=1
        print(f'{self} is deleted')
vicky=Employee('Vicky',23,'developer',500000)
print(Employee.emp_count)
rithwik=Employee('Rithwik',29,'analyst',600000)
print(Employee.emp_count)
del rithwik
print(Employee.emp_count)
