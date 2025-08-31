# Point

a useful helper class used within SpeechBubble implementations

basically a fancy tuple

## Attributes
- `x` float
- `y` float

## Examples

```python
A = Point(1,2)
B = Point(1,2)
A == B: True
```

```python
A = Point(1,2)
B = Point(3,4)
A == B: False
```

```python
A = Point(1,2)
B = Point(3,4)
A + B: Point(4,6)
```

```python
A = Point(1,2)
B = Point(3,4)
B - A: Point(2,2)
```

```python
A = Point(1,2)
B = 2
A * B: Point(2,4)
B * A: Point(2,4)
```

```python
A = Point(1,2)
B = 2
A / B: Point(1/2,2)
```

```python
A = Point(1,2)
A.x  == 1: True
A[0] == 1: True
A.y  == 2: True
A[1] == 2: True
A[2]     : IndexOutOfBoundsError
```