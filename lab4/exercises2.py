# =========================================================
# TASK 1: Generator that generates squares up to N
# =========================================================

def square_up_to(n):
    for i in range(n + 1):
        yield i * i

print("Squares up to 5:")
for num in square_up_to(5):
    print(num)


# =========================================================
# TASK 2: Print even numbers between 0 and n (comma separated)
# =========================================================

n = int(input("Enter n for even numbers: "))

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print("Even numbers:")
print(",".join(str(x) for x in even_numbers(n)))


# =========================================================
# TASK 3: Numbers divisible by 3 and 4 between 0 and n
# =========================================================

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Divisible by 3 and 4 up to 50:")
for num in divisible_by_3_and_4(50):
    print(num)


# =========================================================
# TASK 4: Generator squares from a to b
# =========================================================

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

print("Squares from 3 to 7:")
for value in squares(3, 7):
    print(value)


# =========================================================
# TASK 5: Generator that returns numbers from n down to 0
# =========================================================

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("Countdown from 5:")
for num in countdown(5):
    print(num)