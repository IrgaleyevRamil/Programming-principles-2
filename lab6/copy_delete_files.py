"""
Practice - Copy and Delete Files

Topics:
1) Copy files (shutil.copy)
2) Copy with metadata (shutil.copy2)
3) Move files (shutil.move)
4) Delete files (os.remove)
5) Check file existence (os.path.exists)
"""

import shutil
import os


# =========================================================
# TOPIC 1: Copy files (shutil.copy) (5 examples)
# =========================================================

# Example 1
shutil.copy("example.txt", "copy1.txt")

# Example 2
shutil.copy("example.txt", "copy2.txt")

# Example 3
src = "example.txt"
dst = "copy3.txt"
shutil.copy(src, dst)

# Example 4
print(shutil.copy("example.txt", "copy4.txt"))

# Example 5
file = "example.txt"
shutil.copy(file, "copy5.txt")


# =========================================================
# TOPIC 2: Copy with metadata (shutil.copy2) (5 examples)
# =========================================================

# Example 1
shutil.copy2("example.txt", "meta1.txt")

# Example 2
shutil.copy2("example.txt", "meta2.txt")

# Example 3
src = "example.txt"
dst = "meta3.txt"
shutil.copy2(src, dst)

# Example 4
print(shutil.copy2("example.txt", "meta4.txt"))

# Example 5
shutil.copy2("example.txt", "meta5.txt")


# =========================================================
# TOPIC 3: Move files (shutil.move) (5 examples)
# =========================================================

# Example 1
shutil.move("copy1.txt", "moved1.txt")

# Example 2
shutil.move("copy2.txt", "moved2.txt")

# Example 3
src = "copy3.txt"
dst = "moved3.txt"
shutil.move(src, dst)

# Example 4
print(shutil.move("copy4.txt", "moved4.txt"))

# Example 5
shutil.move("copy5.txt", "moved5.txt")


# =========================================================
# TOPIC 4: Delete files (os.remove) (5 examples)
# =========================================================

# Example 1
if os.path.exists("moved1.txt"):
    os.remove("moved1.txt")

# Example 2
if os.path.exists("moved2.txt"):
    os.remove("moved2.txt")

# Example 3
file = "moved3.txt"
if os.path.exists(file):
    os.remove(file)

# Example 4
if os.path.exists("moved4.txt"):
    os.remove("moved4.txt")

# Example 5
if os.path.exists("moved5.txt"):
    os.remove("moved5.txt")


# =========================================================
# TOPIC 5: Check file existence (os.path.exists) (5 examples)
# =========================================================

# Example 1
print(os.path.exists("example.txt"))

# Example 2
print(os.path.exists("unknown.txt"))

# Example 3
file = "meta1.txt"
print(os.path.exists(file))

# Example 4
if os.path.exists("meta2.txt"):
    print("File exists")

# Example 5
if not os.path.exists("no_file.txt"):
    print("File not found")