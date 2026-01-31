# WHILE LOOP
# Example 1
i = 1
while i <= 5:
    # prints numbers from 1 to 5
    print(i)
    i += 1

# Example 2
count = 0
while count < 3:
    # prints "Hello" three times
    print("Hello")
    count += 1

# Example 3
x = 10
while x > 0:
    # decreases x by 2 each loop
    print(x)
    x -= 2

# Example 4
number = 1
while number <= 10:
    # prints numbers from 1 to 10
    print(number)
    number += 1

# Example 5
flag = True
while flag:
    # loop runs only once
    print("Loop is running")
    flag = False


# WHILE LOOP WITH BREAK
# Example 1
i = 1
while True:
    # stops loop when i equals 5
    print(i)
    if i == 5:
        break
    i += 1

# Example 2
x = 0
while x < 10:
    # breaks loop when x is 4
    if x == 4:
        break
    print(x)
    x += 1

# Example 3
password = ""
while True:
    # exits loop when password is correct
    password = "1234"
    if password == "1234":
        print("Correct password")
        break

# Example 4
count = 1
while count <= 10:
    # breaks loop when count reaches 6
    if count == 6:
        break
    print(count)
    count += 1

# Example 5
i = 0
while i < 5:
    # breaks loop immediately
    print("Checking...")
    break


# WHILE LOOP WITH CONTINUE
# Example 1
i = 0
while i < 5:
    i += 1
    # skips printing when i equals 3
    if i == 3:
        continue
    print(i)

# Example 2
number = 0
while number < 6:
    number += 1
    # skips even numbers
    if number % 2 == 0:
        continue
    print(number)

# Example 3
i = 0
while i < 5:
    i += 1
    # skips value 4
    if i == 4:
        continue
    print("Value:", i)

# Example 4
x = 0
while x < 5:
    x += 1
    # skips value 2
    if x == 2:
        continue
    print(x)

# Example 5
i = 0
while i < 4:
    i += 1
    # skips value 1
    if i == 1:
        continue
    print("Loop:", i)
