"""
    排列组合
"""


def get_factorial(n):
    """
    返回n的阶乘
    :param n:
    :return:
    """
    if n < 0:
        return -1
    # end if
    ret = 1
    for _i_ in range(2, n + 1):
        ret *= _i_
    return ret


def get_permutation_num(n, m):
    """
    排列数
    A_(n)^(m) = n! / (n-m)!
    :param n:
    :param m:
    :return: [分子, 分母]
    """
    return [
        get_factorial(n),
        get_factorial(n - m)
    ]


def get_combination_num(n, m):
    """
    组合数
    C_(n)^(m) = n! / [ m! · (n-m)! ]
    :param n:
    :param m:
    :return:
    """
    return [
        get_factorial(n),
        get_factorial(m) * get_factorial(n - m)
    ]


if __name__ == '__main__':
    """
        有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？
        各是多少？
        用Python编写程序并print所有的情况。
    """
    # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    print(i * 100 + j * 10 + k)
                # end if
            # end for(k)
        # end for(j)
    # end for(i)
    # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑
