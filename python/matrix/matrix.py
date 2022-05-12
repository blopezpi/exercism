from typing import List


class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(element) for element in row.split()]
                       for row in matrix_string.splitlines()]

    def row(self, index) -> List[int]:
        if len(self.matrix) < index:
            raise IndexError("Index row out of range")

        return self.matrix[index-1]

    def column(self, index) -> List[int]:
        if len(self.matrix[0]) < index:
            raise IndexError("Index column out of range")

        return [row[index-1] for row in self.matrix]


matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
matrix.column(1)[2] = 5
print(matrix.column(3))
matrix.row(1)[0] = 5
print(matrix.row(1))
