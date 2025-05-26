---
layout: lesson
title: "Preparation: Setting Up Your Programming Environment"
lang: en
permalink: /en/lessons/preparation/
next_lesson: /en/lessons/lesson1/
order: 0
objectives:
  - Install Python on your Mac computer
  - Download and set up PyCharm IDE for programming
  - Test that everything is working correctly
  - Get familiar with the PyCharm interface
---

# Getting Your Mac Ready for Python Programming

Before we start our exciting journey into game programming, we need to set up the right tools on your computer. Think of this like getting your art supplies ready before painting a masterpiece!

We'll be installing two important programs:
1. **Python** - This is the programming language we'll use to create games
2. **PyCharm** - This is a special text editor designed specifically for writing Python code

Don't worry if this seems complicated at first - we'll go through each step carefully, and once it's set up, you won't need to do this again!

## Part 1: Installing Python

Python is the programming language we'll use throughout our lessons. Let's get it installed on your Mac.

### Step 1: Download Python

1. Open your web browser (Safari, Chrome, or Firefox)
2. Go to [python.org/downloads](https://www.python.org/downloads/)
3. You'll see a big yellow button that says "Download Python 3.x.x" (the numbers might be different - that's okay!)

*[Screenshot placeholder: Python.org download page showing the yellow download button]*

