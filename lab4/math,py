"""
Practice - Math and Random

Topics:
1) Built-in numeric functions
2) math module basics
3) Rounding and precision
4) random basics
5) random with lists + simple simulations
"""

import math
import random


# =========================================================
# TOPIC 1: Built-in numeric functions (5 examples)
# =========================================================

# Example 1
print("abs:", abs(-15))

# Example 2
print("pow:", pow(2, 5))

# Example 3
print("min:", min(5, 2, 9, 1))

# Example 4
print("max:", max(5, 2, 9, 1))

# Example 5
print("sum:", sum([1, 2, 3, 4, 5]))


# =========================================================
# TOPIC 2: math module basics (5 examples)
# =========================================================

# Example 1
print("sqrt:", math.sqrt(49))

# Example 2
print("pi:", math.pi)

# Example 3
print("factorial:", math.factorial(5))

# Example 4
print("gcd:", math.gcd(18, 24))

# Example 5
print("log10:", math.log10(1000))


# =========================================================
# TOPIC 3: Rounding and precision (5 examples)
# =========================================================

# Example 1
print("round:", round(3.14159, 2))

# Example 2
print("ceil:", math.ceil(4.1))

# Example 3
print("floor:", math.floor(4.9))

# Example 4
print("trunc:", math.trunc(-3.7))

# Example 5
x = 0.1 + 0.2
print("0.1 + 0.2 =", x, "| rounded:", round(x, 2))


# =========================================================
# TOPIC 4: random basics (5 examples)
# =========================================================

# Example 1
print("randint 1..10:", random.randint(1, 10))

# Example 2
print("random 0..1:", random.random())

# Example 3
print("uniform 5..10:", random.uniform(5, 10))

# Example 4
print("randrange step:", random.randrange(0, 20, 4))

# Example 5
random.seed(42)
print("seeded randint:", random.randint(1, 10))


# =========================================================
# TOPIC 5: random with lists + simple simulations (5 examples)
# =========================================================

# Example 1
items = ["rock", "paper", "scissors"]
print("choice:", random.choice(items))

# Example 2
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("shuffled:", nums)

# Example 3
cards = ["A", "K", "Q", "J", "10"]
picked = random.sample(cards, 3)
print("sample 3 cards:", picked)

# Example 4
dice = [random.randint(1, 6) for _ in range(5)]
print("5 dice:", dice)

# Example 5
heads = 0
for _ in range(100):
    if random.choice(["H", "T"]) == "H":
        heads += 1
print("Heads in 100 flips:", heads)