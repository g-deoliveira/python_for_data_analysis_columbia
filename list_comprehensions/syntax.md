## List-comprehensions
Basic syntax:
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
## Dictionary-comprehensions
Basic syntax
```python
{k(i,j,k,...):v(i,j,k,...) for i,j,k... in <iterables>}
```
equivalent to
```python
d = {}
for i,j,k,... in <iterables>:
    key = k(i,j,k,...)
    value = v(i,j,k,...)
    d[key] = value
```
Syntax for dict-comprehension with addition of filter condition
```python
{k(i,j,k,...):v(i,j,k,...) for i,j,k... in <iterables> if filter_condition(i,j,...)}
```
equivalent to
```python
d = {}
for i,j,k,... in <iterables>:
    if filter_condition(i,j,k,...):
        key = k(i,j,k,...)
        value = v(i,j,k,...)
        d[key] = value
```
## Set-comprehensions
Basic syntax
```python
x = {function(i,j,...) for i,j,... in <iterables>}
```
equivalent to
```python
x = set()
for i,j,... in <iterables>:
    x.add(function(i,j,...))
```
If we include a filter, the syntax becomes:
```python
x = {function(i,j,...) for i,j,... in <iterables> if filter_condition(i,j,...)}
```
equivalent to:
```python
x = set()
for i,j,... in <iterables>:
    if filter_condition(i,j,...):
        x.add(function(i,j,...))
```
