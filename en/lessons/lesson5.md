---
layout: lesson
title: "Quest 5: Crafting Your Own Spells (Functions)"
lang: en
permalink: /en/lessons/lesson5/
previous_lesson: /en/lessons/lesson4/
next_lesson: /en/lessons/lesson6/
order: 5
difficulty: 3
xp: 225
objectives:
  - Learn to create your own magical functions (spells)
  - Understand parameters and return values
  - Build a collection of reusable spell components
  - Create a magical spell library for your adventures
challenges:
  - title: "Greeting Spell"
    description: "Create a function that takes a name and returns a personalized magical greeting."
    hint: "Use def to create the function and return a string with the person's name."
  - title: "Magical Calculator"
    description: "Create functions for basic math operations (add, subtract, multiply, divide) that work with magical numbers."
    hint: "Each function should take two parameters and return the result of the operation."
  - title: "Spell Power Analyzer"
    description: "Create a function that takes a spell name and power level, then returns whether it's a beginner, intermediate, or advanced spell."
    hint: "Use if/elif/else statements inside your function to categorize based on power level."
---

# Quest 5: Crafting Your Own Spells (Functions)

<i class="fas fa-magic"></i> Greetings, aspiring spell-crafter! Today you'll learn one of the most important skills in the magical arts: **creating your own spells**. In programming, we call these custom spells **functions**.

## Why Create Your Own Spells?

Imagine you're a wizard who needs to cast the same protection spell multiple times. Instead of reciting the entire incantation each time, wouldn't it be easier to just say "Protection!" and have the spell activate? That's exactly what functions do!

```python
# Without functions (repetitive magic)
print("🛡️ Casting protection spell...")
print("✨ Magical barriers rising...")
print("🌟 You are now protected!")

print("🛡️ Casting protection spell...")
print("✨ Magical barriers rising...")
print("🌟 You are now protected!")

# With functions (efficient magic!)
def cast_protection():
    print("🛡️ Casting protection spell...")
    print("✨ Magical barriers rising...")
    print("🌟 You are now protected!")

# Now we can cast it easily
cast_protection()
cast_protection()
```

## Creating Your First Spell (Function)

Let's start with a simple greeting spell:

```python
def magical_greeting():
    print("🧙‍♂️ Greetings, fellow wizard!")
    print("✨ May your code be bug-free and your spells powerful!")

# To cast (call) your spell:
magical_greeting()
```

### The Anatomy of a Spell

```python
def spell_name():
    # Your magical code here
    pass
```

- `def` - tells Python you're creating a new spell
- `spell_name()` - the name of your spell (with parentheses)
- `:` - starts the spell definition
- Indented code - what happens when the spell is cast

## Spells with Ingredients (Parameters)

Most powerful spells need ingredients! In programming, we call these **parameters**:

```python
def personalized_greeting(wizard_name):
    print(f"🧙‍♂️ Greetings, {wizard_name}!")
    print(f"✨ Welcome to the magical realm!")

# Cast the spell with different names
personalized_greeting("Merlin")
personalized_greeting("Gandalf")
personalized_greeting("Hermione")
```

### Multiple Ingredients

```python
def create_potion(ingredient1, ingredient2, magic_level):
    print(f"🧪 Brewing potion with {ingredient1} and {ingredient2}")
    print(f"⚡ Magic level: {magic_level}")
    
    if magic_level > 5:
        print("💥 POWERFUL potion created!")
    else:
        print("✨ Basic potion created!")

# Try different combinations
create_potion("dragon scale", "unicorn hair", 8)
create_potion("mushroom", "water", 3)
```

## Spells That Give You Something Back (Return Values)

Some spells don't just do something - they give you something back! Like a spell that calculates magical power:

```python
def calculate_spell_power(base_power, wizard_level):
    total_power = base_power * wizard_level
    return total_power

# Use the spell's result
my_power = calculate_spell_power(10, 5)
print(f"🔥 Your spell power is: {my_power}")

# Or use it directly
if calculate_spell_power(15, 3) > 40:
    print("💪 You're ready for advanced magic!")
```

### A Magical Calculator

