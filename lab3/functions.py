"""
Practice 03 - Python Functions

Topics:
1) Function definition and calling
2) Function arguments (positional, default, *args, **kwargs)
3) Return values and statements
4) Passing lists and other data types as arguments
5) Function documentation with docstrings
"""

# =========================================================
# TOPIC 1: Function definition and calling (5 examples)
# =========================================================

# Example 1: simplest function (no parameters)
def hello():
    print("Hello!")

hello()  # call the function


# Example 2: function with 1 parameter
def greet(name):
    print("Hi,", name)

greet("Marat")


# Example 3: function that does a small calculation and prints
def square(x):
    print("Square of", x, "=", x * x)

square(7)


# Example 4: function can be called many times with different values
def repeat_word(word, times):
    for _ in range(times):
        print(word)

repeat_word("Study", 3)


# Example 5: function that uses local variables inside
def show_total_price():
    price = 1200
    count = 3
    print("Total price:", price * count)

show_total_price()


# =========================================================
# TOPIC 2: Function arguments (positional, default, *args, **kwargs) (5 examples)
# =========================================================

# Example 1: positional arguments (order matters)
def subtract(a, b):
    print("a - b =", a - b)

subtract(10, 3)


# Example 2: default argument (if not provided, default is used)
def welcome(user="Guest"):
    print("Welcome,", user)

welcome()
welcome("Aruzhan")


# Example 3: keyword arguments (we can specify names)
def student_info(name, gpa):
    print("Name:", name, "| GPA:", gpa)

student_info(gpa=3.4, name="Dias")


# Example 4: *args (any amount of positional arguments)
def sum_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    print("Sum:", total)

sum_numbers(1, 2, 3)
sum_numbers(10, 20, 30, 40)


# Example 5: **kwargs (any amount of keyword arguments)
def show_data(**data):
    for key in data:
        print(key, "->", data[key])

show_data(city="Almaty", uni="KBTU", year=2026)


# =========================================================
# TOPIC 3: Return values and statements (5 examples)
# =========================================================

# Example 1: return a value
def add(a, b):
    return a + b

result = add(5, 9)
print("Add result:", result)


# Example 2: return a boolean using condition
def is_positive(x):
    if x > 0:
        return True
    return False

print("Is 7 positive?", is_positive(7))
print("Is -2 positive?", is_positive(-2))


# Example 3: return early (stop the function earlier)
def check_age(age):
    if age < 18:
        return "Under 18"
    return "18 or older"

print(check_age(16))
print(check_age(20))


# Example 4: return multiple values (tuple)
def calc_stats(nums):
    return min(nums), max(nums), sum(nums)

mn, mx, total = calc_stats([3, 10, 7, 1])
print("Min:", mn, "| Max:", mx, "| Sum:", total)


# Example 5: return None (no return statement)
def print_warning(text):
    print("WARNING:", text)

x = print_warning("Low battery")
print("Returned:", x)  # None


# =========================================================
# TOPIC 4: Passing lists and other data types as arguments (5 examples)
# =========================================================

# Example 1: list argument
def print_items(items):
    for it in items:
        print("Item:", it)

print_items(["pen", "book", "laptop"])


# Example 2: list argument + return average
def average(nums):
    return sum(nums) / len(nums)

print("Average:", average([10, 20, 30, 40]))


# Example 3: string argument (count vowels)
def count_vowels(text):
    vowels = "aeiouAEIOU"
    cnt = 0
    for ch in text:
        if ch in vowels:
            cnt += 1
    return cnt

print("Vowels in 'Hello':", count_vowels("Hello"))


# Example 4: dictionary argument (print key-value)
def show_grades(grades):
    for name in grades:
        print(name, "=", grades[name])

show_grades({"Alex": 85, "Bobby": 72, "Askhar": 93})


# Example 5: function as argument (apply operation)
def apply_operation(func, x, y):
    return func(x, y)

def multiply(a, b):
    return a * b

print("Operation result:", apply_operation(multiply, 6, 7))


# =========================================================
# TOPIC 5: Function documentation with docstrings (5 examples)
# =========================================================

# Example 1: basic docstring
def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b

print(power(2, 5))
print("Doc:", power.__doc__)


# Example 2: docstring with parameters
def full_name(first, last):
    """
    Combines first name and last name.

    first: string
    last: string
    """
    return first + " " + last

print(full_name("John", "Wick"))


# Example 3: docstring describing return
def absolute_value(x):
    """
    Returns absolute value of x.
    If x < 0, returns -x, otherwise returns x.
    """
    if x < 0:
        return -x
    return x

print(absolute_value(-9))
print(absolute_value(4))


# Example 4: docstring for list processing
def top_score(scores):
    """
    Returns the maximum score from the list.
    scores: list of numbers
    """
    return max(scores)

print(top_score([55, 70, 99, 80]))


# Example 5: docstring for *args
def multiply_all(*nums):
    """
    Multiplies all numbers passed to the function.
    Accepts any number of arguments using *args.
    """
    result = 1
    for n in nums:
        result *= n
    return result

print(multiply_all(2, 3, 4))
