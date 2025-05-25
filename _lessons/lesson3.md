---
layout: lesson
title: "Quest 3: Forking Paths with If Enchantments"
lang: en
previous_lesson: lessons/lesson2/
next_lesson: lessons/lesson4/
order: 3
objectives:
  - Master the mystical art of truth magic (Boolean values - True/False)
  - Learn to use comparison runes to evaluate magical conditions
  - Cast if, else, and elif enchantments to create decision-making spells
  - Create a simple text-based magical adventure with branching paths
---

# Forking Paths with If Enchantments

<i class="fas fa-road-fork"></i> Greetings, advancing apprentice! In your previous quests, you've learned to store magical essences and perform arithmancy. Now we shall delve into one of the most powerful forms of wizardry: the art of making decisions in your spells! With if enchantments, your magic will be able to choose different paths based on mystical conditions.

## Truth Magic: The Essence of Boolean Values

Before we can craft decision-making spells, we must understand the fundamental essence of truth magic - Boolean values. In the realm of Python wizardry, there are only two states of truth:

```python
magical_truth = True
magical_falsehood = False
```

These mystical essences are the foundation of all decision-making magic!

### Examples of Truth Magic in Action

```python
has_magic_wand = True
dragon_is_sleeping = False
quest_completed = True
potion_is_ready = False

print("Do I have a magic wand?", has_magic_wand)
print("Is the dragon sleeping?", dragon_is_sleeping)
```

## Comparison Runes: Evaluating Magical Conditions

Comparison runes allow us to compare magical essences and determine truth values. These ancient symbols hold great power:

### The Sacred Comparison Runes

```python
wizard_level = 15
required_level = 10
magic_power = 85
enemy_strength = 90

# Equality Rune (==) - Are two essences exactly the same?
is_exact_level = wizard_level == 15
print("Wizard is exactly level 15:", is_exact_level)  # True

# Inequality Rune (!=) - Are two essences different?
different_strengths = magic_power != enemy_strength
print("Magic power differs from enemy strength:", different_strengths)  # True

# Greater Than Rune (>) - Is the first essence larger?
can_attempt_quest = wizard_level > required_level
print("Can attempt this quest:", can_attempt_quest)  # True

# Less Than Rune (<) - Is the first essence smaller?
is_weaker = magic_power < enemy_strength
print("Wizard is weaker than enemy:", is_weaker)  # True

# Greater Than or Equal Rune (>=)
meets_requirement = wizard_level >= required_level
print("Meets level requirement:", meets_requirement)  # True

# Less Than or Equal Rune (<=)
within_safe_limit = magic_power <= 100
print("Magic power within safe limits:", within_safe_limit)  # True
```

### Advanced Truth Magic with Logical Operators

Combine multiple truth conditions using mystical logical operators:

```python
wizard_health = 80
has_healing_potion = True
enemy_nearby = False

# AND operator - Both conditions must be true
can_explore_safely = wizard_health > 50 and not enemy_nearby
print("Can explore safely:", can_explore_safely)  # True

# OR operator - At least one condition must be true
can_survive_battle = wizard_health > 75 or has_healing_potion
print("Can survive battle:", can_survive_battle)  # True

# NOT operator - Reverses the truth value
safe_to_rest = not enemy_nearby
print("Safe to rest:", safe_to_rest)  # True
```

## If Enchantments: Your First Decision-Making Spells

The `if` enchantment is the foundation of all decision-making magic. It allows your spells to execute different code based on whether a condition is true or false.

### Basic If Enchantment Structure

```python
wizard_mana = 30

if wizard_mana >= 25:
    print("✨ You have enough mana to cast a powerful spell!")
    print("🔥 Casting Fireball!")
```

### If-Else Enchantments: Two Paths of Magic

```python
dragon_health = 20

if dragon_health <= 0:
    print("🎉 Victory! The dragon has been defeated!")
    print("💰 You found 100 gold coins!")
else:
    print("⚔️ The dragon still fights!")
    print(f"🐉 Dragon health remaining: {dragon_health}")
```

### If-Elif-Else Enchantments: Multiple Magical Paths

```python
wizard_experience = 750

if wizard_experience >= 1000:
    wizard_rank = "Archmage"
    special_power = "Reality Manipulation"
elif wizard_experience >= 500:
    wizard_rank = "Master Wizard"
    special_power = "Elemental Control"
elif wizard_experience >= 200:
    wizard_rank = "Skilled Wizard"
    special_power = "Enhanced Spells"
else:
    wizard_rank = "Apprentice"
    special_power = "Basic Magic"

print(f"🧙‍♂️ Rank: {wizard_rank}")
print(f"✨ Special Power: {special_power}")
```

