---
title: How to create a dataclass
---

# Basic Features

--

### Simple Dataclass

```python
{% include examples/01create/point.py %}
```

```python
>>> Point(x=1, y=2)
# Point(x=1, y=2)
```

```python
>>> Point()
# TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
```

--

### Default Values

```python
{% include examples/01create/point_default_val.py %}
```

```python
>>> Point()
# Point(x=0, y=0)

>>> Point(y=3)
# Point(x=0, y=3)
```

--

### Class Methods

```python
{% include examples/01create/point_with_method.py %}
```

```python
>>> p = Point(x=1, y=3)
>>> p.distance_to(Point(x=-2, y=-1))
# 5.0

```

--

### Types Are Hints

```python
{% include examples/01create/point_default_val.py %}
```

```python
>>> Point(x=2.71828, y=3.14159)
# Point(x=2.71828, y=3.14159)

>>> Point(x='Hello', y='PyGotham')
# Point(x='Hello', y='PyGotham')
```

--

## Field Access

```python
{% include examples/01create/point_distance.py %}
```

--

### Methods Added To Simple Dataclass

```python
__init__()
__repr__()
__eq__()
```

--

### What Those Methods Look Like

```python
def __init__(self, x: int = 0, y: int = 0) -> None:
    self.x = x
    self.y = y
```
```python
def __repr__(self):
    return (f'{self.__class__.__qualname__}'
            f'(x={self.x!r}, y={self.y!r})')
```
```python
def __eq__(self, other):
    if other.__class__ is self.__class__:
        return ((self.x, self.y) == (other.x, other.y))
    return NotImplemented
```
