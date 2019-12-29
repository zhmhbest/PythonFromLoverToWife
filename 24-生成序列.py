"""
    yield
   器的一个关键字
"""


def demo1(demo_name):
    def sequence_generator(num):
        for i in range(num):
            yield i
    # end def
    seq = sequence_generator(10)
    print(demo_name, next(seq))
    print(demo_name, next(seq))


def demo2(demo_name):
    class SequenceGenerator:
        def __init__(self):
            self.index = -1

        def __next__(self):
            self.index += 1
            return self.index
    # end class
    sg = SequenceGenerator()
    print(demo_name, next(sg))
    print(demo_name, next(sg))


if __name__ == '__main__':
    demo1("demo1")
    demo2("demo2")

#
#
# g = foo()
# print(next(g))
# print("*" * 20)
# print(next(g))
