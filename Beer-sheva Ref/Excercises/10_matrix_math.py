from typing import List


class DimensionError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Matrix:
    def __init__(self, elements: List[list]):
        """
        :param  elements: a list of lists. Each sublist holds a matrix row
        """
        for i in range(1, len(elements)):
            if len(elements[i]) != len(elements[i-1]):
                raise DimensionError('Matrix must be a rectangular array')
        self.values = elements  # type: List[list]
        self.dimensions = len(elements), len(elements[0])

    def __repr__(self):
        st = '['
        for row in self.values:
            st += str(row) + '\n'
        return st[:-1] + ']'

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('can only multiply matrices')
        if self.dimensions[1] != other.dimensions[0]:
            raise DimensionError('incompatible dimensions for multiplication')

        # traditional implementation
        #res = [[0] * other.dimensions[1]] * other.dimensions[0]
        #for i in range(self.dimensions[0]):
        #    for j in range(other.dimensions[1]):
        #        for k in range(self.dimensions[1]):
        #            res[i][j] += self.values[i][k] * other.values[k][j]
        #return Matrix(res)
        # elegant implementation
        return Matrix([[sum(_a * _b for _a, _b in zip(self_row, other_col)) for other_col in zip(*other.values)]
                      for self_row in self.values])

    def transpose(self):
        self.values = [[self.values[j][i] for j in range(self.dimensions[0])] for i in range(self.dimensions[1])]
        self.dimensions = self.dimensions[1], self.dimensions[0]
        return Matrix(self.values)


class Vector(Matrix):
    def __init__(self, elements: List):
        if len(elements[0]) == 1:  # column vector
            super().__init__(elements)  # super() refers to parent class
            return
        if len(elements) == 1:  # row vector
            super().__init__(elements)
            return
        raise DimensionError("This isn't a vector")

    def dot_product(self, other):
        if not isinstance(other, Vector):
            raise TypeError('can only dot product vectors')
        # Q: why am I creating a copy?
        # A: Don't want to change the vector. Remember the mutability of lists
        if self.dimensions[0] > 1:  # if column vector transpose
            _a = Matrix(self.values).transpose()
        else:
            _a = self
        if other.dimensions[0] == 1:  # if row vector transpose
            _b = Matrix(other.values).transpose()
        else:
            _b = other
        return (_a @ _b).values[0][0]


if __name__ == '__main__':
    print('a:')
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    print(a)
    print('***************')
    print('a transpose:')
    a.transpose()
    print(a)

    a.transpose()
    b = Matrix([[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0]])
    print('b:')
    print(b)
    print('***************')
    print('a*b:')
    print(a@b)

    # dot product
    print('***************')
    print("x:")
    x = Vector([[1, 2, 3]])
    print(x)
    y = Vector([[4, 5, 6]])
    print("y:\n", y)
    print("dot product:")
    y = Vector([[4, 5, 6]])
    print(x.dot_product(y))
    # z = Vector([[4, 5, 6, 7]])
    # print(x.dot_product(z))