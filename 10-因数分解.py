"""
    因数分解1~200的数字
    要求：实现一个函数，获得参数为数字，返回结果为存于列表中的分解结果。
    因数分解方法：
        从最小的素数（k=2）开始尝试
            如果不能被整除：k=k+1，继续尝试；
            如果能被整除，当前数变为除以k的商；
            当前数字为1时即表示分解完毕。
    注意：如果输入的数字为1应立即返回

"""


def factorization(num):
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
        print(i, factorization(i))
    # end for(i)

