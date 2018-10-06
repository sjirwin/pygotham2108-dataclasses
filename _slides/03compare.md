---
title: How do they compare with existing data structures
---

# Comparison To Existing Data Structures

--

### Named Tuple

- Intentionally behave like a ```tuple```
- Immutable
- No field options
- Cannot add methods
- Descriptive ```repr```
- Python 2.6 and later

--

### Dictionary

- Values accessed by keys, not attributes
- No default values
- Cannot add methods
- Semi-descriptive ```repr```
- All Python versions

--

### Default Dictionary

- Values accessed by keys, not attributes
- Same default_factory applied to all entries
- Cannot add methods
- Semi-descriptive ```repr```
- Python 2.5 and later

--

### Hand Written Class

- Dataclass *is* a class
  - Equivalent memory
  - Equivalent speed for object creation and attribute access
- More work since you have to write (and test) all the special methods

--

### Hand Written Class Using ```slots```

- Slightly smaller memory
- Faster object creation and attribute access
- Prevents adding additional attributes
- More work since you have to write (and test) all the special methods

--

### Attrs

- Not part of the Python standard library
- _Slightly_ more verbose syntax
- Has additional features (e.g., validators, converters)
  - One of the inspirations for dataclasses
- Supports all mainstream Python versions, including Python 2.7 and PyPy
