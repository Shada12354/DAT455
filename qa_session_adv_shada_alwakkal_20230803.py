""""
QA-session Beginner (Adv) 2023-08-03
@author Shada Al-Wakkal, GitHub: Shada12354
"""
from numpy import*

X = array([[1,2,3], [4,5,6], [7,8,9]])
Y = array([[10,11],[12,13], [14,15]])
Z = array ([[16,17,18], [19,20,21]])

print("X:",X)
print("Y:",Y)
print("Z:", Z)

X_POWER = linalg.matrix_power(X, 2)
Y_TIMES_Z = dot(Y,Z)

print("X squared:",X_POWER)
print("Y_TIMES_Z:", Y_TIMES_Z)


def laplace_determinant(matrix):
    if matrix.shape == (1,1):
        return matrix[0,0]

    det = 0
    for i in range(matrix.shape[1]):
        minor = delete(matrix,0,axis=0)
        minor = delete(minor, i, axis=1)
        det += (-1) ** i * matrix[0,1] * laplace_determinant(minor)

    return det

W = array([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]])
print("W:", W)

det_W = laplace_determinant(W)
print("Determinant of W:", det_W)

M = array([[5.9, 10.3, 111.0, 7.1010], [1.0001, 102.2020, 2.2023, 09.00], [8.03, 03.0820, 03.082023, 10.0], [1, 99, 0, 7]])
print("M:", M)
M_formatted = "\n".join(["\t".join(["{:.2f}".format(cell) for cell in row]) for row in M])
print("M:", M_formatted)
"""

N = array([[1,2,3], [4,5,6],[7,8,9]])
"""
U,S,Vt  = linalg.svd(N)

print("N:",N)
print("U values SVD:", U)
print("S:", S)
print("Vt:", Vt)


def advanced_svd(matrix, reduced=False, tol=1e-10):
    U, S, Vt = linalg.svd(matrix, full_matrices= not reduced)

    if reduced:
        num_singular_values = sum(S > tol)
        U = U[:, :num_singular_values]
        S = S[:num_singular_values]
        Vt = Vt[:num_singular_values, :]

    return U, S, Vt

U, S, Vt = advanced_svd(N, reduced=False)

print("N:", N)
print("U:", U)
print("Vt:", Vt)
