"""
    打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
"""


def is_narcissus(num):
    """
    是否是水仙花数
    :param num:
    :return: True Or False
    """
    # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
    n = num
    fractured_num = [None, None, None]
    fractured_num[0] = n // 100
    n %= 100
    fractured_num[1] = n // 10
    n %= 10
    fractured_num[2] = n
    # 获得打碎后的数字
    if num == (fractured_num[0] ** 3 + fractured_num[1] ** 3 + fractured_num[2] ** 3):
        return True
    else:
        return False
    # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑


if __name__ == '__main__':
    for i in range(100, 1000):
        if is_narcissus(i):
            print(i)


