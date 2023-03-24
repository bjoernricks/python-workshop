# if/elif/else Statement

The `if` statement can also be extended with additional conditions by using
`elif`. It is possible to add more then one `elif` statement.

A `elif` code block is only executed if its boolean expression evaluates to
`True` and all previous `if` and `elif` statements evaluated to `False`.

Additionally the `else` code block is only executed if all `if` and `elif`
statements evaluated to `False`.

```python
if condition:
    CODE_BLOCK
elif condition_2
    CODE_BLOCK_2
elif condition_x
    CODE_BLOCK_X
else:
    ELSE_CODE_BLOCK
```
Example:

```{literalinclude} if_elif_else.py
```
