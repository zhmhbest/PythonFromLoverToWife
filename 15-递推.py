"""
    已知a_(n+1) = a_(n) * 2 + 1/a_(n)
    a_(0) = 1
    a_(1) = 3
    a_(2) = 6 + 1/3
    求a_(123)
"""


def get_an(n, a0, fun):
    """
    获取递推公式第n项的值
    :param n: 第几项
    :param a0: a(0)的值
    :param fun: 递推表达式
    :return: 结果
    """
    a_n = a0
    for i in range(1, n + 1):
        a_n = fun(a_n)
    # end for
    return a_n


if __name__ == '__main__':
    result = get_an(123, 1, lambda n: n * 2 + 1 / n)
    print(result)
