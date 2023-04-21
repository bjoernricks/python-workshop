# Methods

Functions on classes are called **methods**. Methods are functions *bound* to a
class. A constructor is also a method of the class. The constructor just has
a special name (`__init__`).

The first argument of a method is named `self`. It refers the the instance of
the class.

```{note}

The name `self` is just a convention. Any name could be used, but just to stick
to `self` and forget about that. Changing it to another name would just confuse
other developers.
```

```{literalinclude} methods.py
```
