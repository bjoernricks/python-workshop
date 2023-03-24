# Strings and Bytes

Strings contain a sequence of characters aka. text [^str].


```{literalinclude} str.py
```

Since Python 3 [Unicode](https://en.wikipedia.org/wiki/Unicode) is used for
representing the characters.

Before they were just bytes in the memory [^bytes].
Therefore Python 3 introduced the bytes type for being able to handle binary
data too.

```{literalinclude} bytes.py
```

[^str]:[String type in the Python documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
[^bytes]:[Bytes type in the Python documentation](https://docs.python.org/3/library/stdtypes.html#bytes-objects)

