---
layout: lesson
title: "Quest 4: Magical Loops and Repetition"
lang: en
permalink: /en/lessons/lesson4/
previous_lesson: /en/lessons/lesson3/
next_lesson: /en/lessons/lesson5/
order: 4
difficulty: 3
xp: 200
objectives:
  - Master the art of for loops and while loops
  - Create mystical patterns using repetition
  - Build a magical number divination game
  - Understand when to use different types of loops
challenges:
  - title: "Magical Times Tables"
    description: "Create a program that displays the times table for any number the user chooses."
    hint: "Use a for loop with range() and multiply the loop variable by the chosen number."
  - title: "Password Protection Spell"
    description: "Create a program that keeps asking for a password until the correct one is entered (use 'wizard123')."
    hint: "Use a while loop that continues until the input matches the correct password."
  - title: "Number Wizard Challenge"
    description: "Ask for a number, show all even numbers from 1 to that number, and calculate their sum."
    hint: "Use a for loop with range() and check if each number is even using the modulus operator (%)."
---

# Quest 4: Magical Loops and Repetition

<i class="fas fa-repeat"></i> Welcome back, young wizard! In this quest, you'll learn one of the most powerful spells in programming: **repetition magic**. Just as a wizard might cast the same protection spell around their tower multiple times, programmers use loops to repeat actions efficiently.

## The Power of Repetition

Imagine if you had to write this code to count from 1 to 10:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
```

That's a lot of typing! And what if you wanted to count to 100? Or 1000? There has to be a better way... and there is! 🪄

## The For Loop Spell

The `for` loop is like a magical incantation that repeats a spell a specific number of times:

```python
# Count from 1 to 10 with magic!
for number in range(1, 11):
    print(number)
```

Let's break down this spell:
- `for` - starts the repetition magic
- `number` - a magical container that holds each value
- `range(1, 11)` - creates numbers from 1 to 10 (11 is not included)
- `:` - begins the spell block
- The indented line is what gets repeated

### Try It Yourself: Magical Counting

Create a new file called `magical_counting.py` and try these spells:

```python
# Spell 1: Count like a wizard
print("🧙‍♂️ Counting spell activated!")
for count in range(1, 6):
    print(f"Spell number {count} cast!")

# Spell 2: Magical multiplication table
print("\n🔢 The 5 times table appears:")
for number in range(1, 11):
    result = number * 5
    print(f"5 × {number} = {result}")

# Spell 3: Magical stars pattern
print("\n⭐ Creating a star constellation:")
for stars in range(1, 6):
    print("⭐" * stars)
```

## The While Loop Spell

The `while` loop is different - it repeats as long as a condition is true. It's like saying "keep casting this spell while the dragon is still awake":

```python
# A magical guessing game
import random

secret_number = random.randint(1, 10)
guess = 0

print("🔮 I'm thinking of a number between 1 and 10...")

while guess != secret_number:
    guess = int(input("What's your guess? "))
    
    if guess < secret_number:
        print("🔥 Too low! The magic grows stronger...")
    elif guess > secret_number:
        print("❄️ Too high! The magic grows weaker...")
    else:
        print("✨ Correct! You've mastered the divination spell!")
```

## Magical Patterns with Loops

Let's create some beautiful magical patterns:

```python
# Pattern 1: Magical pyramid
print("🏛️ Building a magical pyramid:")
for level in range(1, 6):
    spaces = " " * (5 - level)
    stars = "⭐" * level
    print(spaces + stars)

# Pattern 2: Magical diamond
print("\n💎 Conjuring a magical diamond:")
# Top half
for i in range(1, 5):
    spaces = " " * (4 - i)
    stars = "✨" * i
    print(spaces + stars)

# Bottom half
for i in range(3, 0, -1):
    spaces = " " * (4 - i)
    stars = "✨" * i
    print(spaces + stars)
```

## Challenge: The Magical Number Divination Game

Now let's combine everything to create an epic magical game! Create a file called `divination_game.py`:

```python
import random

print("🔮✨ Welcome to the Magical Number Divination Game! ✨🔮")
print("The crystal ball has chosen a number between 1 and 20...")
print("You have 6 attempts to divine the correct number!")

# The magical number
magic_number = random.randint(1, 20)
attempts = 0
max_attempts = 6
won = False

while attempts < max_attempts and not won:
    attempts += 1
    remaining = max_attempts - attempts + 1
    
    print(f"\n🌟 Attempt {attempts} of {max_attempts}")
    
    try:
        guess = int(input("Enter your divination: "))
        
        if guess == magic_number:
            print("🎉 INCREDIBLE! You've mastered the art of divination!")
            print(f"✨ The crystal ball reveals: {magic_number}")
            print(f"🏆 You succeeded in {attempts} attempts!")
            won = True
        elif guess < magic_number:
            print("🔥 The magical energy grows stronger... aim higher!")
            if remaining > 0:
                print(f"🔮 {remaining} attempts remaining")
        else:
            print("❄️ The magical energy grows weaker... aim lower!")
            if remaining > 0:
                print(f"🔮 {remaining} attempts remaining")
                
    except ValueError:
        print("⚠️ Please enter a valid number, young wizard!")
        attempts -= 1  # Don't count invalid input as an attempt

if not won:
    print(f"\n💀 The crystal ball's magic was too strong this time...")
    print(f"🔮 The secret number was: {magic_number}")
    print("🌟 Practice your divination skills and try again!")

print("\n✨ Thank you for playing the Magical Divination Game! ✨")
```

## Advanced Loop Magic

### Nested Loops (Loops within Loops)
```python
# Create a magical grid
print("🗺️ Magical realm map:")
for row in range(5):
    for col in range(5):
        if (row + col) % 2 == 0:
            print("🌟", end=" ")
        else:
            print("🌙", end=" ")
    print()  # New line after each row
```

### Loop Control Spells
```python
# break - escape the loop immediately
# continue - skip to the next iteration

print("🔍 Searching for magical artifacts:")
for chest in range(1, 11):
    if chest == 7:
        print(f"💎 Found the legendary gem in chest {chest}!")
        break  # Stop searching
    print(f"📦 Chest {chest}: Empty")

print("\n🏃‍♂️ Avoiding cursed numbers:")
for number in range(1, 11):
    if number == 4 or number == 7:
        print(f"⚠️ Skipping cursed number {number}")
        continue  # Skip this iteration
    print(f"✅ Safe number: {number}")
```

## Practice Challenges

Try these magical challenges to strengthen your loop spells:

### Challenge 1: Magical Times Tables
Create a program that displays the times table for any number the user chooses.

### Challenge 2: Password Protection Spell
Create a program that keeps asking for a password until the correct one is entered (use "wizard123").

### Challenge 3: Magical ASCII Art
Use loops to create a larger magical pattern or picture.

### Challenge 4: Number Wizard
Create a program that:
1. Asks the user for a number
2. Shows all even numbers from 1 to that number
3. Calculates the sum of all those even numbers

## What's Next?

In our next quest, we'll learn about **Inventory Scrolls and Collections** (lists) - magical containers that can hold multiple items at once! This will be crucial for managing player inventories, enemy lists, and game items in our future RPG.

**Keep practicing your loop magic, young wizard!** 🔄✨ 