---
layout: lesson
title: "Lesson 1: Your First Python Program"
lang: en
next_lesson: lesson2.html
objectives:
  - Understand what Python is and why it's great for making games
  - Set up Python on your computer
  - Write your very first Python program
  - Learn about print statements, comments, and variables
---

# Your First Python Program

Hello, future game developer! Are you ready to start your coding adventure? In this first lesson, we're going to learn what Python is, set it up on your computer, and write our very first program!

## What is Python?

Python is a programming language - a special language that lets you talk to computers and tell them what to do. It's named after the comedy group "Monty Python," not the snake! 😄

Python is one of the best languages for beginners because:
- It's easy to read and write (almost like English!)
- It's used by professional programmers at places like NASA, Google, and YouTube
- It's perfect for making games, websites, robots, and more!

## Setting Up Python

Before we can start coding, we need to install Python on your computer. Ask a grown-up to help you with this part if needed.

### Step 1: Download Python

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click the big "Download Python" button
3. Run the installer that downloads

### Step 2: Install Python

During installation:
1. Make sure to check the box that says "Add Python to PATH"
2. Click "Install Now"
3. Wait for the installation to finish

### Step 3: Test Your Installation

Let's make sure Python is installed correctly:

1. Open the "Command Prompt" (Windows) or "Terminal" (Mac/Linux)
2. Type `python --version` and press Enter
3. You should see something like `Python 3.9.5` (the numbers might be different)

Great job! Python is now installed on your computer!

## Your First Python Program: Hello, World!

Now for the exciting part - writing your first program! We'll start with the classic "Hello, World!" program that programmers have been using for decades as their first program.

### Step 1: Open IDLE

IDLE is a simple program that comes with Python that lets you write and run Python code.

1. Search for "IDLE" on your computer and open it
2. You'll see a window called the "Python Shell" with some text and a prompt (`>>>`)

### Step 2: Write Your First Line of Code

At the prompt (`>>>`), type the following exactly as shown and press Enter:

```python
print("Hello, World!")
```

You should see:

```
Hello, World!
```

**CONGRATULATIONS!** You just wrote your first Python program! 🎉

## Let's Understand What Happened

The `print()` function in Python is like a magical spell that makes text appear on the screen. Whatever you put between the parentheses and quotes will be displayed.

Let's try some more:

```python
print("My name is Python Programmer!")
print("I'm learning to make awesome games!")
```

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

1. In IDLE, click on "File" and then "New File"
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

3. Save the file by clicking "File" then "Save As..." and name it `greeting.py`
4. Run the program by clicking "Run" then "Run Module" (or press F5)
5. When asked, type your name and press Enter

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