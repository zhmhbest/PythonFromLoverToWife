"""
    正则表达式
    请先详细阅读[https://deerchao.cn/tutorials/regex/regex.htm]
    做好笔记，然后阅读以下代码。
"""

import re


if __name__ == '__main__':
    """
    字符串开头是否满足正则表达式
    返回值 = re.match(正则表达式, 字符串)
        匹配不成功: 返回值为None
        匹配成功: 返回值为一个对象，该对象的span()方法可以返回匹配的范围。
    """
    reg_str1 = "[gG]it"
    print(re.match(reg_str1, "github"))
    print(re.match(reg_str1, "Github"))
    print(re.match(reg_str1, "git"))
    print(re.match(reg_str1, "Git"))
    print('-' * 30)
    # ------------------------------

    """
    在字符串中搜索第一个满足正则表达式的部分
    返回值 = re.search(正则表达式, 字符串)
        匹配不成功: 返回值为None
        匹配成功: 返回值为一个对象，该对象的span()方法可以返回匹配的范围。
    """
    print(re.search(reg_str1, "super-github!Git"))
    print(re.search(reg_str1, "powerGithub_git"))
    print('-' * 30)
    # ------------------------------

    """
    在一个字符串中搜索满足正则表达式的部分并替换成指定的内容
    替换后的字符串 = re.sub(正则表达式, 替换为字符串, 被搜索字符串[, 替换次数][, 匹配方法])
    替换后的字符串 = re.sub(正则表达式, 替换方法, 被搜索字符串[, 替换次数][, 匹配方法])
    """
    print(re.sub(reg_str1, "|||", "super-github!Git"))
    print(re.sub(reg_str1, "|||", "powerGithub_git"))
    print(re.sub(reg_str1, "|||", "powerGithub_git", 1))

    ret = re.sub(
        reg_str1,
        lambda matched: '[' + str(matched.group(0)) + ']',
        "powerGithub_git"
    )
    print(ret)
    print('-' * 30)
    # ------------------------------

    """
        生成一个正则表达式对象
    """
    reg_exp1 = re.compile("[gG]it")
    print(reg_exp1.match("github"))
    print(reg_exp1.match("Github"))
    print(reg_exp1.search("super-github!Git"))
    print(reg_exp1.sub("|||", "super-github!Git"))
    print(reg_exp1.sub(lambda matched: '<' + str(matched.group(0)) + '>', "super-github!Git"))

