"""
Practice - Move Files

Topics:
1) Move file (shutil.move)
2) Rename file
3) Move to directory
4) Move multiple files
5) Check before move
"""

import shutil
import os


# =========================================================
# TOPIC 1: Move file (shutil.move) (5 examples)
# =========================================================

# Example 1
shutil.move("example.txt", "moved1.txt")

# Example 2
shutil.move("moved1.txt", "moved2.txt")

# Example 3
src = "moved2.txt"
dst = "moved3.txt"
shutil.move(src, dst)

# Example 4
print(shutil.move("moved3.txt", "moved4.txt"))

# Example 5
file = "moved4.txt"
shutil.move(file, "moved5.txt")


# =========================================================
# TOPIC 2: Rename file (5 examples)
# =========================================================

# Example 1
os.rename("moved5.txt", "renamed1.txt")

# Example 2
os.rename("renamed1.txt", "renamed2.txt")

# Example 3
src = "renamed2.txt"
dst = "renamed3.txt"
os.rename(src, dst)

# Example 4
print(os.rename("renamed3.txt", "renamed4.txt"))

# Example 5
file = "renamed4.txt"
os.rename(file, "renamed5.txt")


# =========================================================
# TOPIC 3: Move to directory (5 examples)
# =========================================================

# Example 1
if not os.path.exists("folder"):
    os.mkdir("folder")

shutil.move("renamed5.txt", "folder/file1.txt")

# Example 2
shutil.move("folder/file1.txt", "file2.txt")

# Example 3
shutil.move("file2.txt", "folder/file3.txt")

# Example 4
print(shutil.move("folder/file3.txt", "file4.txt"))

# Example 5
shutil.move("file4.txt", "folder/file5.txt")


# =========================================================
# TOPIC 4: Move multiple files (5 examples)
# =========================================================

# Example 1
files = ["example.txt"]
for f in files:
    if os.path.exists(f):
        shutil.move(f, "multi1.txt")

# Example 2
files = ["multi1.txt"]
for f in files:
    if os.path.exists(f):
        shutil.move(f, "multi2.txt")

# Example 3
files = ["multi2.txt"]
for f in files:
    if os.path.exists(f):
        shutil.move(f, "multi3.txt")

# Example 4
files = ["multi3.txt"]
for f in files:
    if os.path.exists(f):
        shutil.move(f, "multi4.txt")

# Example 5
files = ["multi4.txt"]
for f in files:
    if os.path.exists(f):
        shutil.move(f, "multi5.txt")


# =========================================================
# TOPIC 5: Check before move (5 examples)
# =========================================================

# Example 1
if os.path.exists("multi5.txt"):
    shutil.move("multi5.txt", "final1.txt")

# Example 2
if os.path.exists("final1.txt"):
    shutil.move("final1.txt", "final2.txt")

# Example 3
file = "final2.txt"
if os.path.exists(file):
    shutil.move(file, "final3.txt")

# Example 4
if os.path.exists("final3.txt"):
    print(shutil.move("final3.txt", "final4.txt"))

# Example 5
if not os.path.exists("unknown.txt"):
    print("File not found")