"""
    输出100~5000的所有回文数
    回文数：高低位对称的数字
    eg: 12321, 1221, 988523325889
"""


def fractured_number(num, weight=10):
    result = []
    while num != 0:
        result.append(num % weight)
        num = num // weight
    # end while
    return result


def is_palindrome(num):
    num_arr = fractured_number(num)
    num_len = len(num_arr)
    for i in range(int(num_len / 2)):  # 长度为奇数时，中间的数没有判断的必要
        if num_arr[i] != num_arr[num_len - i - 1]:
            return False
        # end if
    # end for
    return True


if __name__ == '__main__':
    for i in range(100, 50001):
        if is_palindrome(i):
            print(i)

