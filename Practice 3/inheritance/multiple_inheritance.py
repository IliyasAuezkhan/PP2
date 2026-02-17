# 1 example

class A:
    def a(self):
        print("A")

class B:
    def b(self):
        print("B")

class C(A, B):
    pass

c = C()
c.a()
c.b()

# 2 example

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

C().show()   

# 3 example

class A:
    def test(self):
        print("A")

class B(A):
    def test(self):
        super().test()
        print("B")

class C(B):
    def test(self):
        super().test()
        print("C")

C().test()

# 4 example

class Fly:
    def move(self):
        print("Flying")

class Swim:
    def move(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

Duck().move() # from left to right