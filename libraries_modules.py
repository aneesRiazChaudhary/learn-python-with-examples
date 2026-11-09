# libraries_modules.py
# random library

"""
Topic: Libraries and Modules

Concepts Covered:

1. Importing Modules
   - Use import to access pre-built Python functionality.
   - Extend Python's capabilities without writing everything from scratch.

2. The random Module
   - A built-in Python module for generating random values.
   - Commonly used in games, simulations, testing, and probability.

3. Random Selection
   - Use random.choice() to select a random item from a sequence.
   - Example: coin toss simulation.

4. Probability Simulations
   - Model real-world random events.
   - Example: heads or tails outcomes.

5. Random Integers
   - Use random.randint(a, b).
   - Generate random numbers within a specified range.
   - Both boundary values are included.

6. Randomising Sequences
   - Use random.shuffle().
   - Rearrange items into a random order.

7. Working With Lists
   - Store multiple values in lists.
   - Apply random operations to list elements.

8. Iterating Through Shuffled Data
   - Use loops to process reordered items.
   - Display values one item at a time.

9. Simulating Card Decks
   - Randomly reorder cards or sequences.
   - Demonstrates practical applications of randomisation.

Key Takeaways:

- Modules provide reusable functionality.
- The random module helps generate unpredictable results.
- random.choice() selects one item from a collection.
- random.randint() generates random numbers.
- random.shuffle() reorders items in place.
- Randomisation is commonly used in games, simulations, testing, and data processing.
"""

import random

print("#" * 20, "new section" , "coin probabilty")
# we will use a 50 by 50 probabilty to find the head or tail through this random library 

coin = random.choice(["ups", "downs"])
print(coin)


print("#" * 20, "new section" , "this will print random number between a and b incluing and b")

dice = random.randint(1,6)
print(dice)



print("#" * 20, "new section" , "shufle a deck of cards")

#  shufle function does not return a value it just reorder items

cards = ["King", "Jack", "Queen"]
random.shuffle(cards)
# this will print a list of reorederd items such as ["Queen", "king", "Jack"]
print(cards)

# to print these shufled cards row by row we will use for loop
print("#" * 20, "new section" , "shufle a deck of cards print card by card")

seq = ["Diamond", "Heart", "Spade", "Club"]
random.shuffle(seq)
for i in seq:
    print(f"reorederd {i}")





