"""
    异常处理
"""
import random


# 自定义异常
# 需要继承Exception类，Exception类继承自BaseException
# BaseException几乎是所有异常的最远父类
class MyError(Exception):  # 按住Ctrl，左键点击此处的Exception，可以看到其定义
    def __init__(self, err):
        Exception.__init__(self, err)
        # err文本用于说明对当前异常的描述


# 产生一个自定义的异常
def test_error_my():
    raise MyError("这是一个用户自己定义的异常")
    # 使用raise关键字可以抛出一个自定义的异常


# 产生一个系统预定义好的异常
def test_error_index():
    print([][0])
    # 以上命令表示打印空列表的第0个元素。
    # 因为是空列表，所以运行时肯定会发生错误。


# 使用 try except 来捕获错误
def loop_body():
    # 只有在try-except区间产生的异常才会被捕获
    try:
        xxx = random.randint(0, 2)  # 可能等于 0 or 1 or 2
        if 0 == xxx:
            test_error_index()
        elif 1 == xxx:
            test_error_my()
        else:
            # 没有抛出异常
            print("[正常      ]", end=' ')
        # end if
        print('end try body', end=' | ')
    except IndexError as err:  # 按住Ctrl，左键点击此处的IndexError，可以看到其定义
        print("[捕获_Index]", end=' ')
        print(err, end=' | ')
    except MyError as err:
        print("[捕获_My   ]", end=' ')
        print(err, end=' | ')
    finally:
        print("不论是否有异常发生这条语句总是会在最后执行")
    # end try


if __name__ == '__main__':
    # test_error_index()
    """
    以上注释部分如果运行，将产生以下错误信息：
    ____________________________________________________
    Traceback (most recent call last):
      File ".../14-异常处理.py", line 53, in <module>
        test_error_index()
      File ".../14-异常处理.py", line 24, in test_error_index
        print([][0])
    IndexError: list index out of range
    ————————————————————————————————————————————————————
    【错误文本说明】
        因为这个错误是在一个方法内产生的
        所以本质上调用方法的地方也是错误的发生位置，不过不是直接位置
        第一个File指定的是最近的位置（第 53 行），因为调用方法产生了错误。
        第二个File指定是更深入地方的错误位置（第 24 行）
        有些情况错误可能会很深入，所以就会打印出非常多的{File 文件名 行 ...}
        最后一行说明了
            异常名称: 详细说明
        我们可以通过捕获错误名称来使发生错误时程序不中断继续执行
        特别需要注意的是，不一定最后一个错误位置就是导致错误发生的根本原因
            比如调用一个系统方法，方法指定了参数只能是数字，你传了个字符串
            这样就会报出一大串错误（因为系统方法一般很深）
            但实际错误原因是最上面一层，你使用出现了问题。
    """
    for i in range(15):
        loop_body()
    # end for
    print("程序已运行到结尾")
