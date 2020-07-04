"""
    打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
"""


def is_narcissus_way1(num):
    """
    是否是水仙花数 方法1 - 高位在前
    :param num:
    :return: True Or False
    """
    n = num
    fractured_num = [None, None, None]
    fractured_num[0] = n // 100
    n %= 100
    fractured_num[1] = n // 10
    n %= 10
    fractured_num[2] = n
    # ↑↑↑获得打碎后的数字↑↑↑
    if num == (fractured_num[0] ** 3 + fractured_num[1] ** 3 + fractured_num[2] ** 3):
        return True
    else:
        return False
    # end if


def is_narcissus_way2(num):
    """
    是否是水仙花数 方法2 - 低位在前（该方法更具有普适性）
    :param num:
    :return: True Or False
    """
    n = num
    fractured_num = []
    while n != 0:
        fractured_num.append(n % 10)
        n = n // 10
    # end while
    # ↑↑↑获得打碎后的数字↑↑↑
    if num == (fractured_num[0] ** 3 + fractured_num[1] ** 3 + fractured_num[2] ** 3):
        return True
    else:
        return False
    # end if


def is_narcissus_way3(num):
    """
    是否是水仙花数 方法3 - 字符串法
    :param num:
    :return: True Or False
    """
    str_num = str(num)  # 转换为字符串
    fractured_num = []
    for ch in str_num:
        # 每次获得一个字符，再转化为数字放入列表。
        fractured_num.append(int(ch))
    # end for
    # ↑↑↑获得打碎后的数字↑↑↑
    if num == (fractured_num[0] ** 3 + fractured_num[1] ** 3 + fractured_num[2] ** 3):
        return True
    else:
        return False
    # end if


if __name__ == '__main__':
    print("方法1：")
    for i in range(100, 1000):
        if is_narcissus_way1(i):
            print(i)
        # end if
    # end for
    
    print()  # 换行

    print("方法2：")
    for i in range(100, 1000):
        if is_narcissus_way2(i):
            print(i)
        # end if
    # end for

    print()  # 换行

    print("方法3：")
    for i in range(100, 1000):
        if is_narcissus_way3(i):
            print(i)
        # end if
    # end for