```python
def magical_add(num1, num2):
    result = num1 + num2
    print(f"✨ {num1} + {num2} = {result}")
    return result

def magical_multiply(num1, num2):
    result = num1 * num2
    print(f"🌟 {num1} × {num2} = {result}")
    return result

# Test your magical calculator
sum_result = magical_add(25, 17)
product_result = magical_multiply(6, 7)
```

## Building Your Spell Library

Let's create a collection of useful spells:

```python
# Spell Library: magical_spells.py

def cast_fireball(damage):
    """A spell that creates a fireball with specified damage."""
    print(f"🔥 FIREBALL! Dealing {damage} damage!")
    return damage

def heal_wizard(current_health, healing_power):
    """A spell that heals a wizard."""
    new_health = current_health + healing_power
    print(f"💚 Healing magic flows through you!")
    print(f"❤️ Health: {current_health} → {new_health}")
    return new_health

def check_spell_success(skill_level, spell_difficulty):
    """Determines if a spell casting is successful."""
    success_chance = skill_level - spell_difficulty
    
    if success_chance >= 3:
        print("✨ PERFECT CAST! Spell succeeds magnificently!")
        return "perfect"
    elif success_chance >= 0:
        print("👍 Good cast! Spell succeeds!")
        return "success"
    else:
        print("💥 Spell fizzles... Try again!")
        return "failure"

def generate_wizard_name(first_name):
    """Creates a magical wizard name."""
    magical_titles = ["the Wise", "the Brave", "the Mystical", "the Powerful"]
    import random
    title = random.choice(magical_titles)
    wizard_name = f"{first_name} {title}"
    print(f"🎭 Your wizard name is: {wizard_name}")
    return wizard_name

# Test your spell library
print("🧙‍♂️ Testing the Spell Library!")
print("=" * 40)

# Test combat spells
damage_dealt = cast_fireball(25)

# Test healing
new_hp = heal_wizard(50, 30)

# Test spell success
result = check_spell_success(7, 4)

# Generate a wizard name
my_wizard_name = generate_wizard_name("Alex")
```

## Advanced Spell Crafting

### Default Ingredients (Default Parameters)

```python
def create_magical_shield(strength=5, duration=10):
    print(f"🛡️ Creating magical shield...")
    print(f"💪 Strength: {strength}")
    print(f"⏰ Duration: {duration} seconds")

# These all work!
create_magical_shield()                    # Uses defaults
create_magical_shield(8)                   # Custom strength
create_magical_shield(strength=12)         # Named parameter
create_magical_shield(7, 15)              # Both custom
```

### Spells with Multiple Return Values

```python
def analyze_magical_creature(creature_name, level):
    """Analyzes a magical creature and returns multiple stats."""
    health = level * 20
    magic_power = level * 15
    danger_level = "Low" if level < 5 else "High" if level > 8 else "Medium"
    
    return health, magic_power, danger_level

# Unpack the results
hp, mp, danger = analyze_magical_creature("Dragon", 10)
print(f"🐉 Dragon Analysis:")
print(f"❤️ Health: {hp}")
print(f"⚡ Magic Power: {mp}")
print(f"⚠️ Danger Level: {danger}")
```

## Challenge: The Ultimate Spell Crafting Workshop

Create a file called `spell_workshop.py` and build your own magical spell collection:

