"""
Practical - Directories
"""

import os
import shutil


# 1. Create nested directories
os.makedirs("main_dir/sub_dir", exist_ok=True)


# 2. List files and folders
print(os.listdir())


# 3. Find files by extension
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)


# 4. Move/copy files between directories
if os.path.exists("task.txt"):
    shutil.copy("task.txt", "main_dir/sub_dir/task_copy.txt")

if os.path.exists("task.txt"):
<<<<<<< HEAD
    shutil.move("task.txt", "main_dir/task_moved.txt")
=======
    shutil.move("task.txt", "main_dir/task_moved.txt")
>>>>>>> fef4671481922721041252107e1296e387f800c8
