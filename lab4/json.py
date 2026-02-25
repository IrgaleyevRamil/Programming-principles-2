"""
Practice - JSON parsing and creation

Topics:
1) json.dumps() – Python → JSON string
2) json.loads() – JSON string → Python
3) Writing JSON to file
4) Reading JSON from file
5) Working with structured JSON data
"""

import json


# =========================================================
# TOPIC 1: json.dumps() – Python → JSON string (5 examples)
# =========================================================

# Example 1
data1 = {"name": "Marat", "age": 18}
json_str1 = json.dumps(data1)
print("JSON string:", json_str1)

# Example 2
data2 = [1, 2, 3, 4]
print(json.dumps(data2))

# Example 3
data3 = {"active": True, "score": 99.5}
print(json.dumps(data3))

# Example 4
data4 = {"city": "Almaty"}
print(json.dumps(data4, indent=4))

# Example 5
data5 = {"a": 1, "b": 2}
print(json.dumps(data5, separators=(",", ":")))


# =========================================================
# TOPIC 2: json.loads() – JSON string → Python (5 examples)
# =========================================================

# Example 1
s1 = '{"name": "Dana", "age": 20}'
obj1 = json.loads(s1)
print(obj1["name"])

# Example 2
s2 = '[10, 20, 30]'
obj2 = json.loads(s2)
print(obj2[1])

# Example 3
s3 = '{"flag": true}'
obj3 = json.loads(s3)
print(obj3["flag"])

# Example 4
s4 = '{"numbers": [1, 2, 3]}'
obj4 = json.loads(s4)
print(obj4["numbers"])

# Example 5
s5 = '{"nested": {"x": 5}}'
obj5 = json.loads(s5)
print(obj5["nested"]["x"])


# =========================================================
# TOPIC 3: Writing JSON to file (5 examples)
# =========================================================

# Example 1
data = {"product": "Laptop", "price": 1200}
with open("output1.json", "w") as f:
    json.dump(data, f)

# Example 2
data = [1, 2, 3]
with open("output2.json", "w") as f:
    json.dump(data, f)

# Example 3
data = {"user": "Ali", "gpa": 3.5}
with open("output3.json", "w") as f:
    json.dump(data, f, indent=4)

# Example 4
data = {"status": "ok"}
with open("output4.json", "w") as f:
    json.dump(data, f)

# Example 5
data = {"list": ["a", "b", "c"]}
with open("output5.json", "w") as f:
    json.dump(data, f)


# =========================================================
# TOPIC 4: Reading JSON from file (5 examples)
# =========================================================

# Example 1
with open("output1.json", "r") as f:
    data = json.load(f)
    print(data)

# Example 2
with open("output2.json", "r") as f:
    print(json.load(f))

# Example 3
with open("output3.json", "r") as f:
    obj = json.load(f)
    print(obj["user"])

# Example 4
with open("output4.json", "r") as f:
    print(json.load(f)["status"])

# Example 5
with open("output5.json", "r") as f:
    print(json.load(f)["list"])


# =========================================================
# TOPIC 5: Working with structured JSON data (5 examples)
# =========================================================

# Example 1
data = {
    "students": [
        {"name": "Ali", "gpa": 3.4},
        {"name": "Dana", "gpa": 3.8}
    ]
}
print(data["students"][0]["name"])

# Example 2
json_str = json.dumps(data)
parsed = json.loads(json_str)
print(parsed["students"][1]["gpa"])

# Example 3
data["students"].append({"name": "Marat", "gpa": 3.9})
print(len(data["students"]))

# Example 4
for student in data["students"]:
    print(student["name"])

# Example 5
filtered = [s for s in data["students"] if s["gpa"] > 3.5]
print(filtered)