## Practical Spell Examples

Let's put our knowledge into practice with some real magical scenarios:

### Example 1: Magical Item Shop

```python
# Magical Item Shop
print("🏪 Welcome to Merlin's Magical Emporium!")
wizard_gold = int(input("How much gold do you have? "))

print("\n📜 Available Items:")
print("1. Health Potion - 25 gold")
print("2. Magic Scroll - 50 gold") 
print("3. Enchanted Sword - 100 gold")

item_choice = input("\nWhat would you like to buy? (1/2/3): ")

if item_choice == "1":
    item_name = "Health Potion"
    item_cost = 25
elif item_choice == "2":
    item_name = "Magic Scroll"
    item_cost = 50
elif item_choice == "3":
    item_name = "Enchanted Sword"
    item_cost = 100
else:
    print("❌ That item doesn't exist in our magical inventory!")
    item_cost = 0
    item_name = None

if item_name and wizard_gold >= item_cost:
    remaining_gold = wizard_gold - item_cost
    print(f"✅ Purchase successful! You bought: {item_name}")
    print(f"💰 Remaining gold: {remaining_gold}")
elif item_name and wizard_gold < item_cost:
    needed_gold = item_cost - wizard_gold
    print(f"❌ Insufficient gold! You need {needed_gold} more gold for {item_name}")
```

### Example 2: Magical Combat System

```python
# Simple Magical Combat
import random

wizard_health = 100
dragon_health = 80

print("🐉 A wild dragon appears!")
print(f"🧙‍♂️ Your health: {wizard_health}")
print(f"🐉 Dragon health: {dragon_health}")

while wizard_health > 0 and dragon_health > 0:
    print("\n⚔️ Choose your action:")
    print("1. Cast Fireball (high damage, high mana cost)")
    print("2. Cast Ice Shard (medium damage, medium mana cost)")  
    print("3. Use Healing Potion (restore health)")
    
    action = input("Enter your choice (1/2/3): ")
    
    if action == "1":
        damage = random.randint(20, 30)
        dragon_health -= damage
        print(f"🔥 Fireball hits for {damage} damage!")
    elif action == "2":
        damage = random.randint(15, 25)
        dragon_health -= damage
        print(f"❄️ Ice Shard hits for {damage} damage!")
    elif action == "3":
        healing = random.randint(15, 25)
        wizard_health += healing
        if wizard_health > 100:
            wizard_health = 100
        print(f"💚 You heal for {healing} health!")
    else:
        print("❌ Invalid action! You lose your turn!")
    
    # Dragon's turn
    if dragon_health > 0:
        dragon_damage = random.randint(10, 20)
        wizard_health -= dragon_damage
        print(f"🐉 Dragon attacks for {dragon_damage} damage!")
    
    print(f"🧙‍♂️ Your health: {wizard_health}")
    print(f"🐉 Dragon health: {dragon_health}")

# Determine the winner
if wizard_health <= 0:
    print("\n💀 You have been defeated! The dragon wins!")
    print("🔄 Return to the academy to train more!")
else:
    print("\n🎉 Victory! You have defeated the dragon!")
    print("💰 You earned 150 gold and 200 experience points!")
```

## Let's Create a Magical Adventure Game

Now let's combine all our knowledge to create an interactive text-based adventure:

