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
# ============================================================
# PYTHON DATA TYPES
# ============================================================

# Data types specify what kind of value a variable contains.
#
# Python has several built-in data types.
#
# Some important categories include:
#
# 1. Sequence types
# 2. Mapping types
# 3. Set types
# 4. Text type
# 5. Numeric types
# 6. Boolean type
#
# In these notes, we will focus on:
#
# - Sequence types
# - Mapping types
# - Set types
# - String conversions
# - Control flow statements


# ============================================================
# 1. SEQUENCE TYPES
# ============================================================

# Sequence types are used to store collections of values
# in a particular order.
#
# The main sequence types we are covering are:
#
# 1. list
# 2. tuple
# 3. range


# ------------------------------------------------------------
# LIST
# ------------------------------------------------------------

# A list is an ordered and mutable collection of values.
#
# Mutable means that we can change the contents of a list
# after creating it.
#
# Lists are created using square brackets [ ].

numbers = [10, 20, 30, 40]

print(numbers)


# Lists can contain duplicate values.

names = ["Lucky", "Jones", "Lucky"]

print(names)


# Lists can contain different data types.

student = ["Lucky", 25, True, 75.5]

print(student)


# ------------------------------------------------------------
# TUPLE
# ------------------------------------------------------------

# A tuple is an ordered and immutable collection of values.
#
# Immutable means that the values cannot be changed after
# the tuple has been created.
#
# Tuples are commonly created using parentheses ( ).

coordinates = (10, 20)

print(coordinates)


# Tuples can contain duplicate values.

numbers = (10, 20, 10, 30)

print(numbers)


# Tuples can also contain different data types.

student = ("Lucky", 25, True)

print(student)


# ------------------------------------------------------------
# RANGE
# ------------------------------------------------------------

# The range type represents a sequence of numbers.
#
# It is commonly used with loops when we want to repeat
# an operation a certain number of times.
#
# Example:

numbers = range(5)

print(numbers)


# The range above represents:
#
# 0, 1, 2, 3, 4
#
# Notice that 5 is not included.


# We can use a for loop to display the values.

for number in range(5):
    print(number)


# ============================================================
# 2. MAPPING TYPE
# ============================================================

# A mapping type stores data using key-value pairs.
#
# The main mapping type in Python is:
#
# dictionary (dict)


# ------------------------------------------------------------
# DICTIONARY
# ------------------------------------------------------------

# A dictionary stores information as:
#
# key : value
#
# Dictionaries are created using curly brackets { }.

student = {
    "name": "Lucky",
    "age": 25,
    "course": "Python"
}

print(student)


# We access dictionary values using their keys.

print(student["name"])
print(student["age"])
print(student["course"])


# Dictionary keys must be unique.

student = {
    "name": "Lucky",
    "age": 25
}


# Dictionary values can have different data types.

student = {
    "name": "Lucky",
    "age": 25,
    "skills": ["Python", "JavaScript"],
    "is_student": True
}

print(student)


# ============================================================
# 3. SET TYPES
# ============================================================

# A set is an unordered collection of unique values.
#
# Sets do not allow duplicate elements.
#
# Python has two main set types:
#
# 1. set
# 2. frozenset


# ------------------------------------------------------------
# SET
# ------------------------------------------------------------

# A set is mutable.
#
# This means that we can add or remove elements after
# creating the set.
#
# Sets are created using curly brackets { }.

fruits = {"apple", "banana", "orange"}

print(fruits)


# Sets automatically remove duplicate values.

numbers = {1, 2, 3, 2, 4, 3}

print(numbers)

# The duplicate values are removed.
#
# The set contains:
#
# 1, 2, 3, 4


# We can add an element to a set using add().

fruits.add("mango")

print(fruits)


# We can remove an element using remove().

fruits.remove("banana")

print(fruits)


# ------------------------------------------------------------
# FROZENSET
# ------------------------------------------------------------

# A frozenset is similar to a set, but it is immutable.
#
# This means that once a frozenset has been created,
# its elements cannot be changed.

numbers = frozenset([1, 2, 3, 4])

print(numbers)


# We cannot use add() or remove() on a frozenset.
#
# For example, this would cause an error:
#
# numbers.add(5)


# ============================================================
# QUICK DATA TYPE COMPARISON
# ============================================================

# LIST
#
# list = [1, 2, 3]
#
# - Ordered
# - Mutable
# - Allows duplicates
# - Uses [ ]


# TUPLE
#
# tuple = (1, 2, 3)
#
# - Ordered
# - Immutable
# - Allows duplicates
# - Uses ( )


# RANGE
#
# range(5)
#
# - Represents a sequence of numbers
# - Commonly used with loops


# DICTIONARY
#
# dictionary = {"name": "Lucky"}
#
# - Stores key-value pairs
# - Mutable
# - Keys must be unique
# - Uses { }


# SET
#
# set = {1, 2, 3}
#
# - Unordered collection
# - Mutable
# - Does not allow duplicates
# - Uses { }


# FROZENSET
#
# frozenset = frozenset([1, 2, 3])
#
# - Unordered
# - Immutable
# - Does not allow duplicates


# ============================================================
# STRING CONVERSIONS
# ============================================================

# String conversion means converting values or objects
# into a string representation.
#
# Three useful functions/methods are:
#
# 1. str()
# 2. repr()
# 3. format()


