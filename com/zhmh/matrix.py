"""
    https://www.bilibili.com/read/cv6445679/
    https://zhuanlan.zhihu.com/p/111573239
"""
import sympy
# Rational 分数
# abc 引入符号
# import numpy as np
import re
CONSTANT_SUP_NUMBER = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
CONSTANT_SUB_NUMBER = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']


def get_arr_matrix(text: str):
    """
    从文本中获取一个二维数组
    :param text:
    :return:
    """
    _rs = re.split(
        re.compile('[ \\t]*[\\n\\r]\\s*'),      # 去除空行、空白行
        re.sub('[ \\t]+', ' ', text.strip())    # 连续空格
    )
    return [(_r.split(' ')) for _r in _rs]


def get_one_matrix(text: str):
    """
    从文本中获取一个矩阵
    """
    try:
        _a = get_arr_matrix(text)
        _m = sympy.Matrix(_a)
        return _a, _m
    except Exception as e:
        print("矩阵表达式错误（get_one_matrix）", e)
        return None, None


def packing_list(_l, margin_left=1, pre_line=1):
    _margin = '\t' * margin_left
    _heading = '\n' * pre_line
    return _heading + _margin + f'\n{_margin}'.join(_l)


def str_arr_matrix(_a, margin_left=1, pre_line=0):
    return packing_list(
        ['\t'.join(_r) for _r in _a],
        margin_left, pre_line)


def str_one_matrix(_m: sympy.Matrix, margin_left=2, pre_line=1):
    return packing_list(
        ['\t'.join([str(col) for col in row]) for row in _m.tolist()],
        margin_left, pre_line)


def get_nn_matrix_information(_m: sympy.Matrix):
    """
    获得n×n的矩阵信息
    :return:
    """
    show_jordan = _m.jordan_form()[1]
    return {
        'det': _m.det(),
        'trace': _m.trace(),
        'inv': _m.inv(),
        'pol': ' · '.join(
            [f'(λ - ({k})){CONSTANT_SUP_NUMBER[e]}' for k, e in _m.eigenvals().items()]
        ),
        'vec': [f'λ = {v[0]}, ξ = {str([i[0] for i in v[2][0].tolist()])}ᵀ' for v in _m.eigenvects()],
        'jordan': show_jordan
    }


def print_matrix_information(_m: sympy.Matrix):
    from sympy import oo
    constant_split_double = '=' * 32
    constant_split_single = '-' * 16
    if _m is None:
        return

    show_n_row, show_n_col = _m.shape
    try:
        # 最简式
        show_simplest = _m.rref()[0]
    except Exception as e:
        print("矩阵表达式错误（print_matrix_information）", e)
        return

    print(constant_split_double)
    print(f"矩阵：A = {str_one_matrix(_m, 1)}")
    print(f"    {constant_split_single}")
    print(f"    形状    \t: {'n' if show_n_row == show_n_col else 'm'}×n = {show_n_row}×{show_n_col}")
    print(f"    秩      \t: {_m.rank()}")
    print(f"    列(1)范数\t: {_m.norm(1)}")
    print(f"    行(∞)范数\t: {_m.norm(oo)}")
    print(f"    最简     \t: {str_one_matrix(show_simplest)}")
    if show_n_row == show_n_col:
        print(f"    {constant_split_single}")
        show_nn = get_nn_matrix_information(_m)
        print(f"    迹       \t：{show_nn['trace']}")
        print(f"    行列式    \t：|A| = {show_nn['det']}")
        print(f"    特征多项式\t：|λE - A| = {show_nn['pol']}")
        print(f"    特征向量  \t：Aξ = λξ{packing_list(show_nn['vec'], 2)}")
        print(f"    逆矩阵    \t：{str_one_matrix(show_nn['inv'])}")
        print(f"    Jordan   \t：{str_one_matrix(show_nn['jordan'])}")


def calculate_multiply_matrix(terms):
    """
    计算多个矩阵相乘
    :param terms:
    :return:
    """
    constant_split_double = '=' * 32
    constant_split_single = '-' * 16
    try:
        buffer = []
        for term in terms:
            term = term.strip()
            if term.find(' ') > -1:
                _a, _m = get_one_matrix(term)
                buffer.append(_m)
            else:
                _fraction = term.split('/')
                if 2 == len(_fraction):
                    buffer.append(sympy.Rational(_fraction[0], _fraction[1]))
                else:
                    buffer.append(int(_fraction[0]))

        # 开始计算
        result = 1
        print()
        print(constant_split_double)

        for _m in buffer:
            if 1 != result:
                print('×')
            if isinstance(_m, sympy.MutableDenseMatrix):
                print(str_one_matrix(_m, 1, 0))
            else:
                print(f'\t{_m}')
            result = result * _m
        print('=')
        print(str_one_matrix(result, 1, 0))
    except Exception as e:
        print("计算时发生异常(calculate_multiply_matrix)", e)
