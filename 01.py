"""
    有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？
    各是多少？
    用Python编写程序并print所有的情况。
"""

if __name__ == '__main__':
    # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    print(i * 100 + j * 10 + k)
    # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑


