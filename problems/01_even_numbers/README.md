Extracting even  numbers
========================
The scope of this exercise is to create an `even()` function that will allow to extract all the even numbers from a given 
list of numbers and return them into a new list`.

For example, we would like to obtain the following kind of results:
```python
>>> even([1, 2, 3, 4, 5, 6, 2])
[2, 4, 6, 2]
>>> even([1, 3, 5, 7])
[]
>>> even(["1", "3", "something", "odd"])
[]
```

This function should also respect the rules:
* Does not remove duplicated values
* Ignores the non-integer elements from a list


Verifying your solution
-----------------------
To validate your solution, just run the following command (from this folder):
```shell script
pytest -v test_even.py
```
