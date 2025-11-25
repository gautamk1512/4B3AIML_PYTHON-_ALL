# Topic 26: Standard Library

# Questions
# 1. How do you use the math module?
# 2. How do you do string pattern matching?
# 3. How do you work with dates and times?

# Notes
# math: Provides mathematical functions
# re: Regular expressions for pattern matching
# datetime: Date and time manipulation

# Solutions
import math
print(math.sqrt(25))

import re
pattern = r'\d+'
result = re.findall(pattern, 'There are 24 apples and 17 oranges.')
print(result)

from datetime import datetime
now = datetime.now()
print(now)
