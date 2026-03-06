import math


# =========================================================
# TASK 1: Convert degree to radian
# =========================================================

degree = 15
radian = math.radians(degree)

print("Input degree:", degree)
print("Output radian:", round(radian, 6))


# =========================================================
# TASK 2: Area of a trapezoid
# =========================================================

height = 5
base1 = 5
base2 = 6

area_trapezoid = (base1 + base2) * height / 2

print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area_trapezoid)


# =========================================================
# TASK 3: Area of regular polygon
# =========================================================

n = 4
side = 25

area_polygon = (n * side ** 2) / (4 * math.tan(math.pi / n))

print("Input number of sides:", n)
print("Input the length of a side:", side)
print("The area of the polygon is:", int(area_polygon))


# =========================================================
# TASK 4: Area of a parallelogram
# =========================================================

base = 5
height_par = 6

area_parallelogram = base * height_par

print("Length of base:", base)
print("Height of parallelogram:", height_par)
print("Expected Output:", float(area_parallelogram))