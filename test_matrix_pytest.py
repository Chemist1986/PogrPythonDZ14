import pytest
from matrix import Matrix

def test_matrix_creation():
    matrix = Matrix(2, 3)
    assert matrix.rows == 2
    assert matrix.cols == 3

def test_matrix_addition():
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    result = matrix1 + matrix2

    expected_result = Matrix(2, 3)
    expected_result.data = [[8, 10, 12], [14, 16, 18]]

    assert result == expected_result

def test_matrix_multiplication():
    matrix1 = Matrix(3, 2)
    matrix1.data = [[1, 2], [3, 4], [5, 6]]

    matrix2 = Matrix(2, 4)
    matrix2.data = [[7, 8, 9, 10], [11, 12, 13, 14]]

    result = matrix1 * matrix2

    expected_result = Matrix(3, 4)
    expected_result.data = [[29, 32, 35, 38], [65, 72, 79, 86], [101, 112, 123, 134]]

    assert result == expected_result

if __name__ == "__main__":
    pytest.main()