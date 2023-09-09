#!/usr/bin/python3
def matrix_mul(m_a, m_b):

    # Validate m_a

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a[:-1]):
    raise TypeError("m_a should contain only integers or floats")


if not all(isinstance(num, (int, float)) for num in m_a[-1]):
    raise TypeError("m_a should contain only integers or floats")

    # Validate m_b

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    if any(not all(lambda num: isinstance(num, (int, float)), row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    # Calculate the product of the matrices

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(elem)
        result.append(row)

    return result
