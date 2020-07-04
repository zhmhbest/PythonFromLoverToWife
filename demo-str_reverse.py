"""
    字符串逆序
"""


def str_reverse_way1(input_str):
    """
    • [:]               提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串。
    • [start:]          从start 提取到结尾。
    • [:end]            从开头提取到end - 1。
    • [start:end]       从start 提取到end - 1。
    • [start:end:step]  从start 提取到end - 1，每step 个字符提取一个。
    """
    return input_str[::-1]


def str_reverse_way2(input_str):
    """
    字符串.join(列表)    以“字符串”将“列表”连接成字符串
    eg:
        l1 = [1, 2, 3]
        '#@#'.join(l1)
        # 结果: 1#@#2#@#3
    """
    temp_list = []
    for i in input_str:
        temp_list.append(i)
    # end for
    temp_list.reverse()
    return ''.join(temp_list)


def str_reverse_way3(input_str):
    result = ''
    for ch in reversed(input_str):
        result += ch
    # end for
    return result


def str_reverse_way4(input_str):
    result = ''
    for i in range(len(input_str) - 1, -1, -1):
        ch = input_str[i: i+1]  # 取第i个字符
        result += ch
    return result


def str_reverse_way5(input_str):
    str_list = [i for i in input_str]
    i = 0
    j = len(str_list) - 1
    while i < j:
        str_list[i], str_list[j] = str_list[j], str_list[i]
        i += 1
        j -= 1
    # end while
    result = ''
    for ch in str_list:
        result += ch
    # end for
    return result


if __name__ == '__main__':
    test_str = "abc123"
    print(str_reverse_way1(test_str))
    print(str_reverse_way2(test_str))
    print(str_reverse_way3(test_str))
    print(str_reverse_way4(test_str))
    print(str_reverse_way5(test_str))
