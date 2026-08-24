# ============================================================
# PYTHON BASICS
# ============================================================


# ============================================================
# 1. PRINT FUNCTION
# ============================================================

# The print() function is used to display text, variables,
# values, or other information on the screen.

print("Hello Lucky!")

# Text (strings) in Python can be written using either:
# double quotes (" ")
# or
# single quotes (' ')

print("Hello World")
print('Hello World')


# ============================================================
# 2. VARIABLES
# ============================================================

# Python does not have a special command for declaring variables.
# A variable is created automatically when you assign a value to it.

x = 5
y = "Sally"

# In the examples above:
#
# x stores the number 5.
# y stores the text "Sally".


# ============================================================
# 3. TYPE FUNCTION
# ============================================================

# The type() function is used to determine the data type
# of a variable or value.

# Example:

print(type(x))
print(type(y))

# Output:
#
# <class 'int'>
# <class 'str'>
#
# This means:
# x is an integer (int)
# y is a string (str)


# ============================================================
# 4. CASE SENSITIVE
# ============================================================

# Python is case-sensitive.
#
# This means that uppercase and lowercase letters are treated
# as different characters.

x = 5
X = 10

# x and X are two different variables.

print(x)
print(X)


# ============================================================
# 5. RULES FOR NAMING VARIABLES
# ============================================================

# There are several rules that should be followed when
# creating variable names in Python.

# Rule 1:
# The variable name must start with a letter or an underscore (_).

name = "Lucky"
_name = "Lucky"


# Rule 2:
# The variable name cannot start with a number.

# This is NOT allowed:
#
# 1name = "Lucky"


# Rule 3:
# The variable name can only contain:
#
# A-Z
# a-z
# 0-9
# _
#
# Example:

first_name = "Lucky"
age2 = 25

# Spaces and special characters such as @, -, and $ are
# not allowed in variable names.


# Rule 4:
# Variable names are case-sensitive.

name = "Lucky"
Name = "Jones"

# name and Name are different variables.


# Rule 5:
# Variable names cannot be Python keywords.
#
# Keywords are reserved words that already have a special
# meaning in Python.
#
# Examples of Python keywords include:
#
# if
# else
# for
# while
# class
# def
# return
# import
# True
# False
#
# Therefore, you should not use these words as variable names.


# ============================================================
# 6. MULTI-WORD VARIABLE NAMES
# ============================================================

# When a variable name contains multiple words,
# Python programmers commonly use different naming styles.


# ------------------------------------------------------------
# camelCase
# ------------------------------------------------------------

# The first word starts with a lowercase letter and
# subsequent words start with uppercase letters.

firstName = "Lucky"


# ------------------------------------------------------------
# PascalCase
# ------------------------------------------------------------

# Every word starts with an uppercase letter.

FirstName = "Lucky"


# ------------------------------------------------------------
# snake_case
# ------------------------------------------------------------

# Words are separated using underscores.
#
# This is the most commonly recommended style for
# normal Python variables.

first_name = "Lucky"


# ============================================================
# 7. PRINTING VARIABLES
# ============================================================

# The print() function can also be used to display
# the value stored inside a variable.

x = 5
y = "Sally"

print(x)
print(y)


# ============================================================
# PYTHON DATA STRUCTURES
# ============================================================

# Python has several built-in data structures that are
# used to store collections of data.
#
# Three important Python data structures are:
#
# 1. Lists
# 2. Tuples
# 3. Dictionaries


# ============================================================
# 8. LISTS
# ============================================================

# A list is an ordered and mutable sequence that allows
# duplicate elements.
#
# Ordered means that the elements maintain their position.
#
# Mutable means that the elements can be changed after
# the list has been created.
#
# Lists allow duplicate values.
#
# List elements are accessed using their index.
#
# Python indexing starts from 0.


# ------------------------------------------------------------
# LIST SYNTAX
# ------------------------------------------------------------

# Lists are created using square brackets [ ].

fruits = ["apple", "banana", "orange"]


# ------------------------------------------------------------
# ACCESSING LIST ELEMENTS
# ------------------------------------------------------------

# The first element has index 0.
# The second element has index 1.
# The third element has index 2.

print(fruits[0])
print(fruits[1])
print(fruits[2])


# ------------------------------------------------------------
# LIST PROPERTIES
# ------------------------------------------------------------

# 1. Lists can contain elements of different data types.

student = ["Lucky", 25, True, 75.5]

print(student)


# 2. List elements are accessed using their index,
#    starting from 0.

print(student[0])


# 3. Lists are mutable.
#
#    This means we can change an element after creating
#    the list.

student[0] = "Jones"

print(student)


# 4. Lists allow duplicate elements.

numbers = [1, 2, 3, 2, 4, 2]

print(numbers)


