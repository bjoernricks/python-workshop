# Variables

As already mentioned Python variables are *typeless* in the regard to not caring
about which type gets assigned.

```{literalinclude} typeless.py
```

You can also assign expressions to variables.

```{literalinclude} expression.py
```

But actually if a value gets assigned variables have a type.

```{literalinclude} typefull.py
```

Output can be found here [^output]

You can get the type of a variable by calling the `type` function on the
variable.

```{literalinclude} type.py
```

[^output]: Code output

    ```python
     >>> output = "Hello World"
     >>> print(output.upper())
     HELLO WORLD
     >>> output = 24 * 60
     >>> print(output.upper())
     Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     AttributeError: 'int' object has no attribute 'upper'
    ```
