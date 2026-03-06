# FOR LOOPS
# Example 1
for i in range(5):
    # prints numbers from 0 to 4
    print(i)

# Example 2
for i in range(1, 6):
    # prints numbers from 1 to 5
    print(i)

# Example 3
for letter in "Python":
    # iterates through each character in the string
    print(letter)

# Example 4
numbers = [1, 2, 3, 4]
for n in numbers:
    # prints each number from the list
    print(n)

# Example 5
for i in range(0, 10, 2):
    # prints even numbers from 0 to 8
    print(i)


# FOR LOOP WITH BREAK
# Example 1
for i in range(1, 10):
    # stops loop when i equals 5
    if i == 5:
        break
    print(i)

# Example 2
for letter in "Hello":
    # breaks loop when letter is 'l'
    if letter == "l":
        break
    print(letter)

# Example 3
numbers = [3, 6, 9, 12]
for n in numbers:
    # stops loop when number equals 9
    if n == 9:
        break
    print(n)

# Example 4
for i in range(10):
    # breaks loop when i is greater than 3
    if i > 3:
        break
    print("Value:", i)

# Example 5
for i in range(5):
    # loop runs only once because of break
    print(i)
    break


# FOR LOOP WITH CONTINUE
# Example 1
for i in range(5):
    # skips printing when i equals 2
    if i == 2:
        continue
    print(i)

# Example 2
for i in range(1, 8):
    # skips even numbers
    if i % 2 == 0:
        continue
    print(i)

# Example 3
for letter in "Python":
    # skips the letter 'o'
    if letter == "o":
        continue
    print(letter)

# Example 4
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    # skips number 3
    if n == 3:
        continue
    print(n)

# Example 5
for i in range(6):
    # skips numbers less than 3
    if i < 3:
        continue
    print("Number:", i)
