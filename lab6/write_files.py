"""
Practice - File Writing Examples

Topics:
1) write()
2) writelines()
3) append mode (a)
4) with statement (writing)
5) overwrite file (w)
"""


# =========================================================
# TOPIC 1: write() (5 examples)
# =========================================================

# Example 1
f = open("example.txt", "w")
f.write("Hello World")
f.close()

# Example 2
f = open("example.txt", "w")
f.write("Python\n")
f.write("is cool")
f.close()

# Example 3
f = open("example.txt", "w")
text = "Writing to file"
f.write(text)
f.close()

# Example 4
f = open("example.txt", "w")
print(f.write("12345"))
f.close()

# Example 5
f = open("example.txt", "w")
f.write("Line 1\nLine 2\nLine 3")
f.close()


# =========================================================
# TOPIC 2: writelines() (5 examples)
# =========================================================

# Example 1
f = open("example.txt", "w")
f.writelines(["A\n", "B\n", "C\n"])
f.close()

# Example 2
f = open("example.txt", "w")
lines = ["Hello\n", "World\n"]
f.writelines(lines)
f.close()

# Example 3
f = open("example.txt", "w")
f.writelines(["1\n", "2\n", "3\n"])
f.close()

# Example 4
f = open("example.txt", "w")
data = ["Python\n", "Java\n", "C++\n"]
f.writelines(data)
f.close()

# Example 5
f = open("example.txt", "w")
f.writelines(["First\n", "Second\n", "Third\n"])
f.close()


# =========================================================
# TOPIC 3: append mode (a) (5 examples)
# =========================================================

# Example 1
f = open("example.txt", "a")
f.write("\nNew line")
f.close()

# Example 2
f = open("example.txt", "a")
f.write("\nAppend text")
f.close()

# Example 3
f = open("example.txt", "a")
f.writelines(["\nA", "\nB"])
f.close()

# Example 4
f = open("example.txt", "a")
f.write("\n123")
f.close()

# Example 5
f = open("example.txt", "a")
f.write("\nEnd")
f.close()


# =========================================================
# TOPIC 4: with statement (writing) (5 examples)
# =========================================================

# Example 1
with open("example.txt", "w") as f:
    f.write("Hello")

# Example 2
with open("example.txt", "w") as f:
    f.write("Python")

# Example 3
with open("example.txt", "a") as f:
    f.write("\nAppend")

# Example 4
with open("example.txt", "w") as f:
    f.writelines(["A\n", "B\n"])

# Example 5
with open("example.txt", "a") as f:
    f.write("\nDone")


# =========================================================
# TOPIC 5: overwrite file (w) (5 examples)
# =========================================================

# Example 1
f = open("example.txt", "w")
f.write("New content")
f.close()

# Example 2
f = open("example.txt", "w")
f.write("Overwrite again")
f.close()

# Example 3
f = open("example.txt", "w")
f.write("123")
f.close()

# Example 4
f = open("example.txt", "w")
f.write("Reset file")
f.close()

# Example 5
f = open("example.txt", "w")
f.write("Final version")
f.close()