# if Statement

Boolean conditions are used mostly in `if` statements to execute code
conditionally. The code block following an `if` statement is only executed if
the boolean expression evaluates to `True`.

```python
if condition:
    CODE_BLOCK
```

Example:

```{literalinclude} if.py
```

To check the boolean evaluation of an expression you can use the `bool()`
function.

```{code-block} python
:caption: Python REPL

>>> bool("some text")
True
>>> bool([])
False
```
