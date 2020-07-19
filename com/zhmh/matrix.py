"""
    https://www.bilibili.com/read/cv6445679/
"""
import sympy
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
    return {
        'det': _m.det(),
        'inv': _m.inv(),
        'pol': ' · '.join(
            [f'(λ - ({k})){CONSTANT_SUP_NUMBER[e]}' for k, e in _m.eigenvals().items()]
        ),
        'vec': [f'λ = {v[0]}, ξ = {str([i[0] for i in v[2][0].tolist()])}ᵀ' for v in _m.eigenvects()]
    }


def print_matrix_information(_m: sympy.Matrix):
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
    print(f"    形状: {'n' if show_n_row == show_n_col else 'm'}×n = {show_n_row}×{show_n_col}")
    print(f"    最简: {str_one_matrix(show_simplest)}")
    if show_n_row == show_n_col:
        print(f"    {constant_split_single}")
        show_nn = get_nn_matrix_information(_m)
        print(f"    行列式    \t：|A| = {show_nn['det']}")
        print(f"    特征多项式\t：|λE - A| = {show_nn['pol']}")
        print(f"    特征向量  \t：Aξ = λξ{packing_list(show_nn['vec'], 2)}")
        print(f"    逆矩阵    \t：{str_one_matrix(show_nn['inv'])}")


def calculate_matrix():
    pass
    # else:
    #     # 矩阵乘法计算
    #     try:
    #         buffer = []
    #         for _t in _ts:
    #             _t = _t.strip()
    #             if _t.find(' ') > -1:
    #                 _m = get_arr_matrix(_t)
    #                 _sm = get_one_matrix(_m)
    #                 if _sm is None:
    #                     return
    #                 buffer.append(_sm)
    #             else:
    #                 buffer.append(_t)
    #
    #         # 开始计算
    #         result = 1
    #         print()
    #         print(consent_split_double)
    #
    #         for _a in buffer:
    #             if 1 != result:
    #                 print('×')
    #
    #             if isinstance(_a, str):
    #                 print(f'\t{_a}')
    #                 result = result * float(_a)
    #             else:
    #                 print(str_one_matrix(_a, 1, 0))
    #                 result = result * sympy.eye()
    #
    #         print('=')
    #         print(str_one_matrix(result, 1, 0))
    #     except NameError as e:
    #         print("矩阵不对称", e)
