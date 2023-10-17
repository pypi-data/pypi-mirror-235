# STDIO Python

Facilitating functions related to reading and writing data on the terminal.

## Installation

```bash
pip install stdio
```

## Usage (write)

```python
from stdio import clear
from stdio import write
from stdio import skipline
from stdio import deleteline
from stdio import deletechar

# Usage examples:
clear()             # Clears the terminal
write("start")      # Writes the string "start" to the terminal
skipline()          # Skips one line in the terminal
write("a")          # Writes the string "a" to the terminal
skipline()          # Skips one line in the terminal
write("b")          # Writes the string "b" to the terminal
skipline()          # Skips one line in the terminal
write("c")          # Writes the string "c" to the terminal
deleteline()        # Deletes the last line from the terminal
skipline()          # Skips one line in the terminal
write("123")        # Writes the string "123" to the terminal
write("456")        # Writes the string "456" to the terminal
write("789")        # Writes the string "789" to the terminal
deletechar()        # Deletes the last character in the terminal
skipline(2)         # Skips two lines in the terminal
write("end!!!")     # Writes the string "end!!!" to the terminal
deletechar(2)       # Deletes the last 2 characters in the terminal
skipline(2)         # Skips two lines in the terminal

# Output

'''
start
a
b
12345678

end!

'''
```

## Usage (read)

```python
from stdio import read
from stdio import readint
from stdio import readfloat
from stdio import clear
from stdio import write
from stdio import skipline

# Usage examples:
clear()         # Clears the terminal

# Prompt user for name, age, and height
name = read("Enter your name: ")            # Example input: "Thiago"
age = readint("Enter your age: ")           # Example input: "26"
height = readfloat("Enter your height: ")   # Example input: "1.8"

clear()         # Clears the terminal

# Writes the collected information to the terminal
write(f"Your name is {name}, your age is {age}, and height is {height}")
skipline(2)

# Output

'''
Your name is Thiago, your age is 26, and height is 1.8

'''
```

## Usage (basic loader)

```python
from stdio import clear
from stdio import skipline
from stdio import write
from stdio import Loader
from time import sleep


clear()
write("Example: Basic Usage")
skipline()
ldr = Loader()
while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

# Output

'''
Example: Basic Usage

100/100 ███████████████████████
'''
```

## Usage (custom loader)

```python
from stdio import clear
from stdio import skipline
from stdio import write
from stdio import Loader
from time import sleep


clear()
#######################
write("Example: Custom Min and Max Progress")
skipline()
ldr = Loader(
    min_progress=50,
    max_progress=200
)
while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Custom Fill and Empty Strings")
skipline()
ldr = Loader(
    fill_string=">",
    empty_string="-"
)

while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Custom Pre-string")
skipline()
ldr = Loader(
    pre_string=""
)
while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Starting with Custom Progress")
skipline()
ldr = Loader(
    current_progress=30
)
while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Decreasing Progress")
skipline()
ldr = Loader(
    current_progress=100
)
while ldr.current_progress > ldr.min_progress:
    sleep(0.1)
    ldr.increase(-2)

skipline(2)

#######################
write("Example: Manual Progress Entry")
skipline()
ldr = Loader(
    current_progress=100
)

ldr.progress(10)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(80)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(10)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(80)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(10)
sleep(0.1)
ldr.progress(10)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(80)
sleep(0.1)
ldr.progress(100)

# Output

'''
Example: Custom Min and Max Progress

200/200 ███████████████████████

Example: Custom Fill and Empty Strings

100/100 >>>>>>>>>>>>>>>>>>>>>>>

Example: Custom Pre-string

███████████████████████████████

Example: Starting with Custom Progress

100/100 ███████████████████████

Example: Decreasing Progress

0/100

Example: Manual Progress Entry

100/100 ███████████████████████
'''
```
