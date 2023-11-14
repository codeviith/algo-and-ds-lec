### always a square

# time == O(n^2)
# space == O(n^2)
def mat_identity(n):
    """should return an n * n identity matrix"""

    mat = []

    ###
    for i in range(n):
        mat.append([])
        
        for j in range(n):
            mat[i].append(0)

    ###
    # time: O(n^2)
    # space: O(n^2)
    mat = []
    for i in range(n):
        row = []
        
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        mat.append(row)
    
    # for x in range(n):
    #     mat[x][x] = 1

    return mat


if __name__ == '__main__':
    expected = [
        [1, 0],
        [0, 1]
    ]
    assert mat_identity(2) == expected

    expected = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    assert mat_identity(3) == expected
