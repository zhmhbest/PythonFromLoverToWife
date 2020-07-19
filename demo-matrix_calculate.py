"""
    线性代数，矩阵计算
    pip install pyperclip
"""
import sympy
consent_split_double = '=' * 32
consent_split_single = '-' * 16


def listen_clipboard(callback, speed=0.5):
    """
    实时监测剪切板
    """
    import pyperclip
    import time
    _recent = None
    while True:
        time.sleep(speed)
        _text = pyperclip.paste()
        if _text == _recent:
            continue
        # <do-sth>
        callback(str(_text))
        # </do-sth>
        _recent = _text


def get_arr_matrix(text: str):
    """
    从文本中获取一个矩阵
    """
    import re
    _rs = re.split(
        re.compile('[ \\t]*[\\n\\r]\\s*'),      # 去除空行、空白行
        re.sub('[ \\t]+', ' ', text.strip())    # 连续空格
    )
    return [(_r.split(' ')) for _r in _rs]


def get_one_matrix(_m: [list]):
    """
    从数组生成一个矩阵对象
    """
    # from sympy import SympifyError
    try:
        _A = sympy.Matrix(_m)
    except Exception as e:
        print("矩阵表达式错误（生成）", _m)
        return None
    return _A


def str_arr_matrix(_m: [list], margin_left=1):
    _margin = '\t' * margin_left
    return _margin + f'\n{_margin}'.join(['\t'.join(_r) for _r in _m])


def str_one_matrix(_sm: sympy.Matrix, margin_left=2, pre_line=1):
    _margin = '\t' * margin_left
    return ('\n' * pre_line) + _margin + f'\n{_margin}'.join(
        ['\t'.join([str(col) for col in row]) for row in _sm.tolist()]
    )


def print_matrix_message(_m: [list]) -> None:
    # 常量
    consent_sup = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    consent_sub = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']

    _A = get_one_matrix(_m)
    if _A is None:
        return

    try:
        show_n_row, show_n_col = _A.shape
        show_simplest = _A.rref()[0]    # 最简式

        # n×n的情况
        # from sympy import NonSquareMatrixError  # TypeError
        show_determinant = None
        show_polynomial = None
        show_vector = None
        show_inverse = None
        if show_n_row == show_n_col:
            show_determinant = _A.det()     # 行列式
            show_polynomial = ' · '.join(
                [f'(λ - ({k})){consent_sup[e]}' for k, e in _A.eigenvals().items()]
            )   # 特征多项式
            show_vector = '\n\t\t' + '\n\t\t'.join(
                [f'λ = {v[0]}, ξ = {str([i[0] for i in v[2][0].tolist()])}ᵀ' for v in _A.eigenvects()]
            )   # 特征向量
            show_inverse = _A ** -1
    except:
        print("矩阵表达式错误（计算）")
        return

    # 展示
    print(consent_split_double)
    print(f"""矩阵：A = \n{str_arr_matrix(_m)}
    {consent_split_single}
    形状      \t： {'n' if show_n_row == show_n_col else 'm'}×n = {show_n_row}×{show_n_col}
    最简行阶梯 \t：{str_one_matrix(show_simplest)}""")

    if show_n_row == show_n_col:
        print(f"    {consent_split_single}")
        print(f"    行列式    \t：|A| = {show_determinant}")
        print(f"    特征多项式\t：|λE - A| = {show_polynomial}")
        print(f"    特征向量  \t：Aξ = λξ{show_vector}")
        print(f"    逆矩阵    \t：{str_one_matrix(show_inverse)}")


def calculate_matrix(text: str) -> None:
    import re
    _ts = re.split('[*×]', text)
    if 1 == len(_ts):
        # 一个矩阵打印信息
        print_matrix_message(get_arr_matrix(_ts[0]))
    else:
        # 矩阵乘法计算
        try:
            buffer_sm = []
            for _t in _ts:
                _m = get_arr_matrix(_t)
                # print(_m)
                _sm = get_one_matrix(_m)
                if _sm is None:
                    return
                buffer_sm.append(_sm)
            # 开始计算
            result = 1
            print()
            print(consent_split_double)
            for _a in buffer_sm:
                if 1 != result:
                    print('×')
                print(str_one_matrix(_a, 1, 0))
                result = result * _a
            print('=')
            print(str_one_matrix(result, 1, 0))
        except:
            print("矩阵不对称")


if __name__ == '__main__':
    """
    测试数据，复制到剪切板
    ----------------
    8  -3   6
    3  -2   0 
    -4  2   -2
    ----------------
    2   0   2
    1   5   -1
    1   3   3
    ----------------
    2   3   1   -3  -7
    1   2   0   -2  -4 
    3   -2  8   3   0
    2   -3  7   4   3
    ----------------
    1	0	0
    -1	1	0
    2	3	1
        *
    2	0	0
    0	1	0
    0	0	3
        =
    2   0   0
    -2  1   0
    4   3   3
    ----------------
    
"""
    listen_clipboard(calculate_matrix)
