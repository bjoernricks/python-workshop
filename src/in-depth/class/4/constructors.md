# Constructors

We have seen that classes can share data via class variables. Also it is
possible to assign specific data to instances. To generalize and unify instance
variables constructors are used.

Constructors are called to initialize an object. They can define and change the
data of an instance. Constructors are special class functions with the following
signature `def __init__(self, arg1, arg2)`.

The first argument **self** is a special argument referring to the current
instance of the class.

Examples:

```{literalinclude} constructors.py
```
