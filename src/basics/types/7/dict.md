# Dict

A Python `dict` contains a key to value mapping aka. hashmap [^dict]. Dicts are
mutable objects. That means their content can be changed in place.

Keys and values can be arbitrary values [^hashable].

```{literalinclude} dict.py
```

[^dict]:[Dict type in the Python documentation](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

[^hashable]: A single limitation exists, keys need to be [hashable](https://docs.python.org/3/glossary.html#term-hashable).
