# Python's Special Methods

Python uses some *special* methods to implement behavior. These methods are
called *dunder* (double under) methods.

We already discovered a dunder method, the constructor method `__init__`.

Some other important special methods:

* `__str__` return a string for printable output
* `__repr__` return a string representation of the object
* `__len__` return the length of an object (mostly interesting for container
  objects)
* `__add__` allow to use the `+` operator with the object
* `__eq___` allow to compare objects with the `==` operator

You can find [additional special methods in the Python docs](https://docs.python.org/3.10/reference/datamodel.html#special-method-names).

Example:

```{literalinclude} example.py
```
