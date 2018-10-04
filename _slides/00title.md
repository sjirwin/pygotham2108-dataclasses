---
title: Main title
---

## Dataclasses Are Here!

## Now What?

<span style="font-size:smaller">PyGotham &mdash; 2018-Oct-06</span>
<center>
Scott Irwin<br/>
<img src="images/bloomberg-logo-black.svg"
     style="border: none; box-shadow: none; height: 45px"
     alt="Bloomberg"><br/>
</center>

--

## What We Will Cover

- What Is A Dataclass?
- Basic Features
- Additional Features
- Comparison To Existing Data Structures
- Guidelines For Usage

--

### What Is A Dataclass?

- A "normal" Python class
  - But one intended to be used as a data container
  - Same memory and speed as any class
- Think _"mutable namedtuples with defaults"_

--

### Quick Background

- <span style="color:indianred">```dataclasses```</span> module
  - added to standard library in Python 3.7
  - written by Eric V. Smith
- Described in:
  - Python [docs](https://docs.python.org/3/library/dataclasses.html)
  - [PEP 557](https://www.python.org/dev/peps/pep-0557/)

--

### A Few More Details

- Module includes:
  - <span style="color:indianred">```@dataclass```</span> - class decorator which generates special methods (a.k.a. dunder methods)
  - <span style="color:indianred">```field()```</span> - function which provides additional control over **field** definitions
- Field definitions rely on Variable Annotations ([PEP 526](https://www.python.org/dev/peps/pep-0526/))
