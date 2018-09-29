---
title: When might I want to use dataclasses
---

# Guidelines For Usage

--

### When To Use

- Need a mutable data holder
- Want/need the special methods, but do not want to write them

--

### When Not To Use

- Need to support Python versions prior to 3.7
  - Backport available for Python 3.6 via ```pip```
- Require API compatibility with tuples or dicts
- Require extended features
  - Value validation or conversion
  - Type validation
