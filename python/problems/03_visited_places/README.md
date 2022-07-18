Visited places
==============
For this exercise, the aim is to collect the different places visited by someone, and then display them.
During the collecting phase, we will apply the following rules:
* Each place will be represented by a string with the format `"<city>,<country>"`
* If no comma is entered, the user should be displayed an error message
* The collection process ends when a user enters a blank line
* Each country should appear only once in the collection

The presentation of the data collected should:
* Capitalize cities and countries names
* Group the cities visited by countries
* Display the results in alphabetical order
* Display the number of visits in a city, if it has been visited more than once

For example, we should be able to have the following behaviour:
```shell script
>>> visited = collect_places()
>>> Where did you go? Berlin, Germany
>>> Where did you go? Berlin, Germany
>>> Where did you go? Milano, Italy
>>> Where did you go? Valencia, Spain
>>>
>>>
>>> display_places(visited)
>>> Italy
>>>   Milano
>>> Germany
>>>   Berlin (2)
>>> Spain
>>>   Valencia
```

Verifying your solution
-----------------------
To validate your solution, just run the following command (from this folder):
```shell script
pytest -v test_visited_places.py
```
