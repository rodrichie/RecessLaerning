#object oriented programming
#classses
"""
class Cars:
    def __init__(self,make,model,year):
        self.model=model
        self.make=make
        self.year=year

    def start_engine(self):
        print("engine started")
    def stop_engine(self):
        print("engine stopped")

my_car=Cars("Toyota","corollard",2022)
print(my_car.make)
print(my_car.year)
print(my_car.model)
my_car.start_engine()
my_car.stop_engine()

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(self.length*self.width)

    def calulate_perimeter(self):
        print(2*(self.length+self.width))

rectangle=Rectangle(14,10)
rectangle.calulate_perimeter()
rectangle.calculate_area()  

class BankAccount:
    def __init__(self,account_number,initial_balance=0):
        self.account_number=account_number
        self.balance=initial_balance

    def deposit(self,amount):
        if amount >0:
            self.balance += amount
            print(f"Deposited {amount} into Account #{self.account_number}.")
        else:
            print("Invalid deposit amount.")



    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -=amount
            print(f"withdrew {amount} from  Account #{self.account_number}.")
        else:
            print("insufficient funds")


    def display_balance(self):
        print(f"Account #{self.account_number} balance: {self.balance}") 
account1 = BankAccount(12345 , 1000)
account1.display_balance() 

account1.deposit(500)
account1.display_balance()

account1.withdraw(200)
account1.display_balance()

account1.withdraw(2000)
             


class Student:
    def __init__(self,name,year,course):
        self.name = name
        self.year = year
        self.course = course

    def display(self):
        print(self.name)
        print(self.year)
        print(self.course)

newStudent = Student("rodrick", 2,"software engineering")
newStudent.display()
"""
#exercise calculate and display employee bonusses(15%) of salary [employee1: 150000, employee2: 230000]
"""
class EmployeeSalary:
    def __init__(self,name,salary):
        self.salary = salary
        self.name = name

    def calculateBonus(self):
        bonus=(15/100)*self.salary
        print(f" {self.name} has Bonus:{bonus}")

employee1 = EmployeeSalary("rodrick" ,150000)
employee1.calculateBonus()
employee2= EmployeeSalary("stephen" ,230000)
employee2.calculateBonus()
"""


#Encapsulation
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number#encapsulates the accnumber attribute
        self._balance = balance#encapsulates the balance attribute

    def deposit(self, amount):
        self._balance +=amount#encapsulates the depost

    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount#encapsulates the withdraw
        else:
            print("insufficient balance")

    def display_balance(self):
        print("Account Number:", self._account_number)
        print("Balance:", self._balance) 

my_account = BankAccount("12345678" ,1000)

#access the bank objects and modify the encapsulated attributes attributes indirectly
print(my_account._account_number)
print(my_account._balance)
my_account.deposit(500)
print(my_account.balance)
my_account.withdraw(100)
print(my_account.balance)
"""
#another better way for encapsulating
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Number:", self._account_number)
        print("Balance:", self._balance)

    # Getter methods
    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    # Setter methods
    def set_account_number(self, account_number):
        self._account_number = account_number

    def set_balance(self, balance):
        self._balance = balance


my_account = BankAccount("12345678", 1000)

# Access the encapsulated attributes indirectly using getter methods
print(my_account.get_account_number())
print(my_account.get_balance())

my_account.deposit(500)
print(my_account.get_balance())

my_account.withdraw(100)
print(my_account.get_balance())
"""

#exercise1 converting degrees to fahrenheit
class TemperatureConverter:
    def __init__(self, degrees):
        self._degrees = degrees

    def get_degrees(self):
        return self._degrees

    def set_degrees(self, degrees):
        self._degrees = degrees

    def to_fahrenheit(self):
        return (self._degrees * 9/5) + 32


# Create an instance of TemperatureConverter
temp_converter = TemperatureConverter(25)

# Access the encapsulated attribute indirectly using getter method
print("Degrees Celsius:", temp_converter.get_degrees())

# Convert degrees to Fahrenheit using the to_fahrenheit method
fahrenheit = temp_converter.to_fahrenheit()
print("Degrees Fahrenheit:", fahrenheit)

# Modify the degrees using setter method
temp_converter.set_degrees(30)

# Convert the updated degrees to Fahrenheit
fahrenheit = temp_converter.to_fahrenheit()
print("Updated Degrees Fahrenheit:", fahrenheit)

# Assignment2:  Show encapsulation with employee information to give a
# pay incrementation (Salary with employee information to new_salary)e.g from 850000 to 1000000

class Employee:
    def __init__(self, emp_code, emp_fullname, emp_salary):
        self._emp_code = emp_code
        self._emp_fullname = emp_fullname
        self._emp_salary = emp_salary

    def get_employee_code(self):
        return self._emp_code

    def get_employee_fullname(self):
        return self._emp_fullname

    def get_employee_salary(self):
        return self._emp_salary

    def set_employee_salary(self, new_salary):
        self._emp_salary = new_salary

    def increment_pay(self, increment_amount):
        self._emp_salary += increment_amount


# Create employee instances
employee1 = Employee(1001, "Rodrick Nabasa", 850000)
employee2 = Employee(1002, "Ronald Atuhaire", 900000)
employee3 = Employee(1003, "Samuel Ainomugisha", 950000)

# Access and display initial salaries
print("Initial Employee Salaries:")
print(f'{employee1.get_employee_fullname()}: shs {employee1.get_employee_salary()}') 
print(f'{employee2.get_employee_fullname()}: shs {employee2.get_employee_salary()}')
print(f'{employee3.get_employee_fullname()}: shs {employee3.get_employee_salary()}')

# Increment the salaries for each employee
increment_amount = 150000
employee1.increment_pay(increment_amount)
employee2.increment_pay(increment_amount)
employee3.increment_pay(increment_amount)

# Access and display salaries after the first increment
print("\nEmployee Salaries after Increment:")
print(f'{employee1.get_employee_fullname()} : shs {employee1.get_employee_salary()}')
print(f'{employee2.get_employee_fullname()}: shs {employee2.get_employee_salary()}')
print(f'{employee3.get_employee_fullname()}: shs {employee3.get_employee_salary()}')







