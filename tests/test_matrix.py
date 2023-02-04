
def test_matrix_column():
   from mathhole._matrix import Matrix

   matrix = Matrix(2, [1,2,1,0])
   assert [1, 1] == list(matrix.get_col(0))

   assert [1, 2] == list(matrix.get_row(0))

   assert [2, 0] == list(matrix.get_col(1))
   assert [1, 0] == list(matrix.get_row(1))


   data = [
    90,	75,	 2,	50,	49,
    87,	84,	28,	67,	35,
    81,	67,	99,	28,	52,
    33,	52,	93,	53,	72,
    78,	40,	36,	23,	32,
   ]

   matrix = Matrix(5, data)
   assert [90, 87, 81, 33, 78] == list(matrix.get_col(0))
   assert data[0:5] == list(matrix.get_row(0))

   assert [75, 84, 67, 52, 40] == list(matrix.get_col(1))
   assert data[5:10] == list(matrix.get_row(1))

   assert [ 2, 28, 99, 93, 36] == list(matrix.get_col(2))
   assert data[10:15] == list(matrix.get_row(2))
   
   assert [ 50, 67, 28, 53, 23] == list(matrix.get_col(3))
   assert data[15:20] == list(matrix.get_row(3))
   
   assert [ 49, 35, 52, 72, 32] == list(matrix.get_col(4))
   assert data[20:] == list(matrix.get_row(4))


   data = [7, 8, 9, 10, 11, 12]
   matrix = Matrix(2, data)
   assert [7,8] == list(matrix.get_row(0))
   assert [9,10] == list(matrix.get_row(1))
   assert [11,12] == list(matrix.get_row(2))



def test_matrix_multi():
    from mathhole._matrix import Matrix
    
    matrix_a_data = [
        1, 2, 3,
        4, 5, 6
    ]

    matrix_b_data = [
        7, 8,
        9, 10,
        11, 12
    ]

    matrix_a = Matrix(3, matrix_a_data)
    matrix_b = Matrix(2, matrix_b_data)
    
    result = matrix_a * matrix_b

    assert result is not None

    assert result.column_count == 2
    assert result.row_count == 2
    assert [58, 64] == list(result.get_row(0))
    assert [139, 154] == list(result.get_row(1))


    matrix_b = Matrix(2, matrix_b_data)
    result = 2 * matrix_b
    assert result is not None
    assert [14, 16] == list(result.get_row(0))
    assert [18, 20] == list(result.get_row(1))
    assert [22, 24] == list(result.get_row(2))