4. Click on this yellow download button
5. A file will start downloading - it will be called something like "python-3.x.x-macosx10.9.pkg"
6. Wait for the download to finish (you'll see it in your Downloads folder or at the bottom of your browser)

*[Screenshot placeholder: Download progress in browser]*

### Step 2: Install Python

1. Find the downloaded file (it's probably in your Downloads folder)
2. Double-click on the file to start the installer

*[Screenshot placeholder: Python installer file in Downloads folder]*

3. You'll see a welcome screen for the Python installer - click "Continue"

*[Screenshot placeholder: Python installer welcome screen]*

4. On the next screen, read through the important information and click "Continue"
5. You'll see the software license agreement - click "Continue" and then "Agree"
6. Choose where to install Python (the default location is fine) and click "Continue"
7. Click "Install" - you might need to enter your Mac's password

*[Screenshot placeholder: Python installation location screen]*

8. Wait for the installation to complete - this might take a few minutes
9. When you see "The installation was successful," click "Close"

*[Screenshot placeholder: Successful installation screen]*

### Step 3: Verify Python Installation

Let's make sure Python was installed correctly:

1. Open the "Terminal" app on your Mac:
   - Press `Command + Space` to open Spotlight search
   - Type "Terminal" and press Enter

*[Screenshot placeholder: Spotlight search showing Terminal]*

2. In the Terminal window, type exactly: `python3 --version`
3. Press Enter
4. You should see something like "Python 3.x.x" appear

*[Screenshot placeholder: Terminal showing Python version]*

If you see the Python version number, congratulations! Python is successfully installed.

## Part 2: Installing PyCharm

PyCharm is a powerful program that makes writing Python code much easier. It's like having a smart assistant that helps you write code!

### Step 1: Download PyCharm

1. Go to [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/)
2. Make sure "macOS" is selected at the top
3. You'll see two versions: "Professional" and "Community"
4. Click "Download" under **Community** (it's free and perfect for learning!)

*[Screenshot placeholder: PyCharm download page showing Community edition]*

5. The download will start - it's a big file (about 500MB) so it might take a while
6. Wait for "pycharm-community-2023.x.x.dmg" to finish downloading

*[Screenshot placeholder: Download progress for PyCharm]*

### Step 2: Install PyCharm

1. Find the downloaded PyCharm file in your Downloads folder
2. Double-click on the ".dmg" file

*[Screenshot placeholder: PyCharm DMG file in Downloads]*

3. A new window will open showing the PyCharm application and an Applications folder
4. Drag the PyCharm icon to the Applications folder icon

*[Screenshot placeholder: Dragging PyCharm to Applications folder]*

5. Wait for the copy to complete
6. Close the installer window
7. You can now find PyCharm in your Applications folder or Launchpad

### Step 3: Set Up PyCharm for the First Time

1. Open PyCharm from your Applications folder or Launchpad
2. The first time you open it, you might see a security warning - click "Open"

*[Screenshot placeholder: Security warning dialog]*

3. PyCharm will ask about importing settings - choose "Do not import settings" and click "OK"

*[Screenshot placeholder: Import settings dialog]*

4. Accept the User Agreement by clicking "Accept"
5. Choose whether to send usage statistics (either choice is fine) and click "Continue"

*[Screenshot placeholder: Usage statistics dialog]*

6. PyCharm will show you a welcome screen with themes - pick the one you like (you can change this later)

*[Screenshot placeholder: Theme selection screen]*

7. You might see screens about plugins - you can skip these by clicking "Skip remaining and set defaults"

*[Screenshot placeholder: Plugin configuration screens]*

### Step 4: Configure Python in PyCharm

Now we need to tell PyCharm where to find the Python we just installed:

1. On the PyCharm welcome screen, click "New Project"

*[Screenshot placeholder: PyCharm welcome screen with New Project button]*

2. You'll see a "New Project" dialog
3. Make sure "Pure Python" is selected on the left
4. Choose a location for your project (the default is fine)
5. Expand the "Python Interpreter" section by clicking the arrow
6. Make sure "Add interpreter" is selected
7. Choose "System Interpreter" from the dropdown
8. Click the "..." button next to the interpreter path

*[Screenshot placeholder: New Project dialog with interpreter settings]*

9. Navigate to `/usr/bin/python3` or `/usr/local/bin/python3` (PyCharm might find it automatically)
10. Click "OK" to select the interpreter
11. Click "Create" to create your first project

*[Screenshot placeholder: Interpreter selection dialog]*

### Step 5: Test Everything is Working

Let's create a simple program to test that everything is set up correctly:

1. PyCharm will open with your new project
2. Right-click in the project panel on the left and choose "New" → "Python File"

*[Screenshot placeholder: Right-click menu showing New Python File option]*

3. Name your file "test" and press Enter
4. PyCharm will create a new file and open it in the editor
5. Type the following code exactly as shown:

```python
print("Hello, World! Python and PyCharm are working!")
```

*[Screenshot placeholder: PyCharm editor with the test code]*

6. Right-click in the editor and choose "Run 'test'"

*[Screenshot placeholder: Right-click menu showing Run option]*

7. You should see a panel at the bottom showing the output: "Hello, World! Python and PyCharm are working!"

*[Screenshot placeholder: Output panel showing the result]*

## Part 3: Getting Familiar with PyCharm

Now that everything is working, let's quickly learn about the PyCharm interface:

### Main Areas of PyCharm

*[Screenshot placeholder: PyCharm interface with labeled areas]*

1. **Project Panel** (left side): Shows all your files and folders
2. **Editor** (center): Where you write your code
3. **Tool Windows** (bottom): Shows output, errors, and other information
4. **Menu Bar** (top): Contains all the commands and options

### Useful Features for Beginners

1. **Auto-completion**: As you type, PyCharm will suggest code for you
2. **Error highlighting**: If you make a mistake, PyCharm will underline it in red
3. **Running programs**: Right-click in your code and choose "Run" to test your program
4. **File management**: Use the project panel to organize your code files

*[Screenshot placeholder: Examples of auto-completion and error highlighting]*

## Troubleshooting Common Issues

If something doesn't work, here are the most common fixes:

### Python Not Found
- Make sure you installed Python 3 (not Python 2)
- Try typing `python3 --version` in Terminal instead of `python --version`

### PyCharm Can't Find Python
- In PyCharm, go to "PyCharm" → "Preferences" → "Project" → "Python Interpreter"
- Click the gear icon and "Add"
- Choose "System Interpreter" and browse to `/usr/bin/python3`

### Permission Errors
- Make sure you entered your Mac password when installing
- Try running Terminal as an administrator if needed

## You're All Set!

Congratulations! You now have:
- ✅ Python installed and working
- ✅ PyCharm set up and configured
- ✅ A working development environment
- ✅ Basic knowledge of the PyCharm interface

You're ready to start learning Python programming! In the next lesson, we'll dive into writing your first real Python programs and start building the foundation for creating amazing games.

Remember: if you run into any problems, don't worry! Programming setup can be tricky, and even experienced programmers sometimes need help with installation. Ask a parent, teacher, or friend for help if you get stuck.

**You're ready to start your programming adventure!** 🚀 