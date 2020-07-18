# pip install sympy
from sympy import Matrix

A = Matrix([
    [8, -3, 6],
    [3, -2, 0],
    [-4, 2, -2]
])

if __name__ == '__main__':
    print("行列式：", A.det())
    print("特征多项式：", ' × '.join(
        [f'(λ-{k})^{e}' for k, e in A.eigenvals().items()]
    ))
    print("特征向量：", A.eigenvects())
    print("行阶梯矩阵：", A.rref())
