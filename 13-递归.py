"""
    已知f(x+1) = f(x) * 2 + 1/f(x)
    f(0) = 1，求f(123)
"""


def f(x):
    a1 = x

    return (x*2) + (1/x)


if __name__ == '__main__':
    result = f(1)
    print(result)
