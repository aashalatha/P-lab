class Employee:
    def __init__(self,empid,name,address,salary):
        self.empid = empid 
        self.name = name
        self.address = address
        self.salary = salary
    
class Teacher(Employee):
    def __init__(self,sub,dept):
        self.sub = sub
        self.dept = dept
        Employee.__init__(self,empid,name,address,salary)
   
    def display(self):
        print("Employee Id:",self.empid)
        print("Employee Name:",self.name)
        print("Address :",self.address)
        print("Department:",self.dept)
        print("Subject:",self.sub)
        print("Salary :",self.salary)
        
empid = input("Enter the employee id:")
name = input("Enter the employee name:")
address = input("Enter the address of the employee:")
salary = input("Enter the salary:")
dept = print("Enter the department:")
sub = print("Enter the subjects taught by the teacher:")

t = Teacher(sub,dept)
t.display()