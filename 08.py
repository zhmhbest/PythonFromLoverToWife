"""
    日期计算
    1.计算1996-10-16过78天后是哪一天
    2.计算1996-10-16至2019年12月12日有多少天
    3.计算7:36:52至17:32:24有多少秒
"""
import datetime


if __name__ == '__main__':
    # 1
    d1 = datetime.date(1996, 10, 16)
    d1_after78 = d1 + datetime.timedelta(days=78)
    print(d1_after78.strftime("%Y-%m-%d"))

    # 2
    d2 = datetime.date(2019, 12, 12)
    delta_days = d2 - d1
    print(delta_days.days, "天")

    # 3
    t1 = datetime.timedelta(hours=7, minutes=36, seconds=52)
    t2 = datetime.timedelta(hours=17, minutes=32, seconds=24)
    print((t2 - t1).seconds, "秒")


