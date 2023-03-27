# Python supports functional and object oriented programming

```{code-block}
:caption: Python with just functions

def do_something():
    ...

def foo():
    do_something()
```

```{code-block}
:caption: Python with classes

class Bar:
    def do_something(self):
        ...

class Baz:
    def run(self):
        bar = Bar()
        bar.do_something()
```

Or mix both

```{code-block}
:caption: Python: A class calling a function

def do_something():
    ...

class Baz:
    def run(self):
        do_something()
```
