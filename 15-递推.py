"""
    已知a_(n+1) = a_(n) * 2 + 1/a_(n)
    a_(0) = 1
    a_(1) = 3
    a_(2) = 6 + 1/3
    求a_(123)
"""


def get_an(n, a_0, recursion):
    """
    获取递推公式第n项的值
    :param n: 第几项
    :param a_0: a(0)的值
    :param recursion: 递推表达式
    :return: 结果
    """
    a_n = a_0
    for i in range(n):
        a_n = recursion(a_n)
    # end for
    return a_n


if __name__ == '__main__':
    result = get_an(123, 1, lambda a: a * 2 + 1 / a)
    print(result)