# ============================================================
# 4. str()
# ============================================================

# The str() function converts a value into a string.
#
# It is commonly used when we want to convert numbers,
# booleans, or other values into text.

age = 25

age_string = str(age)

print(age_string)

print(type(age_string))


# The result is:
#
# 25
#
# But the data type is:
#
# <class 'str'>


# Another example:

number = 100

text = str(number)

print("The number is " + text)


# Without str(), combining a number directly with a string
# using + would cause an error.
#
# Example:
#
# print("The number is " + number)
#
# This is NOT allowed because number is an integer.


# ============================================================
# 5. repr()
# ============================================================

# The repr() function returns a string representation of
# an object.
#
# It is mainly useful for developers because it attempts
# to show a representation that clearly describes the object.
#
# repr() can make special characters visible.

name = "Lucky"

print(str(name))
print(repr(name))


# Example with a newline:

message = "Hello\nLucky"

print(str(message))

print(repr(message))

# str() displays the newline as an actual line break.
#
# repr() shows the escape sequence:
#
# 'Hello\nLucky'
#
# This makes repr() useful when debugging and inspecting values.


# ============================================================
# 6. format()
# ============================================================

# The format() method is used to insert values into strings
# using placeholders.
#
# Placeholders are represented using curly brackets { }.


name = "Lucky"
age = 25

message = "My name is {} and I am {} years old.".format(
    name,
    age
)

print(message)


# Output:
#
# My name is Lucky and I am 25 years old.


# ------------------------------------------------------------
# FORMAT USING POSITIONAL PLACEHOLDERS
# ------------------------------------------------------------

# We can specify the position of values using numbers
# inside the curly brackets.

name = "Lucky"
age = 25

message = "My name is {0} and I am {1} years old.".format(
    name,
    age
)

print(message)


# ------------------------------------------------------------
# FORMAT USING NAMED PLACEHOLDERS
# ------------------------------------------------------------

# We can also give names to the placeholders.

message = "My name is {name} and I am {age} years old.".format(
    name="Lucky",
    age=25
)

print(message)


# ============================================================
# CONTROL FLOW STATEMENTS
# ============================================================

# Control flow statements determine which parts of a program
# should execute and when they should execute.
#
# They allow a program to make decisions based on conditions.
#
# The main conditional statements are:
#
# 1. if
# 2. elif
# 3. else


# ============================================================
# 7. IF STATEMENT
# ============================================================

# An if statement executes a block of code if its condition
# evaluates to True.
#
# Syntax:
#
# if condition:
#     statement


age = 20

if age >= 18:
    print("You are an adult.")


# In this example:
#
# age >= 18
#
# is the condition.
#
# If the condition is True, Python executes the code
# inside the if block.


# ------------------------------------------------------------
# ANOTHER IF EXAMPLE
# ------------------------------------------------------------

temperature = 30

if temperature > 25:
    print("It is hot today.")


# ============================================================
# 8. ELIF STATEMENT
# ============================================================

# elif means "else if".
#
# An elif statement checks another condition when the
# previous condition was False.
#
# We can use multiple elif statements when we have
# several possible conditions.


marks = 75

if marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")


# In this example:
#
# First Python checks:
#
# marks >= 80
#
# If that is False, it checks:
#
# marks >= 70
#
# Since 75 is greater than 70, it prints:
#
# Grade B


# ============================================================
# 9. ELSE STATEMENT
# ============================================================

# The else statement executes when all previous conditions
# are False.
#
# The else statement does not have a condition.
#
# Syntax:
#
# if condition:
#     statement
#
# else:
#     statement


age = 15

if age >= 18:
    print("You are an adult.")

else:
    print("You are a minor.")


# Since age is 15:
#
# age >= 18
#
# is False.
#
# Therefore, Python executes the else block.


# ============================================================
# IF + ELIF + ELSE
# ============================================================

# We can combine all three conditional statements
# to make more complex decisions.

marks = 85

if marks >= 80:

    print("Grade A")

elif marks >= 70:

    print("Grade B")

elif marks >= 60:

    print("Grade C")

else:

    print("You need to improve.")


# Python checks the conditions from top to bottom.
#
# Once it finds a condition that is True,
# it executes that block and skips the remaining
# elif and else blocks.


# ============================================================
# CONTROL FLOW SUMMARY
# ============================================================

# IF
#
# Executes code when a condition is True.
#
# Example:
#
# if age >= 18:
#     print("Adult")


# ELIF
#
# Checks another condition when the previous condition
# was False.
#
# Example:
#
# elif age >= 13:
#     print("Teenager")


# ELSE
#
# Executes when all previous conditions are False.
#
# Example:
#
# else:
#     print("Child")


# ============================================================
# FINAL QUICK SUMMARY
# ============================================================

# DATA TYPES
#
# Sequence:
#     list
#     tuple
#     range
#
# Mapping:
#     dict
#
# Set:
#     set
#     frozenset
#
#
# STRING CONVERSIONS
#
# str()
#     Converts a value into a string.
#
# repr()
#     Returns a developer-oriented string representation
#     of an object.
#
# format()
#     Inserts values into strings using placeholders.
#
#
# CONTROL FLOW
#
# if
#     Executes when a condition is True.
#
# elif
#     Checks another condition when the previous condition
#     was False.
#
# else
#     Executes when all previous conditions are False.