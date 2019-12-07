"""
    字符串逆序
    实现一个函数，传入一个字符串，返回字符串的逆序
    eg:
        input: abc123
        output: 321cba
"""


def str_reverse_way1(input_str):
    return input_str[::-1]


def str_reverse_way2(input_str):
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
    str_list[0] = 15
    return


if __name__ == '__main__':
    test_str = "abc123"
    print(str_reverse_way1(test_str))
    print(str_reverse_way2(test_str))
    print(str_reverse_way3(test_str))
    print(str_reverse_way4(test_str))
    print(str_reverse_way5(test_str))
