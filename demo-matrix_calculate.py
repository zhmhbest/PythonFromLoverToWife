"""
    线性代数，矩阵计算
    pip install pyperclip
"""
from com.zhmh.matrix import get_one_matrix
from com.zhmh.matrix import print_matrix_information, calculate_multiply_matrix


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


def do_calculate(text):
    import re
    terms = re.split('[*×]', text)
    if 1 == len(terms):
        # 一个矩阵打印信息
        print_matrix_information(get_one_matrix(terms[0])[1])
    else:
        calculate_multiply_matrix(terms)


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
    listen_clipboard(do_calculate)
