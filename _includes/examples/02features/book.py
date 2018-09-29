from dataclasses import dataclass, field
from datetime import date

@dataclass
class Book:
    title: str
    author: str
    acquired: date = field(compare=False)
