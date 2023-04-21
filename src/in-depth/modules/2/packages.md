# Packages

Packages extend modules for building a hierarchy of namespaces. A Python package
is a directory containing a `__init__.py` file. It may contain additional
modules and packages.

Example:

```{literalinclude} fruits/__init__.py
:caption: fruits/\_\_init__.py
```

```{literalinclude} fruits/container.py
:caption: fruits/container.py
```

```{literalinclude} example.py
:caption: example.py
```

```{code-block} sh
:caption: running the code

cd src/in-depth/modules/2
python3 example.py
```
