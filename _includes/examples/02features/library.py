from dataclasses import dataclass, field
from typing import List
from book import Book

@dataclass
class Library:
    books: List[Book] = field(default_factory=list)
