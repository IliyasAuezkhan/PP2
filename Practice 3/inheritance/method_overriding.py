# 1 example

class Bird:
    def fly(self):
        print("Bird flies")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

Penguin().fly()

# 2 example

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4 * 4

print(Square().area())

# 3 example

class Parent:
    def hello(self):
        print("Hello")

class Child(Parent):
    def hello(self):
        print("Hi")

Child().hello()

# 4 example

class Base:
    def test(self):
        print("Base")

class Derived(Base):
    def test(self):
        super().test()
        print("Derived")

Derived().test()
