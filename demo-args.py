"""
    *args、**kwargs

    在Python中的代码中经常会见到这两个词 args 和 kwargs，前面通常还会加上一个或者两个星号。
    其实这只是编程人员约定的变量名字
        args 是 arguments 的缩写，表示位置参数；
        kwargs 是 keyword arguments 的缩写，表示关键字参数。
    这其实就是 Python 中可变参数的两种形式，并且 *args 必须放在 **kwargs 的前面，因为位置参数在关键字参数的前面。
"""


def test_args(first, *args):
    print("[必填参数] first =", first)
    print("[位置可选] args =", type(args), args)


def test_kwargs(first, *args, **kwargs):
    print("[必填参数] first =", first)
    print("[位置可选] args =", type(args), args)
    print("[实名可选] kwargs =", type(kwargs), kwargs)


if __name__ == '__main__':
    test_args(0)
    print()

    test_args(1, 2, 3, 4)
    print()

    test_kwargs(0)
    print()

    # 错误使用，第一个参数已指定名称，无法自定义
    # test_kwargs(k0=1)

    test_kwargs(0, k1=1)
    print()

    test_kwargs(1, 2, 3, 4, k1=5, k2=6)
    print()

    # **将字典展开为参数
    params = {'a': 11, 'b': 12, 'c': 13}
    test_kwargs(0, **params)
