"""
Practical - Built-in Functions
"""

from functools import reduce


nums = [1, 2, 3, 4, 5]


# 1. Use map() and filter()
mapped = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))

print(mapped)
print(filtered)


# 2. Aggregate with reduce()
result = reduce(lambda x, y: x + y, nums)
print(result)


# 3. Use enumerate() and zip()
names = ["A", "B", "C"]
scores = [90, 80, 70]

for i, (n, s) in enumerate(zip(names, scores)):
    print(i, n, s)


# 4. Type checking and conversions
value = "123"

print(type(value))
num = int(value)
print(type(num))

print(float(num))
<<<<<<< HEAD
print(str(num))
=======
print(str(num))
>>>>>>> fef4671481922721041252107e1296e387f800c8
