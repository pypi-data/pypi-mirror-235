# The Trojan Rabbit #
A collection of python extras (and an hommage to Monty Python's Holy Grail)

## Decorator @dynamicmethod ##
This decorator provides the missing option for method definitions:

```
| decorator           | 1st parameter passed when called from |
|                     | instance / class                      |
|---------------------+---------------------------------------|
| - (instance method) | instance / None                       |
| @classmethod        | class    / class                      |
| @staticmethod       | -        / -                          |
| @dynamicmethod      | instance / class                      |
```

### Usage ###

```python
from trojan_rabbit.dynamicmethod import dynamicmethod


class Knight:
    description = "a knight of the Round Table"

    def __init__(self, name, attribute):
        self.name = name
        self.attribute = attribute

    @dynamicmethod
    def whoami(caller):
        if isinstance(caller, Knight):
            print(f"{caller.attribute.capitalize()} Sir {caller.name}", end=', ')
        print(caller.description)


robin = Knight("Robin", "brave")

Knight.whoami
# output: <bound method Knight.whoami of <class '__main__.Knight'>>

robin.whoami
# output: <bound method Knight.whoami of <__main__.Knight object at 0x7f377073fe50>>

Knight.whoami()
# output: a knight of the Round Table

robin.whoami()
# output: Brave Sir Robin, a knight of the Round Table
```
