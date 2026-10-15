# Knowledge base for the Python Q&A chatbot.
# Each entry has:
#   question : the main question
#   variants : other ways people might ask it (helps the matching)
#   answer   : the reply shown to the user (supports Markdown and code blocks)

KNOWLEDGE_BASE = [
    {
        "question": "What is Python?",
        "variants": "python introduction meaning explain python language define python why use python",
        "answer": r"""Python is a popular, beginner-friendly programming language. It is easy to read, runs on every major system, and is used for web development, data science, machine learning, automation and more.""",
    },
    {
        "question": "How do I install Python?",
        "variants": "download python setup python on windows install python and add to path",
        "answer": r"""Download the installer from **python.org/downloads**, run it, and tick **Add python.exe to PATH** on the first screen. Then open a terminal and type `python --version` to check it worked.""",
    },
    {
        "question": "How do I print something in Python?",
        "variants": "hello world print function display output show text on screen",
        "answer": r"""Use the `print()` function:

```python
print("Hello, World!")
print("Sum:", 2 + 3)
```""",
    },
    {
        "question": "What is a variable in Python?",
        "variants": "how to create a variable store a value declare variable assign value naming rules",
        "answer": r"""A variable is a name that stores a value. You create one by assigning with `=`:

```python
age = 20
name = "Asha"
```
Names can contain letters, digits and underscores, cannot start with a digit, and are case-sensitive.""",
    },
    {
        "question": "What are the data types in Python?",
        "variants": "basic data types int float str bool types of data check type of variable",
        "answer": r"""The basic types are `int` (whole numbers), `float` (decimals), `str` (text) and `bool` (True or False). Collections include `list`, `tuple`, `set` and `dict`. Use `type(x)` to check a value's type.""",
    },
    {
        "question": "How do I write comments in Python?",
        "variants": "single line comment multi line comment hash symbol docstring",
        "answer": r"""Start a line with `#` to write a comment. Python ignores it.

```python
# This is a comment
x = 5  # this is also a comment
```""",
    },
    {
        "question": "How do I take input from the user?",
        "variants": "input function read keyboard input ask user to enter value get user input",
        "answer": r"""Use `input()`. It always returns text, so convert it if you need a number:

```python
name = input("Your name: ")
age = int(input("Your age: "))
```""",
    },
    {
        "question": "How do I convert one data type to another?",
        "variants": "type casting type conversion int to string string to int float conversion",
        "answer": r"""Use the conversion functions `int()`, `float()`, `str()` and `bool()`:

```python
int("10")     # 10
str(25)       # "25"
float("3.5")  # 3.5
```""",
    },
    {
        "question": "What are the arithmetic operators in Python?",
        "variants": "plus minus multiply divide modulus floor division exponent power math operators",
        "answer": r"""`+` add, `-` subtract, `*` multiply, `/` divide (gives a float), `//` floor division, `%` remainder, `**` power.

```python
7 // 2   # 3
7 % 2    # 1
2 ** 3   # 8
```""",
    },
    {
        "question": "What are comparison and logical operators?",
        "variants": "equal not equal greater than and or not boolean operators relational operators",
        "answer": r"""Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`. Logical: `and`, `or`, `not`.

```python
age = 20
print(age >= 18 and age < 60)   # True
```""",
    },
    {
        "question": "How does the if else statement work?",
        "variants": "conditional statement elif if condition decision making syntax of if",
        "answer": r"""```python
marks = 72
if marks >= 80:
    print("Distinction")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
```
Python checks the conditions from top to bottom and runs the first block that is true.""",
    },
    {
        "question": "How does a for loop work?",
        "variants": "for loop syntax iterate over list loop through items repeat code loop example",
        "answer": r"""A `for` loop goes through each item of a sequence:

```python
for fruit in ["apple", "mango", "kiwi"]:
    print(fruit)
```""",
    },
    {
        "question": "How does a while loop work?",
        "variants": "while loop syntax repeat until condition false infinite loop",
        "answer": r"""A `while` loop repeats as long as its condition is true:

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```
Make sure the condition eventually becomes false, or the loop never ends.""",
    },
    {
        "question": "What are break and continue?",
        "variants": "stop a loop skip an iteration exit loop early loop control statements pass",
        "answer": r"""`break` stops the loop completely. `continue` skips the rest of the current round and moves to the next one. `pass` does nothing and is used as a placeholder.""",
    },
    {
        "question": "What does the range function do?",
        "variants": "range syntax start stop step generate numbers loop n times",
        "answer": r"""`range()` produces a sequence of numbers:

```python
range(5)         # 0, 1, 2, 3, 4
range(2, 6)      # 2, 3, 4, 5
range(0, 10, 2)  # 0, 2, 4, 6, 8
```""",
    },
    {
        "question": "What is a list in Python?",
        "variants": "create a list list example access list items list indexing ordered collection",
        "answer": r"""A list is an ordered, changeable collection written in square brackets:

```python
nums = [10, 20, 30]
print(nums[0])    # 10
nums[1] = 25
```""",
    },
    {
        "question": "What are the common list methods?",
        "variants": "append remove pop insert sort reverse add item to list delete item from list",
        "answer": r"""```python
a = [3, 1, 2]
a.append(4)      # add at the end
a.insert(0, 9)   # add at a position
a.remove(1)      # remove a value
a.pop()          # remove the last item
a.sort()         # sort in place
a.reverse()      # reverse in place
```""",
    },
    {
        "question": "What is a tuple?",
        "variants": "tuple example create a tuple immutable sequence tuple syntax",
        "answer": r"""A tuple is like a list but **cannot be changed** after it is created. It is written with round brackets:

```python
point = (4, 7)
print(point[0])   # 4
```""",
    },
    {
        "question": "What is a set in Python?",
        "variants": "set example unique values remove duplicates set operations union intersection",
        "answer": r"""A set stores **unique** items with no order. It is handy for removing duplicates:

```python
s = {1, 2, 2, 3}
print(s)                 # {1, 2, 3}
print({1, 2} | {2, 3})   # union
print({1, 2} & {2, 3})   # intersection
```""",
    },
    {
        "question": "What is a dictionary in Python?",
        "variants": "dict example key value pairs create a dictionary access dictionary values add key",
        "answer": r"""A dictionary stores data as key-value pairs:

```python
student = {"name": "Ravi", "age": 20}
print(student["name"])
student["city"] = "Chennai"
for k, v in student.items():
    print(k, v)
```""",
    },
    {
        "question": "What is list comprehension?",
        "variants": "list comprehension syntax create list in one line shorter loop comprehension example",
        "answer": r"""A short way to build a list from a loop:

```python
squares = [x * x for x in range(5)]       # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]
```""",
    },
    {
        "question": "What is slicing in Python?",
        "variants": "slice a list slice a string start stop step reverse a list negative index",
        "answer": r"""Slicing takes part of a sequence using `[start:stop:step]`:

```python
s = "PYTHON"
s[1:4]    # "YTH"
s[:3]     # "PYT"
s[::-1]   # "NOHTYP" (reversed)
```""",
    },
    {
        "question": "What are the common string methods?",
        "variants": "upper lower strip split join replace find string functions string operations",
        "answer": r"""```python
s = "  Hello World  "
s.strip()              # removes spaces at both ends
s.upper()              # "  HELLO WORLD  "
s.lower()
s.replace("World", "Python")
"a,b,c".split(",")     # ["a", "b", "c"]
"-".join(["a", "b"])   # "a-b"
```""",
    },
    {
        "question": "What are f-strings?",
        "variants": "string formatting format string insert variable in string f string example",
        "answer": r"""f-strings let you put variables directly inside text:

```python
name = "Asha"
marks = 91.456
print(f"{name} scored {marks:.1f}")   # Asha scored 91.5
```""",
    },
    {
        "question": "How do I define a function in Python?",
        "variants": "create a function def keyword function syntax call a function function example",
        "answer": r"""Use the `def` keyword:

```python
def greet(name):
    return "Hello, " + name

print(greet("Asha"))
```""",
    },
    {
        "question": "What are default arguments, args and kwargs?",
        "variants": "function parameters default value variable number of arguments star args double star kwargs",
        "answer": r"""```python
def power(x, n=2):          # n has a default value
    return x ** n

def total(*args):           # any number of values
    return sum(args)

def show(**kwargs):         # any number of name=value pairs
    print(kwargs)
```""",
    },
    {
        "question": "What is the difference between return and print?",
        "variants": "return vs print function output returning a value print inside function",
        "answer": r"""`print()` only **shows** a value on the screen. `return` **sends the value back** to the code that called the function, so you can store or use it. A function with no `return` gives back `None`.""",
    },
    {
        "question": "What is a lambda function?",
        "variants": "anonymous function lambda syntax lambda example small one line function",
        "answer": r"""A lambda is a small unnamed function written in one line:

```python
square = lambda x: x * x
print(square(5))   # 25
```""",
    },
    {
        "question": "What are local and global variables?",
        "variants": "variable scope global keyword inside function outside function scope of a variable",
        "answer": r"""A variable created inside a function is **local** and only works there. One created outside is **global**. To change a global variable inside a function, declare it with the `global` keyword.""",
    },
    {
        "question": "What is recursion?",
        "variants": "recursive function function calling itself factorial using recursion base case",
        "answer": r"""Recursion is when a function calls itself. It needs a **base case** to stop:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```""",
    },
    {
        "question": "What are classes and objects?",
        "variants": "object oriented programming oop create a class create an object class example attributes methods",
        "answer": r"""A class is a blueprint; an object is something built from it:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says woof")

d = Dog("Tommy")
d.bark()
```""",
    },
    {
        "question": "What are __init__ and self?",
        "variants": "constructor in python self keyword meaning init method purpose",
        "answer": r"""`__init__` is the **constructor**. It runs automatically when an object is created and sets up its data. `self` refers to the current object, so each object can keep its own values.""",
    },
    {
        "question": "What is inheritance in Python?",
        "variants": "parent class child class inherit from a class super function reuse code oop inheritance example",
        "answer": r"""Inheritance lets a class reuse another class's features:

```python
class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):      # Dog inherits from Animal
    def bark(self):
        print("woof")

Dog().eat()
```""",
    },
    {
        "question": "What is polymorphism and encapsulation?",
        "variants": "oop concepts four pillars of oop method overriding data hiding private variables",
        "answer": r"""**Polymorphism**: different classes can have a method with the same name that behaves differently. **Encapsulation**: keeping data inside a class and controlling access, for example with names starting with an underscore like `_balance`. The other OOP pillars are inheritance and abstraction.""",
    },
    {
        "question": "How does exception handling work?",
        "variants": "try except finally handle errors avoid program crash catch error raise exception",
        "answer": r"""Use `try` and `except` to handle errors without crashing:

```python
try:
    x = int(input("Number: "))
    print(10 / x)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
```""",
    },
    {
        "question": "How do I read and write files in Python?",
        "variants": "file handling open a file read a text file write to a file with open append mode",
        "answer": r"""```python
with open("notes.txt", "w") as f:    # write
    f.write("Hello")

with open("notes.txt", "r") as f:    # read
    print(f.read())
```
Modes: `r` read, `w` write (overwrites), `a` append. `with` closes the file automatically.""",
    },
    {
        "question": "What are modules and how do I import them?",
        "variants": "import statement import library from import use math module create own module",
        "answer": r"""A module is a file of Python code you can reuse:

```python
import math
print(math.sqrt(16))

from random import randint
print(randint(1, 6))
```""",
    },
    {
        "question": "What is pip?",
        "variants": "install a library package manager pip install command install packages",
        "answer": r"""`pip` is Python's package installer. Run it in the terminal:

```
pip install pandas
pip list
```""",
    },
    {
        "question": "What is a virtual environment?",
        "variants": "venv create virtual environment why use venv activate environment separate project libraries",
        "answer": r"""A virtual environment is a separate Python setup for one project, so its libraries do not clash with others. On Windows:

```
python -m venv venv
venv\Scripts\activate
```""",
    },
    {
        "question": "What is pandas?",
        "variants": "pandas library dataframe data analysis read csv in python series",
        "answer": r"""pandas is a library for working with tables of data. Its main object is the **DataFrame**.

```python
import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())
```""",
    },
    {
        "question": "What is NumPy?",
        "variants": "numpy library arrays numerical python numpy array example",
        "answer": r"""NumPy is a library for fast numerical work with arrays:

```python
import numpy as np
a = np.array([1, 2, 3])
print(a * 2)    # [2 4 6]
```""",
    },
    {
        "question": "What is the difference between a list and a tuple?",
        "variants": "list vs tuple tuple vs list when to use tuple mutable immutable difference",
        "answer": r"""Lists use `[ ]` and **can be changed** (add, remove, edit). Tuples use `( )` and **cannot be changed**. Tuples are slightly faster and are used for fixed data such as coordinates.""",
    },
    {
        "question": "What does mutable and immutable mean?",
        "variants": "mutable vs immutable objects which types can be changed immutable data types",
        "answer": r"""**Mutable** objects can be changed after creation: list, dict, set. **Immutable** objects cannot: int, float, str, tuple, bool.""",
    },
    {
        "question": "What is a decorator in Python?",
        "variants": "decorator example at symbol wrapper function modify a function",
        "answer": r"""A decorator adds extra behaviour to a function without changing its code:

```python
def shout(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@shout
def hello():
    print("Hello")
```""",
    },
    {
        "question": "What is a generator and the yield keyword?",
        "variants": "generator function yield vs return lazy evaluation iterator",
        "answer": r"""A generator produces values one at a time using `yield`, saving memory:

```python
def count_up(n):
    for i in range(1, n + 1):
        yield i

for x in count_up(3):
    print(x)
```""",
    },
    {
        "question": "What do map and filter do?",
        "variants": "map function filter function apply function to list functional programming reduce",
        "answer": r"""```python
nums = [1, 2, 3, 4]
list(map(lambda x: x * 2, nums))         # [2, 4, 6, 8]
list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]
```
`map` transforms every item. `filter` keeps only items that pass a test.""",
    },
    {
        "question": "What are enumerate and zip?",
        "variants": "loop with index loop over two lists together enumerate example zip example",
        "answer": r"""```python
for i, name in enumerate(["A", "B"]):     # index and value
    print(i, name)

for n, m in zip(["A", "B"], [90, 80]):    # two lists together
    print(n, m)
```""",
    },
    {
        "question": "Why is indentation important in Python?",
        "variants": "indentation error spaces and tabs code block unexpected indent",
        "answer": r"""Python uses **indentation** (usually 4 spaces) to mark blocks of code instead of curly brackets. Wrong or mixed indentation causes an `IndentationError`.""",
    },
    {
        "question": "What is None and what are boolean values?",
        "variants": "none type true false null in python empty value truthy falsy",
        "answer": r"""`None` means "no value" (Python's version of null). Booleans are `True` and `False`. Empty things like `0`, `""`, `[]` and `None` count as false in conditions.""",
    },
    {
        "question": "What does if __name__ == '__main__' mean?",
        "variants": "main function in python name main check run script directly vs import",
        "answer": r"""It runs code only when the file is **run directly**, not when it is imported as a module:

```python
def main():
    print("Running")

if __name__ == "__main__":
    main()
```""",
    },
    {
        "question": "How do I find the length of a list or string?",
        "variants": "len function count items size of list number of characters",
        "answer": r"""Use `len()`:

```python
len([1, 2, 3])    # 3
len("Python")     # 6
```""",
    },
    {
        "question": "How do I sort a list in Python?",
        "variants": "sort vs sorted ascending descending order sort a list of numbers reverse sort",
        "answer": r"""```python
a = [3, 1, 2]
a.sort()                    # changes the list itself
b = sorted(a, reverse=True) # returns a new sorted list
```""",
    },
    {
        "question": "What is PEP 8?",
        "variants": "python style guide coding conventions naming conventions clean code",
        "answer": r"""PEP 8 is Python's official style guide. Key points: 4 spaces for indentation, `snake_case` for variable and function names, `CamelCase` for class names, and lines under about 79 characters.""",
    },
]
