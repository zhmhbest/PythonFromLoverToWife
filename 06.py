"""
    判断101-200之间有多少个素数，并输出所有素数
    用一个数分别去除2到根号下这个数，如果能被整除，则表明此数不是素数，反之是素数。
"""


def is_prime_number(num):
    """
    传入的数字是否为素数
    :param num:
    :return: True Or False
    """
    # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
    return True
    # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑
    pass


if __name__ == '__main__':
    for i in range(101, 201):
        if is_prime_number(i):
            print(i)
