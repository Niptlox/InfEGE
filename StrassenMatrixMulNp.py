from itertools import product
import numpy as np


def matrix_to_2x2(matrix):
    return (list(map(lambda row: np.hsplit(row, 2), np.vsplit(matrix, 2))))


def strassen_mul_2x2(m1, m2):
    d = strassen_mul(m1[0][0] + m1[1][1], m2[0][0] + m2[1][1])
    d1 = strassen_mul(m1[0][1] - m1[1][1], m2[1][0] + m2[1][1])
    d2 = strassen_mul(m1[1][0] - m1[0][0], m2[0][0] + m2[0][1])

    h1 = strassen_mul(m1[1][1], m2[1][0] - m2[0][0])
    h2 = strassen_mul(m1[0][0], m2[0][1] - m2[1][1])
    v1 = strassen_mul(m1[0][0] + m1[0][1], m2[1][1])
    v2 = strassen_mul(m1[1][0] + m1[1][1], m2[0][0])

    return [[d + d1 + h1 - v1, h2 + v1],
            [h1 + v2, d + d2 + h2 - v2]]


def strassen_mul(mat1, mat2):
    if not mat1.shape:
        return mat1 * mat2

    if mat1.shape[0] == 2:
        return np.array(strassen_mul_2x2(mat1, mat2))
    print(mat1)
    print(mat2)
    return np.block(strassen_mul_2x2(matrix_to_2x2(mat1), matrix_to_2x2(mat2)))


def matrix_to_n2(mat1, mat2):
    rsize = max(len(mat1), len(mat2), len(mat1[0]), len(mat2[0]))
    i = 1
    while rsize > 2 ** i:
        i += 1
    nsize = 2 ** i
    nmat1 = to_size(mat1, nsize)
    nmat2 = to_size(mat2, nsize)
    return nmat1, nmat2


def to_size(mat, sz):
    nmat = []
    ow = sz - len(mat[0])
    for st in mat:
        nmat.append(st + [0] * ow)
    nmat += [[0] * sz] * (sz - len(mat))
    return np.array(nmat)


if __name__ == '__main__':
    mat1 = [[1, 0, 1], [2, 1, 1], [-1, 0, 1]]
    mat2 = [[1, 0], [-1, 2], [2, 1]]
    mat1, mat2 = matrix_to_n2(mat1, mat2)

    res = strassen_mul(mat1, mat2)
    print(res)
