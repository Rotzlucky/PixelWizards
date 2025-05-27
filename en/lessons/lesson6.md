---
layout: lesson
title: "Quest 6: Magical Collections and Lists"
lang: en
permalink: /en/lessons/lesson6/
previous_lesson: /en/lessons/lesson5/
next_lesson: /en/lessons/lesson7/
order: 6
difficulty: 3
xp: 250
objectives:
  - Master the art of creating and managing magical lists
  - Learn to add, remove, and organize magical items
  - Understand list methods and magical operations
  - Build an inventory system for your magical adventures
challenges:
  - title: "Spell Inventory"
    description: "Create a list of spells and add functions to add new spells, remove learned spells, and display all spells."
    hint: "Use append() to add spells, remove() to delete them, and a for loop to display all spells."
  - title: "Magical Item Sorter"
    description: "Create a list of magical items with different values and sort them by price or alphabetically."
    hint: "Use the sort() method or sorted() function to organize your magical items."
  - title: "Party Manager"
    description: "Create a program that manages a party of adventurers, allowing you to add members, remove them, and check party size."
    hint: "Use a list to store party member names and len() to check the party size."
---

# Quest 6: Magical Collections and Lists

<i class="fas fa-list"></i> Welcome back, young wizard! Today you'll learn about one of the most useful magical containers in programming: **lists**. Think of lists as magical bags that can hold multiple items - spells, potions, magical creatures, or anything else you need for your adventures!

## What Are Magical Lists?

A list is like a magical scroll that can hold many items in a specific order. Unlike the simple containers (variables) you've used before, lists can store multiple values:

```python
# A simple variable holds one item
favorite_spell = "Fireball"

# A list holds many items
spell_collection = ["Fireball", "Heal", "Lightning Bolt", "Shield", "Teleport"]
```

## Creating Your First Magical List

Let's start by creating some magical collections:

```python
# Different ways to create lists
empty_bag = []  # An empty magical bag
potions = ["Health Potion", "Mana Potion", "Strength Potion"]
magical_numbers = [7, 13, 21, 42, 99]
mixed_collection = ["Dragon", 150, "Gold Coins", True, 3.14]

print("🧪 Potions:", potions)
print("🔢 Magical numbers:", magical_numbers)
print("📦 Mixed collection:", mixed_collection)
```

## Accessing Items in Your Magical Collection

