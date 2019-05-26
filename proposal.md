# Proposal

## Abstract
The PEP 557 dataclasses module was added in Python 3.7 and so is one of the newest features of the language. Now that they are here, they bring a few questions with them. In this talk, we will explore some of those questions.

## Description
The PEP 557 dataclasses module is one of the new features added in Python 3.7 and are a decorator which generates the boiler-plate code needed by a data container class. In addition to providing access to stored data values by name, they provide a easy mechanism for including additional features such as default values and customized ordering.

In this talk we will explore dataclasses from a data container perspective by asking several questions. 

- How should one use dataclasses?
- What functionality do dataclasses provide?
- How do these features compare to existing data structures in the standard library like NamedTuple, and dict?
- What about the third-party package attrs?
- What are some additional features of dataclasses?
- When might one want to use dataclasses?

## Outline
- Introduction (1 min)
- How to create a dataclass? (2 min)
- Functionality: How do they compare with existing data structures? (10 min)
  - regular Python class
  - namedtuple
  - dict
  - attrs
- What are some additional features of dataclasses? (5 min)
  - default values
  - order
  - default_factory
- When might I want to use dataclasses? (2 min)
- Conclusion (1 min)