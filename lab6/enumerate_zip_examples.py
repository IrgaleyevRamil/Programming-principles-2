"""
Practice - Enumerate and Zip

Topics:
1) enumerate()
2) enumerate with start
3) zip()
4) unzip()
5) combined usage
"""


# =========================================================
# TOPIC 1: enumerate() (5 examples)
# =========================================================

# Example 1
nums = [10, 20, 30]
for i, val in enumerate(nums):
    print(i, val)

# Example 2
names = ["A", "B", "C"]
print(list(enumerate(names)))

# Example 3
for i, val in enumerate(["x", "y", "z"]):
    print(i, val)

# Example 4
data = ["apple", "banana"]
print(list(enumerate(data)))

# Example 5
for i, val in enumerate([1, 2]):
    print(i, val)


# =========================================================
# TOPIC 2: enumerate with start (5 examples)
# =========================================================

# Example 1
nums = [10, 20, 30]
for i, val in enumerate(nums, start=1):
    print(i, val)

# Example 2
names = ["A", "B"]
print(list(enumerate(names, start=5)))

# Example 3
for i, val in enumerate(["x", "y"], start=10):
    print(i, val)

# Example 4
data = ["apple", "banana"]
print(list(enumerate(data, start=2)))

# Example 5
for i, val in enumerate([1, 2], start=100):
    print(i, val)


# =========================================================
# TOPIC 3: zip() (5 examples)
# =========================================================

# Example 1
a = [1, 2, 3]
b = ["a", "b", "c"]
print(list(zip(a, b)))

# Example 2
x = [10, 20]
y = [30, 40]
print(list(zip(x, y)))

# Example 3
names = ["A", "B"]
scores = [90, 80]
for n, s in zip(names, scores):
    print(n, s)

# Example 4
print(list(zip([1, 2], [3, 4])))

# Example 5
print(list(zip("ab", [1, 2])))


# =========================================================
# TOPIC 4: unzip() (5 examples)
# =========================================================

# Example 1
pairs = [(1, "a"), (2, "b")]
x, y = zip(*pairs)
print(x, y)

# Example 2
pairs = [(10, 20), (30, 40)]
a, b = zip(*pairs)
print(a, b)

# Example 3
pairs = [("A", 1), ("B", 2)]
letters, nums = zip(*pairs)
print(letters, nums)

# Example 4
pairs = [(1, 2), (3, 4)]
p, q = zip(*pairs)
print(p, q)

# Example 5
pairs = [(5, 6), (7, 8)]
u, v = zip(*pairs)
print(u, v)


# =========================================================
# TOPIC 5: combined usage (5 examples)
# =========================================================

# Example 1
names = ["A", "B", "C"]
scores = [90, 80, 70]
for i, (n, s) in enumerate(zip(names, scores)):
    print(i, n, s)

# Example 2
nums = [1, 2, 3]
letters = ["a", "b", "c"]
print(list(enumerate(zip(nums, letters))))

# Example 3
pairs = list(zip([1, 2], [3, 4]))
for i, (a, b) in enumerate(pairs):
    print(i, a, b)

# Example 4
data = zip(["x", "y"], [10, 20])
for i, (a, b) in enumerate(data, start=1):
    print(i, a, b)

# Example 5
names = ["A", "B"]
scores = [100, 200]
result = list(enumerate(zip(names, scores), start=1))
print(result)