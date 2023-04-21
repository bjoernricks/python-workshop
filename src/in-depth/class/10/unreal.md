# More (unreal) Example

Lets make the example even more *unreal*. A `Fruit` can be added to a `Fruit`
and the `Fruit` prints itself now.

Advantages over the last example:
* A `Basket` doesn't know anything about the amount anymore
* The `Fruit` is responsible for its own print output
* `Basket` and `Fruit` have much in common now (they have a very similar *interface*)

Example:

```{literalinclude} example.py
```
