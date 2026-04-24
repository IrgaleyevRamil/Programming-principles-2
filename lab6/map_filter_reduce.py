"""
Practice - Map, Filter, Reduce

Topics:
1) map()
2) filter()
3) reduce()
4) lambda with map/filter
5) combined usage
"""

from functools import reduce


# =========================================================
# TOPIC 1: map() (5 examples)
# =========================================================

# Example 1
nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))

# Example 2
print(list(map(lambda x: x + 1, nums)))

# Example 3
print(list(map(lambda x: x ** 2, nums)))

# Example 4
print(list(map(str, nums)))

# Example 5
print(list(map(lambda x: x - 1, nums)))


# =========================================================
# TOPIC 2: filter() (5 examples)
# =========================================================

# Example 1
nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))

# Example 2
print(list(filter(lambda x: x > 2, nums)))

# Example 3
print(list(filter(lambda x: x < 4, nums)))

# Example 4
print(list(filter(lambda x: x != 3, nums)))

# Example 5
print(list(filter(lambda x: x >= 2, nums)))


# =========================================================
# TOPIC 3: reduce() (5 examples)
# =========================================================

# Example 1
nums = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, nums))

# Example 2
print(reduce(lambda x, y: x * y, nums))

# Example 3
print(reduce(lambda x, y: x if x > y else y, nums))

# Example 4
print(reduce(lambda x, y: x - y, nums))

# Example 5
print(reduce(lambda x, y: x + y * 2, nums))


# =========================================================
# TOPIC 4: lambda with map/filter (5 examples)
# =========================================================

# Example 1
nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 3, nums)))

# Example 2
print(list(filter(lambda x: x % 2 != 0, nums)))

# Example 3
print(list(map(lambda x: x + 5, nums)))

# Example 4
print(list(filter(lambda x: x > 1, nums)))

# Example 5
print(list(map(lambda x: x // 2, nums)))


# =========================================================
# TOPIC 5: combined usage (5 examples)
# =========================================================

# Example 1
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))
print(result)

# Example 2
result = list(map(lambda x: x + 1, filter(lambda x: x > 2, nums)))
print(result)

# Example 3
result = reduce(lambda x, y: x + y, map(lambda x: x * 2, nums))
print(result)

# Example 4
result = list(filter(lambda x: x > 5, map(lambda x: x * 3, nums)))
print(result)

# Example 5
result = reduce(lambda x, y: x * y, filter(lambda x: x > 1, nums))
print(result)