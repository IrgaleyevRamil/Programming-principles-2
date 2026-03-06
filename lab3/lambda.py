"""
Practice 03 - Python Lambda (All in one file)

Topics:
1) Lambda syntax and basic usage
2) Using lambda with map() for transformation
3) Using lambda with filter() for selection
4) Using lambda with sorted() for custom sorting
"""

# =========================================================
# TOPIC 1: Lambda syntax and basic usage (5 examples)
# =========================================================

# Example 1: simplest lambda (one argument)
square = lambda x: x * x
print("Square:", square(5))


# Example 2: lambda with two arguments
add = lambda a, b: a + b
print("Add:", add(3, 7))


# Example 3: lambda inside a function (returns a lambda)
def make_multiplier(k):
    return lambda x: x * k

times3 = make_multiplier(3)
print("Times 3:", times3(10))


# Example 4: conditional lambda (ternary expression)
is_even_text = lambda x: "even" if x % 2 == 0 else "odd"
print("7 is", is_even_text(7))
print("10 is", is_even_text(10))


# Example 5: using lambda as a quick small function (no need to define def)
to_upper = lambda s: s.upper()
print("Upper:", to_upper("kbtu"))


# =========================================================
# TOPIC 2: Using lambda with map() for transformation (5 examples)
# =========================================================

# Example 1: map numbers -> squares
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
print("Squares:", squares)


# Example 2: map numbers -> plus 10
plus10 = list(map(lambda x: x + 10, nums))
print("Plus 10:", plus10)


# Example 3: map strings -> lengths
words = ["python", "js", "html", "css"]
lengths = list(map(lambda w: len(w), words))
print("Lengths:", lengths)


# Example 4: map with two lists (element-wise addition)
a = [1, 2, 3]
b = [10, 20, 30]
sum_lists = list(map(lambda x, y: x + y, a, b))
print("Sum two lists:", sum_lists)


# Example 5: map list of dicts -> extract a field
students = [
    {"name": "Alex", "gpa": 3.2},
    {"name": "Bobby", "gpa": 2.7},
    {"name": "Askhar", "gpa": 3.8}
]
gpas = list(map(lambda s: s["gpa"], students))
print("GPAs:", gpas)


# =========================================================
# TOPIC 3: Using lambda with filter() for selection (5 examples)
# =========================================================

# Example 1: filter even numbers
nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums2))
print("Evens:", evens)


# Example 2: filter numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, nums2))
print("> 5:", greater_than_5)


# Example 3: filter strings that start with 'a' or 'A'
names = ["Aruzhan", "marat", "Askhar", "dias", "Alex"]
starts_with_a = list(filter(lambda s: s.lower().startswith("a"), names))
print("Starts with A:", starts_with_a)


# Example 4: filter dicts by condition (gpa >= 3.0)
good_students = list(filter(lambda s: s["gpa"] >= 3.0, students))
print("Good students:", good_students)


# Example 5: filter non-empty strings
texts = ["hello", "", " ", "kbtu", ""]
non_empty = list(filter(lambda s: s.strip() != "", texts))
print("Non-empty:", non_empty)


# =========================================================
# TOPIC 4: Using lambda with sorted() for custom sorting (5 examples)
# =========================================================

# Example 1: sort numbers by absolute value
nums3 = [3, -10, 2, -1, 7, -5]
sorted_by_abs = sorted(nums3, key=lambda x: abs(x))
print("Sorted by abs:", sorted_by_abs)


# Example 2: sort strings by length
words2 = ["python", "js", "database", "ai", "cloud"]
sorted_by_len = sorted(words2, key=lambda w: len(w))
print("Sorted by length:", sorted_by_len)


# Example 3: sort list of tuples by second element
pairs = [("A", 3), ("B", 1), ("C", 2)]
sorted_by_second = sorted(pairs, key=lambda t: t[1])
print("Sorted by 2nd:", sorted_by_second)


# Example 4: sort dicts by GPA descending
sorted_students_by_gpa = sorted(students, key=lambda s: s["gpa"], reverse=True)
print("Students by GPA desc:", sorted_students_by_gpa)


# Example 5: sort strings by last character
names2 = ["Marat", "Dias", "Aruzhan", "Askhar"]
sorted_by_last_char = sorted(names2, key=lambda s: s[-1])
print("Sorted by last char:", sorted_by_last_char)
