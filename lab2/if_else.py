# IF STATEMENT
# Example 1
x = 10
if x > 5:
    # checks if x is greater than 5
    print("x is greater than 5")

# Example 2
age = 18
if age >= 18:
    # checks if age is 18 or more
    print("You are an adult")

# Example 3
is_student = True
if is_student:
    # checks student status
    print("Student access granted")

# Example 4
temperature = 25
if temperature > 20:
    # checks if temperature is warm
    print("It is warm")

# Example 5
logged_in = False
if not logged_in:
    # runs when user is not logged in
    print("Please log in")


# IF ELSE
# Example 1
x = 3
if x > 5:
    # runs if x is greater than 5
    print("x is greater than 5")
else:
    # runs if condition is false
    print("x is 5 or less")

# Example 2
age = 16
if age >= 18:
    # checks adult age
    print("Adult")
else:
    # runs if under 18
    print("student")

# Example 3
password_correct = False
if password_correct:
    # access allowed
    print("Access granted")
else:
    # access denied
    print("Access denied")

# Example 4
number = 4
if number % 2 == 0:
    # checks if number is even
    print("Even number")
else:
    # number is odd
    print("Odd number")

# Example 5
weather = "rain"
if weather == "sun":
    # condition for good weather
    print("Go for a walk")
else:
    # bad weather case
    print("Stay at home")


# IF ELIF ELSE
# Example 1
score = 85
if score >= 90:
    # highest grade
    print("Grade A")
elif score >= 75:
    # medium grade
    print("Grade B")
else:
    # lowest grade
    print("Grade C")

# Example 2
temperature = 10
if temperature > 20:
    # hot weather
    print("Hot")
elif temperature > 10:
    # warm weather
    print("Warm")
else:
    # cold weather
    print("Cold")

# Example 3
age = 12
if age >= 18:
    # adult category
    print("Adult")
elif age >= 13:
    # teenager category
    print("Teenager")
else:
    # child category
    print("Child")

# Example 4
day = "Saturday"
if day == "Monday":
    # working day
    print("Work day")
elif day == "Saturday":
    # weekend day
    print("Weekend")
else:
    # other days
    print("Another day")

# Example 5
number = 0
if number > 0:
    # positive number
    print("Positive")
elif number < 0:
    # negative number
    print("Negative")
else:
    # number equals zero
    print("Zero")


# SHORT HAND IF ELSE
# Example 1
a = 10
# short form condition check
print("Greater than 5" if a > 5 else "5 or less")

# Example 2
age = 18
# assigns status based on age
status = "Adult" if age >= 18 else "Minor"
print(status)

# Example 3
number = 7
# checks even or odd using short if
print("Even" if number % 2 == 0 else "Odd")

# Example 4
is_logged = False
# shows message based on login state
message = "Welcome" if is_logged else "Please log in"
print(message)

# Example 5
temperature = 15
# assigns weather description
weather = "Warm" if temperature > 20 else "Cold"
print(weather)


# SWITCH / IF ELIF ELSE
# Example 1
day = 3
# prints day name based on number
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Unknown day")

# Example 2
grade = 90
# determines letter grade
if grade >= 90:
    print("A")
elif grade >= 75:
    print("B")
elif grade >= 60:
    print("C")
else:
    print("F")

# Example 3
command = "start"
# handles command input
if command == "start":
    print("Starting...")
elif command == "stop":
    print("Stopping...")
else:
    print("Unknown command")
