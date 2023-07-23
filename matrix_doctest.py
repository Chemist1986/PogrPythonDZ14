import doctest
from matrix import Matrix

# Example for DocTest
def matrix_doctest_example():
    """
    >>> matrix = Matrix(2, 3)
    >>> matrix.data = [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix)
    1 2 3
    4 5 6
    """

if __name__ == "__main__":
    doctest.testmod()