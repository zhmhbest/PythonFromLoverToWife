"""
    制作一款数字时钟
    要求：每隔一秒打印一次当前系统的时间
"""


def delay(seconds):
    import time
    time.sleep(seconds)


def get_current_time_string():
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


if __name__ == '__main__':
    while True:
        print(get_current_time_string())
        # 暂停一秒
        delay(1)
