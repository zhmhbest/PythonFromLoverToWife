"""
    装饰器
"""


def demo1(demo_name):
    def wrapper(fun):
        print(demo_name, "wrapper")
        fun()
    # end def

    @wrapper
    def test():
        print(demo_name, "test")
    # end def

    test  # 调用test方法，此处不能加()。
# end def(demo)


def demo2(demo_name):
    def wrapper(func):
        def callback(*args, **kwargs):
            print(demo_name, "callback")
            return func(*args, **kwargs)
        return callback
    # end def

    @wrapper
    def test(item):
        print(demo_name, "test", item)
    # end def

    test("Hello")  # 调用test方法
# end def(demo)


def demo3(demo_name):
    def decorate(tip):
        def wrapper(func):
            def callback(*args, **kwargs):
                print(demo_name, tip)
                return func(*args, **kwargs)
            return callback
        return wrapper
    # end def(decorate)

    @decorate("Something")
    def test(item):
        print(demo_name, "test", item)
    # end def

    test("Hello")  # 调用test方法
# end def(demo)


def demo4(demo_name):
    class Decorate:
        def __init__(self, func):
            self.func = func

        def __call__(self):
            print(demo_name, "Class decorator")
            self.func()

    @Decorate
    def test():
        print(demo_name, "test")

    test()


def demo5(demo_name):
    class Decorate:
        def __init__(self, tip):
            self.tip = tip

        def __call__(self, func):
            def wrapper(*args, **kwargs):
                print(self.tip)
                return func(*args, **kwargs)
            return wrapper

    @Decorate("Something")
    def test(item):
        print(demo_name, "test", item)

    test("Hello")


if __name__ == '__main__':
    demo1("demo1")
    print()

    # 被装饰函数传参
    demo2("demo2")
    print()

    # 装饰器传参
    demo3("demo3")
    print()

    # 类装饰器
    demo4("demo4")
    print()

    # 类装饰器
    demo5("demo5")
    print()
