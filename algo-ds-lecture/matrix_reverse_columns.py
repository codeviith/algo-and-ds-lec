
def reverse_cols(mat):
    """Should reverse the order of the columns for matrix m"""
    pass


if __name__ == '__main__':
    input_m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ]
    assert reverse_cols(input_m) == expected
    