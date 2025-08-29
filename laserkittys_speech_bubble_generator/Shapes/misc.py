class Point:
    """
    basically a fancy 2D tuple
    """

    x: float
    y: float

    def __init__(self, a,b):
        self.x = a
        self.y = b

    def __eq__(self, p):
        if not (type(p) is Point): raise TypeError(f'value not a Point: {p}')
        return self.x == p.x and self.y == p.y
    
    def __ne__(self, p):
        if not (type(p) is Point): raise TypeError(f'value not a Point: {p}')
        return self.x != p.x or self.y != p.y

    def __add__(self, p):
        if not (type(p) is Point): raise TypeError(f'value not a Point: {p}')
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        if not (type(p) is Point): raise TypeError(f'value not a Point: {p}')
        return Point(self.x - p.x, self.y - p.y)
    
    def __mul__(self, n):
        if not (type(n) in [int, float]): raise TypeError(f'value not an int or float: {n}')
        return Point(self.x * n, self.y * n)

    def __rmul__(self, n):
        if not (type(n) in [int, float]): raise TypeError(f'value not an int or float: {n}')
        return Point(self.x * n, self.y * n)

    def __truediv__(self, n):
        if not (type(n) in [int, float]): raise TypeError(f'value not an int or float: {n}')
        return Point(self.x / n, self.y / n)
    
    def __repr__(self):
        return f'Point: (x: {self.x} y: {self.y})'

    def __getitem__(self, i) -> int:
        if type(i) is not int: raise TypeError(f'index must be an int, received: {type(i)}')
        if i == 0: return self.x
        if i == 1: return self.y
        raise ValueError(f'index must be either 0 or 1: {i}')

    def __len__(self) -> int:
        return 2