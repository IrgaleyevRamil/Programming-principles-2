"""
Practice - Directories

Topics:
1) Create directory (os.mkdir)
2) Create nested directories (os.makedirs)
3) List directory contents (os.listdir)
4) Check directory existence
5) Remove directories (os.rmdir)
"""

import os


# =========================================================
# TOPIC 1: Create directory (os.mkdir) (5 examples)
# =========================================================

# Example 1
os.mkdir("dir1")

# Example 2
os.mkdir("dir2")

# Example 3
name = "dir3"
os.mkdir(name)

# Example 4
if not os.path.exists("dir4"):
    os.mkdir("dir4")

# Example 5
os.mkdir("dir5")


# =========================================================
# TOPIC 2: Create nested directories (os.makedirs) (5 examples)
# =========================================================

# Example 1
os.makedirs("folder1/sub1")

# Example 2
os.makedirs("folder2/sub2")

# Example 3
path = "folder3/sub3"
os.makedirs(path)

# Example 4
os.makedirs("folder4/sub4/subsub4")

# Example 5
os.makedirs("folder5/sub5")


# =========================================================
# TOPIC 3: List directory contents (os.listdir) (5 examples)
# =========================================================

# Example 1
print(os.listdir())

# Example 2
print(os.listdir("."))

# Example 3
files = os.listdir()
print(files)

# Example 4
for f in os.listdir():
    print(f)

# Example 5
print(len(os.listdir()))


# =========================================================
# TOPIC 4: Check directory existence (5 examples)
# =========================================================

# Example 1
print(os.path.exists("dir1"))

# Example 2
print(os.path.isdir("dir2"))

# Example 3
if os.path.exists("dir3"):
    print("Exists")

# Example 4
if not os.path.exists("dir100"):
    print("Not exists")

# Example 5
print(os.path.isdir("folder1"))


# =========================================================
# TOPIC 5: Remove directories (os.rmdir) (5 examples)
# =========================================================

# Example 1
if os.path.exists("dir1"):
    os.rmdir("dir1")

# Example 2
if os.path.exists("dir2"):
    os.rmdir("dir2")

# Example 3
name = "dir3"
if os.path.exists(name):
    os.rmdir(name)

# Example 4
if os.path.exists("dir4"):
    os.rmdir("dir4")

# Example 5
if os.path.exists("dir5"):
    os.rmdir("dir5")