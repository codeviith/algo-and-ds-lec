from matrix import print_mat

### matrix transpose is defined as turning the rows of a matrix into columns

# Examples:
###1 
# [[0]] == [[0]]

###2
# [[0,1]] == [
#     [0],
#     [1]
# ]


def transpose(mat):
    """Should transpose matrix m"""
    result = []
    N = len(mat)
    M = len([0])

    for j in range(M):
        row = []

        for i in range(N):
#           print(i, j, '====', mat[i][j])  ### 0 0 ==== 1
                                            ### 1 0 ==== 4
                                            ### 2 0 ==== 7
                                            ### 0 1 ==== 2
                                            ### 1 1 ==== 5
                                            ### 2 1 ==== 8
                                            ### 0 2 ==== 3
                                            ### 1 2 ==== 6
                                            ### 2 2 ==== 9
            row.append(mat[i][j])
        result.append(row)
    
    print_mat(result)
    return result


### Another approach...but only works for number sequence:
def transpose(mat):
    """Should transpose matrix m"""
    result = []
    N = len(mat)
    M = len(mat[0])

    for val in mat[0]:
        row = []
        for x in range(N):
            row.append((val + (M * x)) % 10)
        result.append(row)

    print_mat(result)
    return result



if __name__ == '__main__':
    input_m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]
    assert transpose(input_m) == expected