```python
import random

def welcome_message():
    """Displays a welcome message for the spell workshop."""
    print("🏰 Welcome to the Spell Crafting Workshop! 🏰")
    print("✨ Here you can create and test magical spells!")
    print("=" * 50)

def roll_magical_dice(sides=6):
    """Rolls a magical dice with specified number of sides."""
    result = random.randint(1, sides)
    print(f"🎲 Rolling magical {sides}-sided dice... Result: {result}")
    return result

def brew_random_potion():
    """Brews a random magical potion."""
    ingredients = ["dragon scale", "unicorn hair", "phoenix feather", 
                  "moonstone dust", "troll tears", "fairy wings"]
    colors = ["red", "blue", "green", "purple", "golden", "silver"]
    
    ingredient = random.choice(ingredients)
    color = random.choice(colors)
    potency = random.randint(1, 10)
    
    print(f"🧪 Brewing potion with {ingredient}...")
    print(f"✨ The potion glows {color}!")
    print(f"💪 Potency level: {potency}/10")
    
    return {"ingredient": ingredient, "color": color, "potency": potency}

def calculate_adventure_success(party_size, average_level, quest_difficulty):
    """Calculates the success chance of a magical adventure."""
    base_chance = (party_size * 10) + (average_level * 5)
    difficulty_penalty = quest_difficulty * 15
    success_chance = max(0, min(100, base_chance - difficulty_penalty))
    
    print(f"🗺️ Adventure Analysis:")
    print(f"👥 Party size: {party_size}")
    print(f"📊 Average level: {average_level}")
    print(f"⚔️ Quest difficulty: {quest_difficulty}")
    print(f"🎯 Success chance: {success_chance}%")
    
    if success_chance >= 80:
        print("🏆 Excellent! This quest should be easy!")
    elif success_chance >= 60:
        print("👍 Good chance of success!")
    elif success_chance >= 40:
        print("⚠️ Risky, but possible!")
    else:
        print("💀 Very dangerous! Consider more preparation!")
    
    return success_chance

def magical_number_generator(min_val=1, max_val=100, count=1):
    """Generates magical numbers for spells and potions."""
    numbers = []
    for i in range(count):
        number = random.randint(min_val, max_val)
        numbers.append(number)
    
    print(f"🔢 Generated {count} magical number(s): {numbers}")
    return numbers if count > 1 else numbers[0]

# Main spell workshop program
def run_spell_workshop():
    welcome_message()
    
    while True:
        print("\n🔮 Choose your magical action:")
        print("1. Roll magical dice")
        print("2. Brew random potion")
        print("3. Calculate adventure success")
        print("4. Generate magical numbers")
        print("5. Exit workshop")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            sides = int(input("How many sides on your magical dice? "))
            roll_magical_dice(sides)
            
        elif choice == "2":
            potion = brew_random_potion()
            
        elif choice == "3":
            party = int(input("Party size: "))
            level = int(input("Average party level: "))
            difficulty = int(input("Quest difficulty (1-10): "))
            calculate_adventure_success(party, level, difficulty)
            
        elif choice == "4":
            count = int(input("How many numbers to generate? "))
            magical_number_generator(count=count)
            
        elif choice == "5":
            print("✨ Thank you for visiting the Spell Workshop!")
            print("🧙‍♂️ May your functions be bug-free and your magic strong!")
            break
            
        else:
            print("⚠️ Invalid choice! Please try again.")

# Run the workshop
if __name__ == "__main__":
    run_spell_workshop()
```

## Spell Documentation (Docstrings)

Good wizards document their spells! Use docstrings to explain what your functions do:

```python
def cast_lightning_bolt(target, power_level):
    """
    Casts a lightning bolt at the specified target.
    
    Parameters:
    target (str): The name of the target
    power_level (int): The power of the lightning (1-10)
    
    Returns:
    int: The damage dealt
    """
    damage = power_level * 15
    print(f"⚡ Lightning strikes {target} for {damage} damage!")
    return damage
```

## Quest Complete! 🎉

Congratulations, spell-crafter! You've learned to:

- ✅ Create your own functions (spells)
- ✅ Use parameters to make flexible spells
- ✅ Return values from your functions
- ✅ Build a library of reusable magical components
- ✅ Document your spells properly

Functions are one of the most powerful tools in programming. They help you organize your code, avoid repetition, and create reusable magical components that you can use in all your future adventures!

In your next quest, you'll learn about **lists and magical collections** - perfect for storing your growing collection of spells and magical items!

### Practice Challenges

Try these additional challenges to master your spell-crafting skills:

1. **Weather Spell**: Create a function that takes a temperature and returns whether you need a warming spell, cooling spell, or no spell at all.

2. **Magical Item Shop**: Create functions to calculate prices, apply discounts, and determine if a customer can afford magical items.

3. **Spell Combination**: Create a function that takes two spell names and combines them into a new, more powerful spell name.

Keep practicing, and soon you'll be crafting spells like a true wizard master! 🧙‍♂️✨ 