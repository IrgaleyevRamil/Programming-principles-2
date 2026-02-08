"""
Practice 03 - Python Inheritance (All in one file)

Topics:
1) Inheritance basics (parent -> child)
2) Using super() to call parent constructor/methods
3) Method overriding (child changes parent behavior)
4) Multiple inheritance (class with 2 parents)
"""

# =========================================================
# TOPIC 1: Inheritance basics (5 examples)
# =========================================================

# Example 1: child inherits a method from parent
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()  # inherited from Animal


# Example 2: child class adds its own method
class Cat(Animal):
    def meow(self):
        print("Meow")

c = Cat()
c.speak()
c.meow()


# Example 3: child inherits fields set in parent __init__
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Marat")
print("Student name:", s.name)


# Example 4: child adds new fields by its own __init__ (simple way)
class Worker(Person):
    def __init__(self, name, job):
        self.name = name
        self.job = job

w = Worker("Dias", "Engineer")
print(w.name, w.job)


# Example 5: child class can be checked with isinstance
print("Is s a Student?", isinstance(s, Student))
print("Is s a Person?", isinstance(s, Person))
print("Is s an Animal?", isinstance(s, Animal))


# =========================================================
# TOPIC 2: Using super() (5 examples)
# =========================================================

# Example 1: super() to call parent constructor
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car = Car("Toyota", "Camry")
print("Car:", car.brand, car.model)


# Example 2: super() to reuse parent method
class Printer:
    def show(self):
        print("Printing...")

class ColorPrinter(Printer):
    def show(self):
        super().show()
        print("With color!")

cp = ColorPrinter()
cp.show()


# Example 3: super() with additional logic
class Account:
    def __init__(self, balance=0):
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, balance=0, percent=0.05):
        super().__init__(balance)
        self.percent = percent

sa = SavingsAccount(1000, 0.1)
print("Savings:", sa.balance, sa.percent)


# Example 4: using super() in method to extend behavior
class BaseTimer:
    def start(self):
        print("Timer started")

class AdvancedTimer(BaseTimer):
    def start(self):
        super().start()
        print("Advanced features enabled")

at = AdvancedTimer()
at.start()


# Example 5: super() to avoid rewriting parent logic
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

sq = Square(5)
print("Square area:", sq.area())


# =========================================================
# TOPIC 3: Method overriding (5 examples)
# =========================================================

# Example 1: overriding speak()
class Bird(Animal):
    def speak(self):
        print("Chirp")

b = Bird()
b.speak()


# Example 2: overriding method and using super() inside
class LoudDog(Dog):
    def speak(self):
        super().speak()
        print("WOOF!!!")

ld = LoudDog()
ld.speak()


# Example 3: overriding method to change return value
class MathBase:
    def calc(self, x, y):
        return x + y

class MathChild(MathBase):
    def calc(self, x, y):
        return x * y

mb = MathBase()
mc = MathChild()
print("Base calc:", mb.calc(3, 4))
print("Child calc:", mc.calc(3, 4))


# Example 4: overriding __str__ for nicer printing
class Phone:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return "Phone brand: " + self.brand

p = Phone("Samsung")
print(p)


# Example 5: overriding with small validation logic
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

class SafeTemperature(Temperature):
    def __init__(self, celsius):
        if celsius < -100:
            celsius = -100
        super().__init__(celsius)

st = SafeTemperature(-999)
print("Safe temp:", st.celsius)


# =========================================================
# TOPIC 4: Multiple inheritance (5 examples)
# =========================================================

# Example 1: class inherits from two parents
class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()
duck.swim()


# Example 2: multiple inheritance with methods from both parents
class Talkable:
    def talk(self):
        print("Talking")

class Robot(Talkable, Flyable):
    pass

r = Robot()
r.talk()
r.fly()


# Example 3: if both parents have same method name, MRO decides
class A:
    def action(self):
        print("Action from A")

class B:
    def action(self):
        print("Action from B")

class C(A, B):
    pass

obj = C()
obj.action()  # will use A first because C(A, B)


# Example 4: change order of parents changes method resolution
class D(B, A):
    pass

obj2 = D()
obj2.action()  # now B first


# Example 5: practical mixin example (combine features)
class Logger:
    def log(self, msg):
        print("[LOG]", msg)

class GamePlayer(Logger):
    def __init__(self, name):
        self.name = name

    def move(self):
        self.log(self.name + " moved")

gp = GamePlayer("Knight")
gp.move()
