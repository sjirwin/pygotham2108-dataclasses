class PointHand:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(x={self.x!r}, y={self.y!r})')
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return ((self.x, self.y) == (other.x, other.y))
        return NotImplemented
    def __ne__(self, other):
        if other.__class__ is self.__class__:
            return ((self.x, self.y) != (other.x, other.y))
        return NotImplemented
