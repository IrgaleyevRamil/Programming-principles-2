"""
Practice - Iterators and Generators

Topics:
1) iter() and next()
2) Looping through iterator manually
3) Creating custom iterator
4) Generator functions (yield)
5) Generator expressions
"""

# =========================================================
# TOPIC 1: iter() and next() (5 examples)
# =========================================================

# Example 1
nums = [1, 2, 3]
it = iter(nums)
print(next(it))

# Example 2
letters = ["a", "b", "c"]
it2 = iter(letters)
print(next(it2))
print(next(it2))

# Example 3
string = "abc"
it3 = iter(string)
print(next(it3))

# Example 4
tuple_data = (10, 20)
it4 = iter(tuple_data)
print(next(it4))

# Example 5
set_data = {100, 200}
it5 = iter(set_data)
print(next(it5))


# =========================================================
# TOPIC 2: Looping through iterator manually (5 examples)
# =========================================================

# Example 1
nums = [5, 6, 7]
it = iter(nums)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# Example 2
text = "hi"
it = iter(text)
for char in it:
    print(char)

# Example 3
data = [10, 20]
it = iter(data)
print(next(it))
print(next(it))

# Example 4
names = ["Ali", "Dana"]
for n in iter(names):
    print(n)

# Example 5
nums = range(3)
for n in iter(nums):
    print(n)


# =========================================================
# TOPIC 3: Creating custom iterator (5 examples)
# =========================================================

# Example 1
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for n in CountUp(3):
    print(n)


# Example 2
class EvenNumbers:
    def __init__(self, max_val):
        self.max = max_val
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num <= self.max:
            return self.num
        else:
            raise StopIteration

for e in EvenNumbers(6):
    print(e)


# Example 3
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.data[self.index]
        else:
            raise StopIteration

for x in Reverse("abc"):
    print(x)


# Example 4
class Squares:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i ** 2
        else:
            raise StopIteration

for s in Squares(4):
    print(s)


# Example 5
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            self.current -= 1
            return self.current
        else:
            raise StopIteration

for c in Countdown(3):
    print(c)


# =========================================================
# TOPIC 4: Generator functions (yield) (5 examples)
# =========================================================

# Example 1
def gen_numbers():
    yield 1
    yield 2
    yield 3

for x in gen_numbers():
    print(x)


# Example 2
def gen_squares(n):
    for i in range(n):
        yield i * i

for x in gen_squares(4):
    print(x)


# Example 3
def gen_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for x in gen_even(6):
    print(x)


# Example 4
def gen_reverse(text):
    for i in range(len(text)-1, -1, -1):
        yield text[i]

for ch in gen_reverse("hello"):
    print(ch)


# Example 5
def gen_multiply(n):
    for i in range(1, 6):
        yield i * n

for x in gen_multiply(3):
    print(x)


# =========================================================
# TOPIC 5: Generator expressions (5 examples)
# =========================================================

# Example 1
gen1 = (x for x in range(5))
for x in gen1:
    print(x)

# Example 2
gen2 = (x * 2 for x in range(4))
for x in gen2:
    print(x)

# Example 3
gen3 = (x ** 2 for x in range(3))
print(list(gen3))

# Example 4
gen4 = (c.upper() for c in "abc")
print(list(gen4))

# Example 5
gen5 = (x for x in range(10) if x % 3 == 0)
print(list(gen5))