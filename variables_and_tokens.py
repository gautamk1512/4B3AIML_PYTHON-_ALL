# Topic 02: Variables and Tokens

# Questions
# 1. What is an identifier in Python?
# 2. List different data types in Python.
# 3. How do you write comments in Python?
# 4. What are operators? Give examples.
# 5. What are keywords? Name five.
# 6. Explain operator precedence with an example.
# 7. How do you convert data types in Python?

# Notes
# Identifiers: Names for variables, functions, etc. Must start with a letter or underscore.
# Data types: int, float, str, bool, list, tuple, dict, set.
# Comments: Use `#` for single-line, triple quotes for multi-line.
# Operators: Arithmetic (+, -, *), Comparison (==, !=), Logical (and, or), Assignment (=), Bitwise (&, |), Membership (in), Identity (is).
# Keywords: Reserved words like `if`, `for`, `while`, `def`, `class`.
# Operator precedence: Multiplication/division before addition/subtraction. Example: `2 + 3 * 4 = 14`.
# Type conversion: Use `int()`, `float()`, `str()`, etc.

# Solutions
# 1. Identifier example
my_variable = 10

# 2. Data types examples
an_int = 5
an_float = 3.14
a_string = "Hello"
a_bool = True
a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
a_dict = {"a": 1, "b": 2}
a_set = {1, 2, 3}

# 3. Comments examples
# This is a single-line comment
"""
This is a
multi-line comment
"""

# 4. Operators examples
sum_result = 2 + 3
is_equal = (2 == 3)
logical_and = (True and False)
assignment = 5
bitwise_and = 2 & 3
membership = 2 in [1, 2, 3]
identity = (an_int is 5)

# 5. Keywords examples
# if, for, while, def, class

# 6. Operator precedence example
result = 2 + 3 * 4 # result is 14

# 7. Type conversion examples
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
str_from_int = str(num_int)
