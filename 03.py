"""
请输出 9*9 乘法口诀表
"""

# 显示 2 × 3 = 6 且不换行的代码如下
print("%d × %d = %d" % (2, 3, 6), end='')

# 什么都不打印只换行的代码如下
print()

"""
期望效果如下，不允许直接输出字符串！
1 × 1 = 1	
1 × 2 = 2	2 × 2 = 4	
1 × 3 = 3	2 × 3 = 6	3 × 3 = 9	
1 × 4 = 4	2 × 4 = 8	3 × 4 = 12	4 × 4 = 16	
1 × 5 = 5	2 × 5 = 10	3 × 5 = 15	4 × 5 = 20	5 × 5 = 25	
1 × 6 = 6	2 × 6 = 12	3 × 6 = 18	4 × 6 = 24	5 × 6 = 30	6 × 6 = 36	
1 × 7 = 7	2 × 7 = 14	3 × 7 = 21	4 × 7 = 28	5 × 7 = 35	6 × 7 = 42	7 × 7 = 49	
1 × 8 = 8	2 × 8 = 16	3 × 8 = 24	4 × 8 = 32	5 × 8 = 40	6 × 8 = 48	7 × 8 = 56	8 × 8 = 64	
1 × 9 = 9	2 × 9 = 18	3 × 9 = 27	4 × 9 = 36	5 × 9 = 45	6 × 9 = 54	7 × 9 = 63	8 × 9 = 72	9 × 9 = 81
"""
print("================================")
if __name__ == '__main__':
    # 提示：print()方法只能按行打印。
    # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
    for line in range(1, 10):
        # 第 line 行有 line 列
        for col in range(1, line+1):
            print("%d × %d = %d\t" % (col, line, line*col), end='')
            # \t是制表符，可以做到对齐的效果。
        # end for (col)
        print()
    # end for (line)
    # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑
print("================================")
