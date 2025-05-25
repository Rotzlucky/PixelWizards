---
layout: lesson
title: "Quest 1: Casting Your First Python Spell "
lang: en
next_lesson: lessons/lesson2/
order: 1
objectives:
  - Understand what Python is and why it's great for making games
  - Write your very first Python program
  - Learn about print statements, comments, and variables
  - Create an interactive greeting program
---

# Your First Python Program

Hello, future game developer! Are you ready to start your coding adventure? In this first lesson, we're going to learn what Python is and write our very first program! 

*Note: Make sure you've completed the [Preparation lesson]({{ 'lessons/preparation/' | relative_url }}) before starting this quest. You'll need Python and PyCharm installed and ready to go!*

## What is Python?

Python is a programming language - a special language that lets you talk to computers and tell them what to do. It's named after the comedy group "Monty Python," not the snake! 😄

Python is one of the best languages for beginners because:
- It's easy to read and write (almost like English!)
- It's used by professional programmers at places like NASA, Google, and YouTube
- It's perfect for making games, websites, robots, and more!

## Your First Python Program: Hello, World!

Now for the exciting part - writing your first program! We'll start with the classic "Hello, World!" program that programmers have been using for decades as their first program.

### Step 1: Open PyCharm

PyCharm is the powerful code editor we set up in the preparation lesson.

1. Open PyCharm from your Applications folder or Launchpad
2. If you don't have a project open yet, create a new Pure Python project
3. Right-click in the project panel and create a new Python file called "hello_world"

### Step 2: Write Your First Line of Code

In the PyCharm editor, type the following exactly as shown:

```python
print("Hello, World!")
```

Now run your program by right-clicking in the editor and selecting "Run 'hello_world'" or by pressing the green play button.

You should see in the output panel at the bottom:

```
Hello, World!
```

**CONGRATULATIONS!** You just wrote your first Python program! 🎉

## Let's Understand What Happened

The `print()` function in Python is like a magical spell that makes text appear on the screen. Whatever you put between the parentheses and quotes will be displayed.

Let's try some more. Add these lines to your file:

```python
print("Hello, World!")
print("My name is Python Programmer!")
print("I'm learning to make awesome games!")
```

Run the program again to see all three messages appear!

## Adding Comments to Your Code

Comments are notes that you can add to your code. The computer ignores them, but they help people understand what your code does.

To write a comment in Python, use the `#` symbol:

```python
# This is a comment - the computer will ignore this line
print("But this line will be displayed!") # You can also put comments at the end of a line
```

## Variables: Storing Information

Variables are like magical containers that can hold information for you. You can give them names and put data inside them.

```python
player_name = "Alex"
player_age = 10
print("Hello, my name is", player_name, "and I am", player_age, "years old!")
```

Try changing the values and see what happens!

## Let's Make a Simple Greeting Program

Now let's put everything together to make a program that greets the user:

1. In PyCharm, create a new Python file called "greeting"
2. Type the following code:

```python
# My first Python program
print("Welcome to Python Game Programming!")

# Ask for the player's name
player_name = input("What is your name? ")

# Greet the player
print("Hello,", player_name, "! Let's start making games together!")
print("You are going to be an awesome game developer!")
```

3. Save the file (Cmd+S on Mac)
4. Run the program by right-clicking and choosing "Run 'greeting'" or pressing the green play button
5. When asked in the output panel, type your name and press Enter

Amazing! You've created a program that interacts with the user!

## Try It Yourself: Challenges

Before we end this lesson, here are some fun challenges to try:

1. **Personalize It**: Modify the greeting program to also ask for the user's age and favorite color.

2. **ASCII Art**: Use multiple print statements to create a simple picture. For example:

```python
print("   /\\")
print("  /  \\")
print(" /    \\")
print("/______\\")
print("  |  |")
print("  |__|")
```

3. **Story Starter**: Create a program that asks for a character name, a place, and an object, then uses those to start a story.

## What's Next?

In the next lesson, we'll learn more about variables and different types of data in Python. We'll start building the foundation for our game by understanding how to work with numbers, text, and make decisions in our code.

Remember, learning to code is like learning a new language or instrument - it takes practice! Don't worry if you don't understand everything right away. The more you play with Python, the better you'll get!

**Keep coding, future game developer!** 🚀