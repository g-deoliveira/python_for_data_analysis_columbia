Syntax for list-comprehension:
```python
x = [function(i,j,...) for i,j,... in <iterables>]
```
equivalent to:
```python
x = []
for i,j,... in <iterables>:
    x.append(function(i,j,...))
```
If we include a filter, the syntax becomes:
```python
x = [function(i,j,...) for i,j,... in <iterables> if filter_condition(i,j,...)]
```
equivalent to:
```python
x = []
for i,j,... in <iterables>:
    if filter_condition(i,j,...):
        x.append(function(i,j,...))
```