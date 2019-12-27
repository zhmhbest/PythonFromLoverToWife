"""
    装饰器
"""


def demo1():
    def fun_decorate(fn):
        print('A')
        fn()

    @fun_decorate
    def fun_test():
        print('B')

    fun_test


if __name__ == '__main__':
    demo1()
