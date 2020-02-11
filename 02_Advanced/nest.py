"""
    nonlocal关键字用于在函数嵌套时，使用上层函数的变量
    如果使用global关键字，则表明该变量是全局的
"""

my_var = "全局变量"


def test_var():
    def test_g():
        global my_var
        print(my_var)

    def test_l():
        nonlocal my_var
        print(my_var)

    my_var = "局部变量"
    test_g()
    test_l()


# 闭包
def closer():
    def return_function():
        nonlocal index
        print(index)
        index += 1
    index = 0
    return return_function


if __name__ == '__main__':
    test_var()

    print("\n闭包演示")
    f = closer()
    f()
    f()
    f()
    f()
