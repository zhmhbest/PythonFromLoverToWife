import datetime
import time


class DateTimeHelper:

    @staticmethod
    def get_current_time_string():
        # return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now()

    @staticmethod
    def get_current_date():
        return datetime.date.today()

    @staticmethod
    def get_current_time_float():
        return time.time()

    @staticmethod
    def get_datetime_from_string(sdt):
        """
        从字符串创建一个datetime对象
        :param {string} sdt:
        """
        return datetime.datetime.strptime(sdt, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_date_from_string(sda):
        """
        从字符串创建一个date对象
        :param {string} sda:
        """
        s = sda.split('-')
        return datetime.date(int(s[0]), int(s[1]), int(s[2]))

    @staticmethod
    def to_string(dt):
        """
        将datetime对象转化为字符串
        :param {datetime} dt:
        """
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def to_seconds(dt):
        """
        将datetime对象换算成秒
        :param {datetime} dt:
        """
        return dt.seconds + dt.days * 24 * 3600

    @staticmethod
    def count_down_datetime_seconds(dt):
        """
        还有多少秒到达传入的时间
        :param {datetime} dt:
        """
        diff = dt - datetime.datetime.now()
        return diff.seconds + diff.days * 24 * 3600

    @staticmethod
    def count_down_date_days(da):
        """
        还有多少天到达传入的日期
        :param {date} da:
        """
        diff = da - datetime.date.today()
        return diff.days

    @staticmethod
    def after_current_datetime(**kwargs):
        """
        当前时间±一段时间后的日期
        :param kwargs:
            weeks
            days
            hours
            minutes
            seconds
            microseconds
        :return:
        """
        return datetime.datetime.now() + datetime.timedelta(**kwargs)

    @staticmethod
    def get_age(birth):
        """
        获取年龄
        :param birth: 出生日期
        :return: 天数
        """
        if isinstance(birth, str):
            birth = DateTimeHelper.get_date_from_string(birth)

        if isinstance(birth, datetime.date):
            today = datetime.date.today()
            diff = today - birth
            return diff.days
        else:
            return -1
