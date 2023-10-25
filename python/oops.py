class Parent():
    def test(self):
        print("hi from parent")

class Child(Parent):
    def test(self):
        print("hi from child")

ob = Child()
ob.test()

class Parent1():
    def test(self):
        print("hi from parent1")

class Parent2():
    def test(self):
        print("hi from parent2")

class Child(Parent1, Parent2):
    def test(self):
        print("hi from child")
        
ob = Child()
ob.test()     
