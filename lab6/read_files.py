"""
Practice - File Reading Examples

Topics:
1) read()
2) readline()
3) readlines()
4) with statement
5) File modes (r)
"""


# =========================================================
# TOPIC 1: read() (5 examples)
# =========================================================

# Example 1
f = open("example.txt", "r")
print(f.read())
f.close()

# Example 2
f = open("example.txt", "r")
print(f.read(5))
f.close()

# Example 3
f = open("example.txt", "r")
data = f.read()
print(data)
f.close()

# Example 4
f = open("example.txt", "r")
print(len(f.read()))
f.close()

# Example 5
f = open("example.txt", "r")
content = f.read()
print(content.upper())
f.close()


# =========================================================
# TOPIC 2: readline() (5 examples)
# =========================================================

# Example 1
f = open("example.txt", "r")
print(f.readline())
f.close()

# Example 2
f = open("example.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# Example 3
f = open("example.txt", "r")
line = f.readline()
print(line.strip())
f.close()

# Example 4
f = open("example.txt", "r")
print(len(f.readline()))
f.close()

# Example 5
f = open("example.txt", "r")
print(f.readline(10))
f.close()


# =========================================================
# TOPIC 3: readlines() (5 examples)
# =========================================================

# Example 1
f = open("example.txt", "r")
print(f.readlines())
f.close()

# Example 2
f = open("example.txt", "r")
lines = f.readlines()
print(lines[0])
f.close()

# Example 3
f = open("example.txt", "r")
lines = f.readlines()
print(len(lines))
f.close()

# Example 4
f = open("example.txt", "r")
for line in f.readlines():
    print(line.strip())
f.close()

# Example 5
f = open("example.txt", "r")
lines = f.readlines()
print("".join(lines))
f.close()


# =========================================================
# TOPIC 4: with statement (5 examples)
# =========================================================

# Example 1
with open("example.txt", "r") as f:
    print(f.read())

# Example 2
with open("example.txt", "r") as f:
    print(f.readline())

# Example 3
with open("example.txt", "r") as f:
    print(f.readlines())

# Example 4
with open("example.txt", "r") as f:
    data = f.read()
    print(data.lower())

# Example 5
with open("example.txt", "r") as f:
    print(len(f.read()))


# =========================================================
# TOPIC 5: File modes (r) (5 examples)
# =========================================================

# Example 1
f = open("example.txt", "r")
print(f.read())
f.close()

# Example 2
f = open("example.txt", "rt")
print(f.read())
f.close()

# Example 3
f = open("example.txt", "r")
print(f.read(3))
f.close()

# Example 4
f = open("example.txt", "r")
print(f.readline())
f.close()

# Example 5
f = open("example.txt", "r")
print(f.readlines())
f.close()