```python
# The Enchanted Forest Adventure
print("🌲 Welcome to the Enchanted Forest Adventure! 🌲")
print("=" * 50)

# Character creation
wizard_name = input("What is your wizard's name? ")
print(f"\nWelcome, {wizard_name}! Your magical journey begins...")

# Starting stats
health = 100
mana = 50
gold = 20
has_key = False

print(f"\n📊 Starting Stats:")
print(f"❤️ Health: {health}")
print(f"💙 Mana: {mana}")
print(f"💰 Gold: {gold}")

# The adventure begins
print(f"\n🌟 {wizard_name}, you find yourself at the edge of an enchanted forest.")
print("Three mystical paths stretch before you, each leading to different adventures.")

while True:
    print("\n🛤️ Choose your path:")
    print("1. 🏰 The Ancient Tower (requires magical key)")
    print("2. 🕳️ The Mysterious Cave")
    print("3. 🌸 The Fairy Glade")
    print("4. 🏪 Visit the Forest Merchant")
    print("5. 🚪 Exit the forest")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
        if has_key:
            print("🗝️ You use your magical key to unlock the tower!")
            print("✨ Inside, you discover an ancient spellbook!")
            print("📚 Your magical knowledge increases greatly!")
            mana += 30
            print(f"💙 Mana increased to: {mana}")
            print("🎉 Congratulations! You've completed the greatest challenge!")
            break
        else:
            print("🔒 The tower door is locked with powerful magic.")
            print("🗝️ You need a magical key to enter.")
    
    elif choice == "2":
        print("🕳️ You enter the dark, mysterious cave...")
        print("👹 A goblin jumps out and challenges you to combat!")
        
        if mana >= 20:
            print("⚡ You cast Lightning Bolt!")
            mana -= 20
            gold += 15
            print("🎉 Victory! The goblin drops 15 gold coins!")
            print(f"💰 Gold: {gold}, 💙 Mana: {mana}")
        else:
            print("💔 You don't have enough mana to fight!")
            health -= 15
            print(f"💔 You lose 15 health. Health: {health}")
            
            if health <= 0:
                print("💀 Your adventure ends here. Train more before returning!")
                break
    
    elif choice == "3":
        print("🌸 You enter a beautiful glade filled with friendly fairies.")
        print("🧚‍♀️ The fairies offer to help you!")
        
        fairy_choice = input("Accept their help? (yes/no): ").lower()
        
        if fairy_choice == "yes":
            print("✨ The fairies cast a healing spell on you!")
            health += 25
            if health > 100:
                health = 100
            print("🗝️ They also give you a magical key!")
            has_key = True
            print(f"❤️ Health restored to: {health}")
        else:
            print("🧚‍♀️ The fairies respect your choice and wave goodbye.")
    
    elif choice == "4":
        print("🏪 You meet a friendly forest merchant.")
        print("🧙‍♂️ 'Welcome, young wizard! I have magical wares!'")
        print("💊 Health Potion - 15 gold (restores 30 health)")
        print("🔮 Mana Crystal - 20 gold (restores 25 mana)")
        
        if gold >= 15:
            buy_choice = input("What would you like to buy? (health/mana/nothing): ").lower()
            
            if buy_choice == "health" and gold >= 15:
                gold -= 15
                health += 30
                if health > 100:
                    health = 100
                print(f"💊 Health potion consumed! Health: {health}, Gold: {gold}")
            elif buy_choice == "mana" and gold >= 20:
                gold -= 20
                mana += 25
                print(f"🔮 Mana crystal used! Mana: {mana}, Gold: {gold}")
            elif buy_choice == "mana" and gold < 20:
                print("💰 You don't have enough gold for a mana crystal!")
            else:
                print("🤝 Thank you for visiting!")
        else:
            print("💰 You don't have enough gold to buy anything.")
    
    elif choice == "5":
        print(f"🚪 {wizard_name} exits the enchanted forest.")
        print("🌟 Thank you for playing the Enchanted Forest Adventure!")
        break
    
    else:
        print("❌ Invalid choice! Please choose 1-5.")

print("\n📊 Final Stats:")
print(f"❤️ Health: {health}")
print(f"💙 Mana: {mana}")
print(f"💰 Gold: {gold}")
print(f"🗝️ Has Key: {has_key}")
```

## Try It Yourself: Magical Challenges

Before we conclude this quest, here are some enchanting challenges to master your new if enchantment skills:

### Challenge 1: Magical Weather System
Create a spell that:
1. Asks for the current weather (sunny/rainy/stormy)
2. Recommends appropriate magical gear based on weather
3. Calculates spell effectiveness based on conditions
4. Suggests different magical activities for each weather type

### Challenge 2: Wizard Academy Gradebook
Create a spell that:
1. Asks for three magical subject scores (0-100)
2. Calculates the average magical aptitude
3. Assigns a magical grade (A, B, C, D, F)
4. Provides appropriate encouragement or improvement suggestions
5. Determines if the wizard advances to the next level

### Challenge 3: Magical Creature Encounter
Create a spell that:
1. Randomly encounters different magical creatures
2. Offers different interaction choices for each creature
3. Uses if statements to determine outcomes
4. Tracks reputation with different magical beings
5. Unlocks special encounters based on reputation levels

## What Awaits in Your Next Quest?

In Quest 4, we'll master the mystical art of magical loops and repetition! You'll learn how to create cyclical spells using for loops and while loops, allowing your magic to repeat actions and create powerful patterns. This knowledge will be essential for creating dynamic magical experiences and automated spell casting!

Remember, the power of decision-making through if enchantments is one of the most fundamental skills in all of wizardry. Practice creating spells with multiple branching paths, experiment with complex logical conditions, and don't be afraid to nest if statements within other if statements for truly sophisticated magical decision-making!

**Your magical prowess grows stronger with each enchantment you master, noble wizard!** 🧙‍♂️✨🎮 