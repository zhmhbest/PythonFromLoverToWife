"""
    函数参数演示
    lambda 表达式的存在是为了创建匿名函数
"""


def calc_2_num(x, y, fun):
    return fun(x, y)


def test_callback(x, y, callback):
    result = x + y
    callback(result)


if __name__ == '__main__':
    fun_add = lambda x, y: x + y
    fun_mul = lambda x, y: x * y

    # 函数参数演示
    print(calc_2_num(2, 4, fun_add))
    print(calc_2_num(2, 4, fun_mul))
    print(calc_2_num(2, 4, lambda x, y: x ** y))

    # 函数回调演示
    test_callback(3, 6, lambda val: print("3 + 6 =", val))

    # 匿名类
    obj = type("", (), {
        '__init__': lambda self, **kwargs: self.__dict__.update(kwargs),
        '__eq__': lambda self, other: self.__dict__ == other.__dict__,
    })(
        DEBUG=True,
        say=lambda: print("Hello"),
    )
    print(obj)
    print(obj.DEBUG)
    obj.say()
