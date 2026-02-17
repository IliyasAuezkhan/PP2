# 1 example 

class Company:
    company_name = "Tech Corp"  # Class Variable

    def __init__(self, employee):
        self.employee = employee

emp1 = Company("Alice")
emp2 = Company("Bob")
print(emp1.company_name)  # Output: Tech Corp
print(emp2.company_name)  # Output: Tech Corp

# 2 example

class Employee:
    emp_count = 0  # Class Variable

    def __init__(self, name):
        self.name = name
        Employee.emp_count += 1  # Increment shared counter

emp1 = Employee("Alice")
emp2 = Employee("Bob")
print(Employee.emp_count)  # Output: 2

# 3 example 

class Scenario:
    rate = 1.05  # Class Variable

    def __init__(self, value):
        self.value = value

    def calculate(self):
        return self.value * Scenario.rate

s1 = Scenario(100)
Scenario.rate = 1.10  # Modify for all instances
print(s1.calculate())  # Output: 110.0 (100 * 1.10)

# 4 example

class Product:
    tax = 0.05  # Class Variable

    def __init__(self, price):
        self.price = price

p1 = Product(100)
p2 = Product(200)
p2.tax = 0.10  # Instance-level override

print(p1.tax)  # Output: 0.05 (Original class variable)
print(p2.tax)  # Output: 0.10 (Instance variable)
print(Product.tax)  # Output: 0.05 (Class variable remains unchanged)