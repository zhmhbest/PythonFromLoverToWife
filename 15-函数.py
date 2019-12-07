"""
    函数参数演示
"""


def calc_2_num(x, y, fun):
    return fun(x, y)


if __name__ == '__main__':
    add = lambda x, y: x + y
    mul = lambda x, y: x * y

    print(calc_2_num(2, 4, add))
    print(calc_2_num(2, 4, mul))
    print(calc_2_num(2, 4, lambda x, y: x ** y))