Each item in a list has a magical address called an **index**. Python starts counting from 0 (like a true wizard's ancient numbering system):

```python
magical_creatures = ["Dragon", "Unicorn", "Phoenix", "Griffin", "Basilisk"]

# Accessing items by their magical index
print("🐉 First creature:", magical_creatures[0])    # Dragon
print("🦄 Second creature:", magical_creatures[1])   # Unicorn
print("🔥 Third creature:", magical_creatures[2])    # Phoenix

# Negative indices count from the end (very magical!)
print("🐍 Last creature:", magical_creatures[-1])   # Basilisk
print("🦅 Second to last:", magical_creatures[-2])  # Griffin
```

### Magical List Slicing

You can extract portions of your list using magical slicing:

```python
spell_book = ["Fireball", "Heal", "Lightning", "Shield", "Teleport", "Freeze", "Fly"]

# Get a slice of spells
basic_spells = spell_book[0:3]      # First 3 spells
advanced_spells = spell_book[4:]    # From index 4 to end
middle_spells = spell_book[2:5]     # From index 2 to 4

print("📚 Basic spells:", basic_spells)
print("🔮 Advanced spells:", advanced_spells)
print("⚡ Middle spells:", middle_spells)
```

## Adding Items to Your Collection

### The Append Spell (Adding to the End)

```python
inventory = ["Sword", "Shield"]
print("🎒 Starting inventory:", inventory)

# Add new items to the end
inventory.append("Health Potion")
inventory.append("Magic Ring")
print("🎒 After shopping:", inventory)
```

### The Insert Spell (Adding at Specific Position)

```python
party_members = ["Wizard", "Warrior", "Archer"]
print("👥 Original party:", party_members)

# Insert a healer at position 1
party_members.insert(1, "Healer")
print("👥 Party with healer:", party_members)
```

### The Extend Spell (Adding Multiple Items)

```python
basic_spells = ["Fireball", "Heal"]
new_spells = ["Lightning", "Shield", "Teleport"]

basic_spells.extend(new_spells)
print("📖 Complete spell book:", basic_spells)
```

## Removing Items from Your Collection

### The Remove Spell (Remove by Value)

```python
monster_list = ["Goblin", "Orc", "Dragon", "Troll", "Goblin"]
print("👹 Monsters before battle:", monster_list)

# Remove the first occurrence of "Goblin"
monster_list.remove("Goblin")
print("👹 After defeating a goblin:", monster_list)
```

### The Pop Spell (Remove by Position)

```python
treasure_chest = ["Gold", "Silver", "Ruby", "Diamond", "Emerald"]
print("💎 Treasure chest:", treasure_chest)

# Remove and get the last item
last_treasure = treasure_chest.pop()
print("💎 Took:", last_treasure)
print("💎 Remaining treasure:", treasure_chest)

# Remove and get item at specific position
second_treasure = treasure_chest.pop(1)
print("💎 Also took:", second_treasure)
print("💎 Final treasure:", treasure_chest)
```

## Magical List Operations

### Checking if Items Exist

```python
magical_library = ["Spell Book", "Potion Recipe", "Ancient Map", "Crystal Ball"]

# Check if an item exists
if "Crystal Ball" in magical_library:
    print("🔮 You have a Crystal Ball! You can see the future!")

if "Dragon Egg" not in magical_library:
    print("🥚 You need to find a Dragon Egg for your collection!")
```

### Counting and Measuring

```python
spell_components = ["Eye of Newt", "Wing of Bat", "Eye of Newt", "Dragon Scale"]

# Count how many items
total_components = len(spell_components)
print(f"🧪 Total components: {total_components}")

# Count specific items
newt_eyes = spell_components.count("Eye of Newt")
print(f"👁️ Eyes of Newt: {newt_eyes}")
```

## Organizing Your Magical Collections

### Sorting Spells

```python
messy_spells = ["Teleport", "Fireball", "Heal", "Lightning", "Shield"]
print("📚 Messy spell book:", messy_spells)

# Sort alphabetically (modifies the original list)
messy_spells.sort()
print("📚 Organized spell book:", messy_spells)

# Sort in reverse order
messy_spells.sort(reverse=True)
print("📚 Reverse alphabetical:", messy_spells)
```

### Sorting Numbers

```python
magical_levels = [15, 3, 42, 7, 23, 1, 99]
print("📊 Random levels:", magical_levels)

# Sort numbers
magical_levels.sort()
print("📊 Sorted levels:", magical_levels)

# Create a sorted copy (keeps original unchanged)
level_copy = sorted(magical_levels, reverse=True)
print("📊 Highest to lowest:", level_copy)
print("📊 Original still sorted:", magical_levels)
```

## Looping Through Magical Collections

### The For Loop with Lists

```python
magical_artifacts = ["Excalibur", "Holy Grail", "Elder Wand", "One Ring"]

print("🏛️ Examining magical artifacts:")
for artifact in magical_artifacts:
    print(f"✨ Found: {artifact}")

# With index numbers
print("\n📋 Catalog of artifacts:")
for index, artifact in enumerate(magical_artifacts):
    print(f"{index + 1}. {artifact}")
```

### Processing Each Item

```python
potion_prices = [25, 50, 75, 100, 150]
print("💰 Original prices:", potion_prices)

# Apply a discount to all potions
discounted_prices = []
for price in potion_prices:
    new_price = price * 0.8  # 20% discount
    discounted_prices.append(new_price)

print("💰 Discounted prices:", discounted_prices)
```

## Advanced List Magic

### List Comprehensions (Advanced Spell Crafting)

```python
# Create a list of squared magical numbers
magical_numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in magical_numbers]
print("🔢 Squared numbers:", squared_numbers)

# Filter spells by length
all_spells = ["Fire", "Heal", "Lightning Bolt", "Shield", "Teleportation"]
short_spells = [spell for spell in all_spells if len(spell) <= 5]
print("⚡ Short spells:", short_spells)
```

### Nested Lists (Lists within Lists)

```python
# A magical grid/map
magical_map = [
    ["🌲", "🌲", "🏰", "🌲"],
    ["🌲", "🗡️", "🌲", "🐉"],
    ["🌊", "🌊", "🌲", "🌲"],
    ["🏔️", "🏔️", "🏔️", "💎"]
]

print("🗺️ Magical Realm Map:")
for row in magical_map:
    print(" ".join(row))

# Access specific locations
castle_location = magical_map[0][2]
dragon_location = magical_map[1][3]
print(f"\n🏰 Castle found: {castle_location}")
print(f"🐉 Dragon found: {dragon_location}")
```

## Challenge: The Ultimate Magical Inventory System

Create a file called `magical_inventory.py` and build a complete inventory management system:

```python
class MagicalInventory:
    def __init__(self):
        self.items = []
        self.gold = 100
        
    def display_inventory(self):
        """Display all items in the inventory."""
        print("\n🎒 === MAGICAL INVENTORY ===")
        if not self.items:
            print("📦 Your inventory is empty!")
        else:
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item}")
        print(f"💰 Gold: {self.gold}")
        print("=" * 30)
    
    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)
        print(f"✅ Added {item} to your inventory!")
    
    def remove_item(self, item_name):
        """Remove an item from the inventory."""
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"❌ Removed {item_name} from your inventory!")
        else:
            print(f"⚠️ {item_name} not found in your inventory!")
    
    def use_item(self, item_name):
        """Use an item (removes it from inventory)."""
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"✨ You used {item_name}!")
            
            # Special effects for different items
            if "Health Potion" in item_name:
                print("💚 You feel refreshed and healed!")
            elif "Mana Potion" in item_name:
                print("💙 Your magical energy is restored!")
            elif "Strength Potion" in item_name:
                print("💪 You feel incredibly strong!")
        else:
            print(f"⚠️ You don't have {item_name}!")
    
    def sort_inventory(self):
        """Sort inventory alphabetically."""
        self.items.sort()
        print("📚 Inventory sorted alphabetically!")
    
    def count_item_type(self, item_type):
        """Count how many items contain a specific word."""
        count = sum(1 for item in self.items if item_type.lower() in item.lower())
        return count
    
    def find_items(self, search_term):
        """Find all items containing a search term."""
        found_items = [item for item in self.items if search_term.lower() in item.lower()]
        return found_items

def magical_shop(inventory):
    """A magical shop where you can buy items."""
    shop_items = {
        "Health Potion": 25,
        "Mana Potion": 30,
        "Strength Potion": 50,
        "Magic Sword": 200,
        "Shield of Protection": 150,
        "Scroll of Fireball": 75,
        "Healing Herb": 10,
        "Dragon Scale": 300
    }
    
    print("\n🏪 === MAGICAL SHOP ===")
    print("Welcome to Merlin's Magical Emporium!")
    print("Available items:")
    
    for item, price in shop_items.items():
        print(f"💰 {item}: {price} gold")
    
    while True:
        choice = input("\nWhat would you like to buy? (or 'exit' to leave): ")
        
        if choice.lower() == 'exit':
            break
        
        if choice in shop_items:
            price = shop_items[choice]
            if inventory.gold >= price:
                inventory.gold -= price
                inventory.add_item(choice)
                print(f"💰 Spent {price} gold. Remaining: {inventory.gold}")
            else:
                print(f"💸 Not enough gold! You need {price} but only have {inventory.gold}")
        else:
            print("❓ Item not available in the shop!")

def main():
    """Main game loop for the magical inventory system."""
    inventory = MagicalInventory()
    
    # Start with some basic items
    inventory.add_item("Wooden Staff")
    inventory.add_item("Health Potion")
    inventory.add_item("Spell Book")
    
    print("🧙‍♂️ Welcome to your Magical Adventure!")
    print("You start your journey with some basic equipment.")
    
    while True:
        print("\n🔮 What would you like to do?")
        print("1. View inventory")
        print("2. Add item")
        print("3. Remove item")
        print("4. Use item")
        print("5. Sort inventory")
        print("6. Search items")
        print("7. Visit shop")
        print("8. Item statistics")
        print("9. Exit adventure")
        
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == "1":
            inventory.display_inventory()
            
        elif choice == "2":
            item = input("Enter item name to add: ")
            inventory.add_item(item)
            
        elif choice == "3":
            item = input("Enter item name to remove: ")
            inventory.remove_item(item)
            
        elif choice == "4":
            item = input("Enter item name to use: ")
            inventory.use_item(item)
            
        elif choice == "5":
            inventory.sort_inventory()
            
        elif choice == "6":
            search = input("Search for items containing: ")
            found = inventory.find_items(search)
            if found:
                print(f"🔍 Found items: {found}")
            else:
                print("🔍 No items found!")
                
        elif choice == "7":
            magical_shop(inventory)
            
        elif choice == "8":
            potions = inventory.count_item_type("Potion")
            weapons = inventory.count_item_type("Sword")
            total_items = len(inventory.items)
            
            print(f"\n📊 Inventory Statistics:")
            print(f"🧪 Potions: {potions}")
            print(f"⚔️ Weapons: {weapons}")
            print(f"📦 Total items: {total_items}")
            
        elif choice == "9":
            print("✨ Thank you for playing!")
            print("🧙‍♂️ May your adventures be legendary!")
            break
            
        else:
            print("❓ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
```

## Working with Multiple Lists

Sometimes you need to work with several related lists:

```python
# Parallel lists (related data in separate lists)
hero_names = ["Aragorn", "Legolas", "Gimli", "Gandalf"]
hero_levels = [25, 22, 24, 50]
hero_classes = ["Ranger", "Archer", "Warrior", "Wizard"]

print("🏆 Hero Party Status:")
for i in range(len(hero_names)):
    name = hero_names[i]
    level = hero_levels[i]
    hero_class = hero_classes[i]
    print(f"⚔️ {name} - Level {level} {hero_class}")

# Using zip to combine lists
print("\n🏆 Using zip magic:")
for name, level, hero_class in zip(hero_names, hero_levels, hero_classes):
    print(f"⚔️ {name} - Level {level} {hero_class}")
```

## Quest Complete! 🎉

Congratulations, master of magical collections! You've learned to:

- ✅ Create and manage magical lists
- ✅ Add and remove items from your collections
- ✅ Access items by their magical indices
- ✅ Sort and organize your magical inventory
- ✅ Loop through collections efficiently
- ✅ Build complex inventory management systems

Lists are incredibly powerful tools that you'll use in almost every magical program you create. They're perfect for storing collections of spells, managing party members, tracking inventory, and organizing any kind of data in your adventures!

In your next quest, you'll learn about **dictionaries** - even more powerful magical containers that can store key-value pairs, like a magical address book for your spells and items!

### Practice Challenges

Try these additional challenges to master your list magic:

1. **Magical Recipe Book**: Create a program that stores recipes as lists of ingredients and allows you to search for recipes by ingredient.

2. **Adventure Party Optimizer**: Create a system that manages different types of heroes and suggests the best party composition for different quest types.

3. **Spell Combo Creator**: Build a program that takes a list of basic spells and creates all possible combinations for powerful combo spells.

Keep practicing with lists, and soon you'll be managing magical collections like a true wizard master! 🧙‍♂️📚✨ 