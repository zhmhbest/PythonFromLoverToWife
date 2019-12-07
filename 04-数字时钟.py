"""
    制作一款数字时钟
    要求：每隔一秒打印一次当前系统的时间
"""
import time

if __name__ == '__main__':
    while True:
        sys_t = time.time()
        str_t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sys_t))
        print(str_t)
        # 暂停一秒
        time.sleep(1)
