def transposeMatrix(matrix):
    print(matrix)
    output = [[None] * len(matrix)] * len(matrix[0])
    print(output)
    for col in range(len(matrix[0])):
        print(f"For col {col}")
        for row in range(len(matrix)):
            print(f"for row {row}")
            output[col][row] = matrix[row][col]
            print(output)
    return output


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(transposeMatrix(matrix))
