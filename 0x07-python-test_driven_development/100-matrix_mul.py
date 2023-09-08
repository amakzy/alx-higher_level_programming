def matrix_mul(m_a, m_b):

    # Validate input
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError('m_a and m_b must be lists')
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_a and m_b must be lists of lists')

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError('m_a and m_b can\'t be empty')

    if not all(all(isinstance(ele, (int, float)) for ele in row) for row in m_a) or not all(all(isinstance(ele, (int, float)) for ele in row) for row in m_b):
        raise TypeError('m_a and m_b must contain only integers or floats')

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_a and m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    # Matrix multiplication
    result = [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
