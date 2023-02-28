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