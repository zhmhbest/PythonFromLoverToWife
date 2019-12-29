"""
    序列生成器（generator object）
"""


def demo1(demo_name):
    seq = range(3)
    print(demo_name, type(seq), seq)
    for i in seq:
        print(demo_name, "for in", i)


def demo2(demo_name):
    seq = (x*x for x in range(3))
    print(demo_name, type(seq), seq)
    for i in seq:
        print(demo_name, "for in", i)


def demo3(demo_name):
    def sequence_generator(num):
        """
        带有 yield 的函数在 Python 中被称之为 generator（生成器）
        执行到yield时：
            返回yield后的值
            暂停并跳出当前函数
            下次再调用函数会继续执行
        :param num:
        :return:
        """
        for _i_ in range(num):
            yield 2 * _i_
    # end def

    seq = sequence_generator(3)
    print(demo_name, type(seq), seq)
    print(demo_name, next(seq))
    print(demo_name, next(seq))
    print(demo_name, next(seq))
    try:
        print(demo_name, next(seq))
    except StopIteration:
        print("序列溢出")
    # end try

    for i in sequence_generator(5):
        print(demo_name, "for in", i)


def demo4(demo_name):
    class SequenceGenerator:
        def __init__(self, n):
            self.index = 0
            self.num = n

        def __iter__(self):
            return self

        def __next__(self):
            if self.index <= self.num:
                r = self.index
                self.index += 1
                return r * 2
            else:
                raise StopIteration
    # end class
    for i in SequenceGenerator(3):
        print(demo_name, "for in", i)


if __name__ == '__main__':
    demo1("demo1")
    print()

    demo2("demo2")
    print()

    demo3("demo3")
    print()

    demo4("demo4")
    print()



