"""
    线性代数，矩阵计算
"""


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
        try:
            callback(str(_text))
        except Exception as e:
            print(e)
            print("矩阵表达式不正确！")
        # </do-sth>
        _recent = _text


def calculate_matrix(text: str) -> None:
    import re
    from sympy import Matrix

    # 获得矩阵Text
    inner_trim_text = re.sub('\\s*\\n\\s*', "|", text.strip())
    inner_trim_text = re.sub('\\s+', ",", inner_trim_text)
    # print(inner_trim_text)

    # 生成矩阵数组
    buffer_array = []
    buffer_string = []
    for row in inner_trim_text.split('|'):
        col = row.split(',')
        buffer_array.append(col)
        buffer_string.append('\t'.join(col))
    A = Matrix(buffer_array)

    # 计算
    show_split_double = '=' * 32
    show_split_single = '-' * 16
    show_matrix = '\n\t'.join(buffer_string)
    show_determinant = A.det()
    show_sup = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    show_sub = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
    show_polynomial = ' · '.join(
        [f'(λ-{k}){show_sup[e]}' for k, e in A.eigenvals().items()]
    )
    show_simplest = '\n\t\t'.join(
        ['\t'.join([str(col) for col in row]) for row in A.rref()[0].tolist()]
    )

    # 展示
    print(f"""
{show_split_double}
矩阵：
    {show_matrix}
    {show_split_single}
    行列式：{show_determinant}
    特征多项式：{show_polynomial}
    最简行阶梯：
        {show_simplest}
    """.strip())


if __name__ == '__main__':
    """
    测试数据，复制到剪切板
    8  -3  6
    3  -2  0
    -4  2  -2
    """
    listen_clipboard(calculate_matrix)