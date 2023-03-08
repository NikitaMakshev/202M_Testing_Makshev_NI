import doctest


class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a: int, b: int, c: int):
    """
    Function for checking type of triangle
    :param a: first side of triangle (int)
    :param b: second side of triangle (int)
    :param c: third side of triangle (int)
    :return: type of triangle (str)
    :raises: IncorrectTriangleSides: if sides was set incorrectly
    >>> get_triangle_type(7, 7, 10)
    'isosceles'
    >>> get_triangle_type(7, 7, 7)
    'equilateral'
    >>> get_triangle_type(7, 9, 11)
    'nonequilateral'
    >>> get_triangle_type('1','7','1')
    Traceback (most recent call last):
     ...
    IncorrectTriangleSides: Incorrect Triangle Sides
    >>> get_triangle_type(7, 5, 1)
    Traceback (most recent call last):
     ...
    IncorrectTriangleSides: Incorrect Triangle Sides
    """

    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Incorrect Triangle Sides")
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise IncorrectTriangleSides("Incorrect Triangle Sides")

    if a != b != c:
        return "nonequilateral"
    elif a == b == c:
        return "equilateral"
    else:
        return "isosceles"


if __name__ == '__main__':
    doctest.testmod()