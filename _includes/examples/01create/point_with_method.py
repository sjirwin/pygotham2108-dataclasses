from dataclasses import dataclass
from math import sqrt

@dataclass
class Point:
    x: int = 0
    y: int = 0

    def distance_to(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
