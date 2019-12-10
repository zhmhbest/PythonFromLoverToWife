"""
    静态方法
"""


class Hello:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def say(sth):
        print("静态方法", sth)

    def say_from_heart(self, sth):
        print(self.name, sth)


if __name__ == '__main__':
    Hello.say("Who are you?")

    try:
        Hello.say_from_heart("I am ?")
    except TypeError:
        print("调用 Hello.say_2 时 发生错误！")
    # end try

    hello = Hello("ZHMH")
    hello.say_from_heart("love you!")
