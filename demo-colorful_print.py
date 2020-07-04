"""
    文本颜色
    打印彩色字体方法: \033[{{显示方式}};{{字体色}};{{背景色}}m{{打印的内容}}\033[0m
    以下是对该方法的封装
"""


class RichPrint:
    CONTROL = {
        'DEFAULT': 0,
        'BOLD': 1,
        'UNDERLINE': 4,
        'FLASH': 5,     # 无效
        'SWAP': 7,
        'HIDE': 8,      # 无效
    }
    COLORS = {
        'WHITE':    0, 'w': 0,
        'RED':      1, 'r': 1,
        'GREEN':    2, 'g': 2,
        'YELLOW':   3, 'y': 3,
        'BLUE':     4, 'b': 4,
        'PURPLE':   5, 'p': 5,
        'CYAN':     6, 'c': 6,
        'SHALLOW':  7, 's': 7,
    }

    @staticmethod
    def head(ct, fg, bg):
        ct = '10' if ct is None else str(RichPrint.CONTROL[ct])
        fg = '40' if fg is None else str(30 + RichPrint.COLORS[fg])
        bg = '50' if bg is None else str(40 + RichPrint.COLORS[bg])
        print(f'\033[{ct};{fg};{bg}m', end='')

    @staticmethod
    def tail():
        print('\033[0m', end='')

    @staticmethod
    def p(content, foreground=None, background=None, control=None):
        """
        彩色不换行打印
        :param content: 内容
        :param foreground: 前景色
        :param background: 背景色
        :param control: 其它效果
        :return: None
        """
        RichPrint.head(control, foreground, background)
        print(content, end='')
        RichPrint.tail()

    @staticmethod
    def pb(content, foreground=None, background=None, control=None):
        """
        彩色换行打印
        :param content: 内容
        :param foreground: 前景色
        :param background: 背景色
        :param control: 其它效果
        :return:
        """
        RichPrint.head(control, foreground, background)
        print(content, end='')
        RichPrint.tail()
        print()

    @staticmethod
    def pl(content, foreground=None, background=None, control=None):
        """
        彩色换行打印
        :param content: 内容
        :param foreground: 前景色
        :param background: 背景色
        :param control: 其它效果
        :return:
        """
        RichPrint.head(control, foreground, background)
        print(content)
        RichPrint.tail()


if __name__ == '__main__':
    print('DEFAULT')
    RichPrint.pl('WHITE', 'w')
    RichPrint.pl('RED', 'r')
    RichPrint.pl('GREEN', 'g')
    RichPrint.pl('YELLOW', 'y')
    RichPrint.pl('BLUE', 'b')
    RichPrint.pl('PURPLE', 'p')
    RichPrint.pl('CYAN', 'c')
    RichPrint.pl('SHALLOW', 's')

    RichPrint.pb('WHITE', background='w')
    RichPrint.pb('RED', background='r')
    RichPrint.pb('GREEN', background='g')
    RichPrint.pb('YELLOW', background='y')
    RichPrint.pb('BLUE', background='b')
    RichPrint.pb('PURPLE', background='p')
    RichPrint.pb('CYAN', background='c')
    RichPrint.pb('SHALLOW', background='s')

    RichPrint.pl('WHITE', background='w')
    RichPrint.pl('RED', background='r')
    RichPrint.pl('GREEN', background='g')
    RichPrint.pl('YELLOW', background='y')
    RichPrint.pl('BLUE', background='b')
    RichPrint.pl('PURPLE', background='p')
    RichPrint.pl('CYAN', background='c')
    RichPrint.pl('SHALLOW', background='s')

    print("请注意！不要太", end='')
    RichPrint.p('爱', 'r', control='BOLD')
    RichPrint.p('爱', 'r', control='UNDERLINE')
    RichPrint.p('爱', 'r', control='SWAP')
    RichPrint.p('爱', 'r')
    print("我哦！", end='')
