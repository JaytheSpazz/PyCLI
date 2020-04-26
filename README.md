# PyCLI
PyCLI is a dead simple python command line builder!

## How To Install
`pip3 install -i https://test.pypi.org/simple/ pycli`

## How To Use

import the module:

```python
from pycli import CLI
cli = CLI()
````

Create a new function:

```python
import random
def random_function(x, y):
    """Generates a random number between x and y.
    Usage:
      random x y
    """
    print(random.randint(x,y))
```

Or as part of a class:

```python
import random

class randclass(random.Random):
    def __ init __(self):
        self.rand_seed = 1234
    def random_function(x,y):
        """Generates a random number between x and y.
        Usage:
          random x y"""
        print(self.randint(x,y))
```
Now add your function to the CLI function list:

`cli.add_function('random', random_function)` (for regular functions)

`cli.add_function('random', randclass.random_function)`(for class methods and functions)

Next, set a "welcome" message to make your new CLI look professional:

```python
cli.set_message("""Welcome to my super awesome python CLI!
With this new tool you can quickly generate command line
interfaces that capture user input without having to figure
out how to handle all those inputs yourself!
""")
```

Finally, call the loop function:

`cli.loop()`

And if you want to make it even better, on linux machines add:

```#!/usr/bin/python3```

to the top line of the file and have `cli.loop()` be called by main:

```python
if __name__ in '__main__':
    cli.loop()
```

