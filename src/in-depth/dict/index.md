# Dicts

Dicts are used for two kinds of data.

First of all to represent a single entry of a data structure. For example

```python
user_1 = {
    "first_name": "John",
    "last_name': "Doe",
    "active": True
    "age": 23,
}

users = [user_1]
```

or a map to (cumulated) values. For example

```python
fruits = {
    "apple": 12,
    "pear": 6,
    "orange": 10,
    "kiwi": 9,
}
```

## Getting an item

```{literalinclude} get.py
```

## Adding and updating items

```{literalinclude} update.py
```

## Deleting an item

```{literalinclude} delete.py
```

## Keys

```{literalinclude} keys.py
```

## Values

```{literalinclude} values.py
```

## Items

```{literalinclude} items.py
```
