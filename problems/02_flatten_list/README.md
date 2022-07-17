Flattening a list
=================
The scope of this exercise is to create a `flatten` function that will allow to flatten the given list, respecting the 
optional maximum depth specified.

For example, we would like to obtain the following kind of results:
```python
>>> flatten([1, 2, 3, [4, 5, [6]]], 2)
[1, 2, 3, 4, 5, 6]
>>> flatten([1, 2, 3, [4, 5, [6]]])
[1, 2, 3, [4, 5, [6]]]
```

This function should also respect the rules:
* Raise an exception if the `max_depth` attribute is negative or not even an `int`
* Does not flatten anything by default
* Does not remove duplicated values
* Does not impact the other iterable classes contained in the list


Verifying your solution
-----------------------
To validate your solution, just run the following command (from this folder):
```shell script
pytest -v test_flatten.py
```
