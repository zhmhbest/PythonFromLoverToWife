"""
    判断101-200之间有多少个素数，并输出所有素数
    用一个数分别去除2到根号下这个数，如果能被整除，则表明此数不是素数，反之是素数。
"""
from math import sqrt   # 开根号


def is_prime_number(num):
    """
    传入的数字是否为素数
    :param num:
    :return: True Or False
    """
    # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
    loop_top = int(sqrt(num + 1))
    for i in range(2, loop_top + 1):
        if 0 == num % i:
            return False
        # end if
    # end for
    return True
    # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑
    pass


if __name__ == '__main__':
    count = 0  # 总数统计
    for i in range(101, 201):
        if is_prime_number(i):
            count += 1
            print(i)
    # end for
    print("Total:", count)
