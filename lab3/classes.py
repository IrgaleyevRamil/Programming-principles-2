"""
Practice 03 - Python Classes and Objects (All in one file)

Topics:
1) Class definition and object creation
2) The __init__() constructor method
3) Instance methods and the self parameter
4) Class variables vs instance variables (+ modifying/deleting properties)
"""

# =========================================================
# TOPIC 1: Class definition and object creation (5 examples)
# =========================================================

# Example 1: simplest class + creating object
class Empty:
    pass

a = Empty()
print("Empty object:", a)


# Example 2: class with attribute set after creation
class Box:
    pass

b = Box()
b.color = "red"
print("Box color:", b.color)


# Example 3: two objects of same class can have different attributes
c1 = Box()
c2 = Box()
c1.size = "small"
c2.size = "large"
print("c1 size:", c1.size)
print("c2 size:", c2.size)


# Example 4: class with a simple method
class Lamp:
    def turn_on(self):
        print("Lamp is ON")

lamp = Lamp()
lamp.turn_on()


# Example 5: object stored in a list
lamps = [Lamp(), Lamp(), Lamp()]
for i in range(len(lamps)):
    print("Lamp", i + 1)
    lamps[i].turn_on()


# =========================================================
# TOPIC 2: The __init__() constructor method (5 examples)
# =========================================================

# Example 1: __init__ sets instance attributes
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Marat")
print("Person name:", p.name)


# Example 2: __init__ with multiple parameters
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(3, 7)
print("Point:", pt.x, pt.y)


# Example 3: default values in __init__
class GameCharacter:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

g1 = GameCharacter("Knight")
g2 = GameCharacter("Mage", 70)
print(g1.name, g1.hp)
print(g2.name, g2.hp)


# Example 4: __init__ can do small validation
class AgeUser:
    def __init__(self, age):
        if age < 0:
            age = 0
        self.age = age

u = AgeUser(-5)
print("Age:", u.age)


# Example 5: __init__ can create derived attributes
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.area = w * h

r = Rectangle(4, 6)
print("Area:", r.area)


# =========================================================
# TOPIC 3: Instance methods and the self parameter (5 examples)
# =========================================================

# Example 1: method uses self fields
class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

cnt = Counter()
cnt.inc()
cnt.inc()
print("Counter:", cnt.value)


# Example 2: method with parameter + returns value
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print("Calc add:", calc.add(5, 9))


# Example 3: method changes object state
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.balance)


# Example 4: method calls another method using self
class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def add_seconds(self, x):
        self.seconds += x

    def add_minute(self):
        self.add_seconds(60)

t = Timer(30)
t.add_minute()
print("Timer seconds:", t.seconds)


# Example 5: method returns formatted string (like __str__ but simple)
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def info(self):
        return "Student: " + self.name + ", GPA: " + str(self.gpa)

s = Student("Askhar", 3.6)
print(s.info())


# =========================================================
# TOPIC 4: Class variables vs instance variables (+ modifying/deleting properties) (5 examples)
# =========================================================

# Example 1: class variable shared for all objects
class School:
    university = "KBTU"

st1 = School()
st2 = School()
print("st1 uni:", st1.university)
print("st2 uni:", st2.university)


# Example 2: instance variable belongs to each object
class Car:
    brand = "Unknown"

    def __init__(self, model):
        self.model = model

car1 = Car("Camry")
car2 = Car("Civic")
print("Brand:", car1.brand, "| Model:", car1.model)
print("Brand:", car2.brand, "| Model:", car2.model)


# Example 3: changing class variable affects all (unless overridden)
Car.brand = "Toyota"
print("car1 brand:", car1.brand)
print("car2 brand:", car2.brand)


# Example 4: overriding class variable for one object (creates instance attribute)
car2.brand = "Honda"
print("car1 brand:", car1.brand)
print("car2 brand:", car2.brand)


# Example 5: modifying and deleting object properties
class Profile:
    def __init__(self, name):
        self.name = name

pr = Profile("Marat")
print("Name:", pr.name)

pr.name = "Marat Updated"
print("Updated name:", pr.name)

pr.age = 18
print("Added new field age:", pr.age)

del pr.age
print("Deleted age field")
