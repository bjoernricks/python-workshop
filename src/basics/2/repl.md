# Run Code in the Python Interpreter Directly

Calling the `python3` executable without arguments stats the [Python REPL](https://realpython.com/python-repl/) (Read-Eval-Print Loop).

The REPL allows you to run Python code interactively while working on a project
or learning the language. It's best for testing out some code snippets.

```{code-block} sh
:caption: Shell
python3
```

```{code-block} python
:caption: Python REPL
Python 3.10.7 (main, Mar 10 2023, 10:47:39) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>> 24 * 60
1440
```

`Shift + Enter` in VSCode starts a Python REPL and runs the marked code inside
this REPL.
