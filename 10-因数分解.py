"""
    因数分解1~200的数字
"""


def factorization_way1(num):
    """
    因数分解
    :param num:
    :return: List
    """
    result = []
    if 1 == num:
        result.append(num)
        return result
    # end if

    # 分解
    k = 2  # 从最小的素数开始
    while 1 != num:
        if 0 == num % k:
            result.append(k)
            num //= k
        else:
            k += 1
        # end if
    # end while
    return result


if __name__ == '__main__':
    for i in range(1, 200):
        print(i, factorization_way1(i))
    # end for(i)

