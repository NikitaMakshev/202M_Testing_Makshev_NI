from triangle_func import IncorrectTriangleSides


class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides('Incorrect Triangle Sides')
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
            raise IncorrectTriangleSides('Incorrect Triangle Sides')

    def triangle_type(self) -> str:
        if self.a != self.b != self.c:
            return "nonequilateral"
        elif self.a == self.b == self.c:
            return "equilateral"
        else:
            return "isosceles"

    def perimeter(self) -> int:
        return self.a + self.b + self.c