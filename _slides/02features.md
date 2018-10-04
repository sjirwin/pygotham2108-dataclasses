---
title: What are some additional features of dataclasses
---

# Additional Features

--

### Basic Decorator

These uses of <span style="color:indianred">```dataclass()```</span> are equivalent

```python
@dataclass
class Cls:
    ...

@dataclass()
class Cls:
    ...

@dataclass(init=True, repr=True, eq=True)
class Cls:
    ...
```

--

### Decorator Options

- <span style="color:indianred">```init```</span>: default is ```True```
- <span style="color:indianred">```repr```</span>: default is ```True```
- <span style="color:indianred">```eq```</span>: default is ```True```
- <span style="color:indianred">```order```</span>: default is ```False```
- <span style="color:indianred">```frozen```</span>: default is ```False```
- <span style="color:indianred">```unsafe_hash```</span>: default is ```False```

--

### Ordered Dataclass

Methods added when ```order``` is ```True```
```python
__lt__()
__le__()
__gt__()
__ge__()
```
Example
```python
def __lt__(self, other):
    if other.__class__ is self.__class__:
        return (self.x, self.y) < (other.x, other.y)
    return NotImplemented
```

--

### Frozen Data Classes

- Makes dataclass instances immutable
- Assigning to fields will generate an exception

--

### Unsafe Hash

- If ```unsafe_hash``` is ```False``` (the default):
  - <span style="color:indianred">```__hash__()```</span> method is added depending on how ```eq``` and ```frozen``` are set
- If ```unsafe_hash``` is ```True```:
  - **Not Recommended**
  - Forces <span style="color:indianred">```dataclass()```</span> to create a <span style="color:indianred">```__hash__()```</span> method

--

### Decorator Options Caveats

- Some decorator option will be ignored if class defines some methods
  - <span style="color:indianred">```__init__()```</span>, ```init``` option is ignored
  - <span style="color:indianred">```__repr__()```</span>, ```repr``` option is ignored
  - <span style="color:indianred">```__eq__()```</span>, ```eq``` option is ignored

--

### Decorator Options Caveats

- Decorator can raise <span style="color:indianred">```TypeError```</span>
  - ```order``` is ```True``` and class defines any order methods (e.g., <span style="color:indianred">```__lt__()```</span>)
  - ```frozen``` is ```True``` and class defines either <span style="color:indianred">```__setattr__()```</span> or <span style="color:indianred">```__delattr__()```</span>
  - ```unsafe_hash``` is ```True``` and class defines <span style="color:indianred">```__hash__()```</span>

--

### Beyond Simple Fields

- Basic syntax can define simple field and default value (only)
- <span style="color:indianred">```field()```</span> function has additional features

--

### ```field()``` Function

- Use <span style="color:indianred">```field()```</span> function for additional control
  - ```repr```: if ```False```, field excluded from <span style="color:indianred">```repr```</span>
  - ```init```: if ```False```, field excluded from <span style="color:indianred">```init```</span>
  - ```compare```: if ```False```, field excluded from <span style="color:indianred">```eq```</span>
  - ```default_factory```:
    - Needed to set default value to a mutable type
    - Can be any zero argument function

--

### Exclude From Compare

```python
{% include examples/02features/book.py %}
```
```python
book1 = Book(title='Moby-Dick', author='Melville, Herman',
             acquired=date(2017,12,25))
book2 = Book(title='Moby-Dick', author='Melville, Herman',
             acquired=date.today())
print("Are book1 and book2 equal?", book1==book2)
# book1 and book2 are equal? True
```

--

### Mutable Type As Default Values

- Recall the issue mutable types cause for function default values

```python
def func(my_list=[]):
    my_list += [1]
    return my_list

```
```python
>>> func()
[1]
>>> func()
[1, 1]

```

--

This issue is avoided with <span style="color:indianred">```field()```</span>

```python
{% include examples/02features/library.py %}
```
```python
my_book = Book('Drive','Pink, Daniel H',date.today())
lib1 = Library()
lib2 = Library()
lib1.books += [my_book]
print(lib2.books)
# []
```

--

### An Incomplete List Of Other Features

- <span style="color:indianred">```dataclasses.asdict()```</span>
- <span style="color:indianred">```dataclasses.astuple()```</span>
- <span style="color:indianred">```dataclasses.replace()```</span>
- Post-init processing
- Init-only variables
- Class variables
- Inheritance
