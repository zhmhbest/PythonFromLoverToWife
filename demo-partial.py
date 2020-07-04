from functools import partial


def fun(content, name):
    print(name, "say", content)


if __name__ == '__main__':
    partial_fun = partial(fun, name='张三')
    partial_fun("世界之大，无奇不有！")
