class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = p1

    print(p1 == p2)   # True  -> __eq__ compares values
    print(p1 is p2)   # False -> different objects in memory
    print(p1 is p3)   # True  -> same object, same identity
    print(p1 == p3)   # True  -> same values too
