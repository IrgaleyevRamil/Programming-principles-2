"""
Practice - Python RegEx examples

Topics:
1) RegEx Introduction
2) RegEx Syntax and Metacharacters
3) Special Sequences
4) Sets and Character Classes
5) Quantifiers
6) re.search() – Find first match
7) re.findall() – Find all matches
8) re.split() – Split strings
9) re.sub() – Replace patterns
10) re.match() – Match at beginning
11) Flags
"""

import re


# =========================================================
# TOPIC 1: RegEx Introduction (5 examples)
# =========================================================

# Example 1
text = "Python regex is useful"
print(re.search("Python", text))

# Example 2
print(re.search("regex", text))

# Example 3
print(re.search("use", text))

# Example 4
print(re.search("is", text))

# Example 5
print(re.search("Java", text))


# =========================================================
# TOPIC 2: RegEx Syntax and Metacharacters (5 examples)
# =========================================================

# Example 1
text = "hat hot hit"
print(re.findall("h.t", text))

# Example 2
print(re.findall("h.*t", text))

# Example 3
print(re.findall("^hat", text))

# Example 4
print(re.findall("t$", "cat bat hat"))

# Example 5
print(re.findall("(hat|hot)", text))


# =========================================================
# TOPIC 3: Special Sequences (5 examples)
# =========================================================

# Example 1
text = "User123 score456"
print(re.findall(r"\d+", text))

# Example 2
print(re.findall(r"\w+", text))

# Example 3
print(re.findall(r"\s", "Python is fun"))

# Example 4
print(re.findall(r"\D+", "123abc456"))

# Example 5
print(re.findall(r"\W", "hello@world!"))


# =========================================================
# TOPIC 4: Sets and Character Classes (5 examples)
# =========================================================

# Example 1
text = "abc123XYZ"
print(re.findall("[a-z]", text))

# Example 2
print(re.findall("[A-Z]", text))

# Example 3
print(re.findall("[0-9]", text))

# Example 4
print(re.findall("[a-zA-Z]", text))

# Example 5
print(re.findall("[^0-9]", text))


# =========================================================
# TOPIC 5: Quantifiers (5 examples)
# =========================================================

# Example 1
text = "a aa aaa aaaa"
print(re.findall(r"a{2}", text))

# Example 2
print(re.findall(r"a{2,}", text))

# Example 3
print(re.findall(r"\d{3}", "123 45 6789"))

# Example 4
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))

# Example 5
print(re.findall(r"a+", text))


# =========================================================
# TOPIC 6: re.search() – Find first match (5 examples)
# =========================================================

# Example 1
text = "Python is powerful"
print(re.search("Python", text))

# Example 2
print(re.search("power", text))

# Example 3
print(re.search("is", text))

# Example 4
print(re.search("Java", text))

# Example 5
print(re.search("ful", text))


# =========================================================
# TOPIC 7: re.findall() – Find all matches (5 examples)
# =========================================================

# Example 1
text = "10 20 30 40"
print(re.findall(r"\d+", text))

# Example 2
print(re.findall(r"\d{2}", text))

# Example 3
print(re.findall(r"[0-9]", text))

# Example 4
print(re.findall(r"\d", text))

# Example 5
print(re.findall(r"\d{1,2}", text))


# =========================================================
# TOPIC 8: re.split() – Split strings (5 examples)
# =========================================================

# Example 1
print(re.split(r"\s", "Python is very powerful"))

# Example 2
print(re.split(",", "apple,banana,orange"))

# Example 3
print(re.split("-", "2026-03-06"))

# Example 4
print(re.split(r"\d", "a1b2c3"))

# Example 5
print(re.split(r"\s", "one two three four"))


# =========================================================
# TOPIC 9: re.sub() – Replace patterns (5 examples)
# =========================================================

# Example 1
text = "My number is 12345"
print(re.sub(r"\d", "*", text))

# Example 2
print(re.sub("number", "phone", text))

# Example 3
print(re.sub(r"\s", "-", text))

# Example 4
print(re.sub(r"\d+", "NUM", text))

# Example 5
print(re.sub("My", "Your", text))


# =========================================================
# TOPIC 10: re.match() – Match at beginning (5 examples)
# =========================================================

# Example 1
text = "Python programming"
print(re.match("Python", text))

# Example 2
print(re.match("programming", text))

# Example 3
print(re.match("Py", text))

# Example 4
print(re.match("Java", text))

# Example 5
print(re.match(r"\w+", text))


# =========================================================
# TOPIC 11: Flags (5 examples)
# =========================================================

# Example 1
text = "python PYTHON Python"
print(re.findall("python", text))

# Example 2
print(re.findall("python", text, re.IGNORECASE))

# Example 3
multi = "Start\n123\n456\nEnd"
print(re.findall(r"^\d+", multi, re.MULTILINE))

# Example 4
print(re.findall("start", "Start here", re.IGNORECASE))

# Example 5
print(re.findall(r".+", multi))