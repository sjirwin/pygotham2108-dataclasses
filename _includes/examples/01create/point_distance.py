from dataclasses import dataclass
from math import sqrt

@dataclass
class Point:
    x: int = 0
    y: int = 0

p = Point(x=5, y=-3)

dist = sqrt(p.x**2 + p.y**2)

print(f'Distance from origin to {p} is {dist}')
# Distance from origin to Point(x=5, y=-3) is 5.830951894845301
