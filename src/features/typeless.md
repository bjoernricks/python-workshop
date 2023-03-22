# Python variables are *typeless*

Variables are typeless

```python
a_variable = 1
```

instead of

```c
int a_variable = 1
```

Python's [type system](https://en.wikipedia.org/wiki/Type_system) is dynamic

```python
a_variable = "this is a string"
print(a_variable)
a_variable = 123 # this is a number
print(a_variable)
```

Python supports [optional types](https://docs.python.org/3/library/typing.html) since Python 3.5

```python
a_variable: int = 1
```

but nothing forbids

```python
a_variable: int = "this is a string"
```
