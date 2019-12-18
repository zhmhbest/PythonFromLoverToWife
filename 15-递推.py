# coding=utf-8
"""
    递推
"""


def get_an(n, a0, recursion, return_sn=False):
    """
    获取递推公式第n项的值
    :param n: 第几项
    :param a0: a(0)的值
    :param recursion: 递推表达式
    :param return_sn: 是否返回前n项的和
    :return: 结果, 前n项和
    """
    sn = a0
    an = a0
    for i in range(n):
        an = recursion(an)
        sn += an
    # end for
    if return_sn:
        return an, sn
    else:
        return an
    # end if


if __name__ == '__main__':
    """
        已知a_(n+1) = a_(n) * 2 + 1/a_(n)
        a_(0) = 1
        a_(1) = 3
        a_(2) = 6 + 1/3
        求a_(123)
    """
    a_123 = get_an(123, 1, lambda a: a * 2 + 1 / a)
    print("a(123)=%e" % a_123)

    """
        一球从100米高度自由落下，每次落地后反跳回原高度的一半；
        再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
    """
    a_0 = 100
    a_10, s_10 = get_an(10, a_0, lambda a: a / 2, True)
    height = (s_10 - a_10) * 2 - a_0
    print("第10次高度：%f\n第10次落地时共经过%f米" % (a_10, height))

    """
        猴子吃桃问题
        猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，
        又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
        到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
    """
    start_peach = get_an(9, 1, lambda a: (a + 1) * 2)
    print("第一天摘了%d个桃子" % start_peach)