# ------------------------------------------------------------
# COMMON LIST OPERATIONS
# ------------------------------------------------------------

# append()
# Adds an element to the end of the list.

fruits.append("mango")

print(fruits)


# remove()
# Removes a specific element from the list.

fruits.remove("banana")

print(fruits)


# SLICING
# Slicing allows us to retrieve a portion of a list.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# The result contains:
#
# 20
# 30
# 40


# ============================================================
# 9. TUPLES
# ============================================================

# A tuple is an ordered and immutable sequence that allows
# duplicate elements.
#
# Ordered means that the elements maintain their position.
#
# Immutable means that the elements cannot be changed
# after the tuple has been created.
#
# Tuple elements are accessed using their index.
#
# Indexing starts from 0.


# ------------------------------------------------------------
# TUPLE SYNTAX
# ------------------------------------------------------------

# Tuples are commonly defined using parentheses ( ).

colors = ("red", "green", "blue")


# ------------------------------------------------------------
# ACCESSING TUPLE ELEMENTS
# ------------------------------------------------------------

# Just like lists, tuple indexing starts from 0.

print(colors[0])
print(colors[1])
print(colors[2])


# ------------------------------------------------------------
# TUPLE PROPERTIES
# ------------------------------------------------------------

# 1. Tuples can contain elements of different data types.

person = ("Lucky", 25, True, 75.5)

print(person)


# 2. Tuple elements are accessed using their index,
#    starting from 0.

print(person[0])


# 3. Tuples are immutable.
#
#    This means that their elements cannot be modified
#    after the tuple has been created.


# This would cause an error:
#
# person[0] = "Jones"


# 4. Tuples allow duplicate elements.

numbers = (1, 2, 3, 2, 4, 2)

print(numbers)


# ============================================================
# 10. DICTIONARIES
# ============================================================

# A dictionary is a mutable collection of key-value pairs.
#
# Dictionaries are used to store data where each value
# can be accessed using a key.
#
# Each key must be unique.
#
# In modern Python, dictionaries preserve insertion order,
# although conceptually they are commonly taught as
# key-value mappings rather than index-based sequences.


# ------------------------------------------------------------
# DICTIONARY SYNTAX
# ------------------------------------------------------------

# Dictionaries use curly brackets { }.
#
# Each item is written as:
#
# key: value

student = {
    "name": "Lucky",
    "age": 25,
    "course": "Computer Science"
}


# ------------------------------------------------------------
# ACCESSING DICTIONARY VALUES
# ------------------------------------------------------------

# Dictionary values are accessed using their keys.

print(student["name"])
print(student["age"])
print(student["course"])


# ------------------------------------------------------------
# DICTIONARY PROPERTIES
# ------------------------------------------------------------

# 1. Dictionary keys must be unique.

student = {
    "name": "Lucky",
    "age": 25
}


# If the same key is written more than once,
# the later value replaces the previous value.

student = {
    "name": "Lucky",
    "name": "Jones"
}

print(student)


# The result will contain:
#
# "name": "Jones"


# 2. Dictionary keys must be immutable/hashable types.
#
# Common examples include:
#
# strings
# integers
# tuples
#
# Example:

person = {
    "name": "Lucky",
    1: "Student"
}


# 3. Dictionary values can be of any data type.

person = {
    "name": "Lucky",
    "age": 25,
    "skills": ["Python", "JavaScript"],
    "is_student": True
}

print(person)


# 4. Dictionaries provide fast lookup and retrieval
#    of values based on their keys.

print(person["skills"])


# ============================================================
# QUICK COMPARISON
# ============================================================

# LIST
#
# - Ordered
# - Mutable
# - Allows duplicates
# - Uses square brackets [ ]
# - Accessed using indexes
#
# Example:
#
# fruits = ["apple", "banana", "orange"]


# TUPLE
#
# - Ordered
# - Immutable
# - Allows duplicates
# - Uses parentheses ( )
# - Accessed using indexes
#
# Example:
#
# colors = ("red", "green", "blue")


# DICTIONARY
#
# - Stores key-value pairs
# - Mutable
# - Keys must be unique
# - Uses curly brackets { }
# - Values are accessed using keys
#
# Example:
#
# student = {
#     "name": "Lucky",
#     "age": 25
# }


# ============================================================
# END OF PYTHON DATA STRUCTURES NOTES
# ============================================================



DATA TYPES
sequence types ( list,tuple, range)
mapping type (dict) dictionary
set type ( set frozenset)


string conversions 
  ==str()coverts the value to a string
  ==repr() returns string rep of an object
  ==format() formatting of strings using placeholders and variable substitution



 control flow statements
     1.if statement:- executes if the condiotoon of a statement is True
     2.Elif statements:-checks additional statements if the previos conditions were false
     3.Else:- executes if all the all the previous conditions were false 