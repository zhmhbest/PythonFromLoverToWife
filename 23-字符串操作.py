"""
    字符串处理
"""

if __name__ == '__main__':
    """
        统计子串出现的次数
    """
    str1 = "abc123abcdef987poiabcabab"
    print("子串统计", str1.count('abc'))

    """
        空白删除
        \r、\n、\t显示效果都是空白的
    """
    str2 = " \t \r\n    abc    \r\n    "
    print("空白删除", '[' + str2.lstrip() + ']')
    print("空白删除", '[' + str2.rstrip() + ']')
    print("空白删除", '[' + str2.strip() + ']')

    """
        大小写转换
    """
    str3 = "A Na Ta No Ko To Ga Su Ki De Su"
    print("大小写", str3.upper())
    print("大小写", str3.lower())

    """
        查找字符串所在位置
    """
    str4_1 = "ABC456ABC101112ABC"
    str4_2 = "abc456abc101112abc"
    print("查找", str4_1.find("abc"))
    print("查找", str4_2.find("abc"))
    print("查找", str4_2.find("abc", 2))
    print("查找", str4_2.find("abc", 7))
    print("查找", str4_2.rfind("abc"))

    """
        字符串替换
    """
    str5 = "123abc456qwe789abc"
    print("替换", str5.replace('abc', '|||'))
    print("替换", str5.replace('abc', '|||', 1))

    """
        字符串分割
    """
    str6 = "123abc456qwe789abcqqq"
    print("分割", str6.split('abc'))
    print("分割", str6.split('abc', 1))

    """
        字符串切片
    """
    string_test = "0123456789"
    print('删头:', string_test[2:])
    print('删尾:', string_test[:-2])
    print('Left:\t', string_test[:3])
    print('Right:\t', string_test[-3:])
    print('Mid:\t', string_test[1:3])
    print('Mid:\t', string_test[3:7])

    """
        作业
        已知文件路径 C:\Program Files (x86)\Internet Explorer\iexplore.exe
        通过方法可返回
            文件路径：C:\Program Files (x86)\Internet Explorer
            文件名：iexplore.exe
            文件扩展名：exe
            文件磁盘：C
        请设计并实现该函数，并使得传入任意文件路径都可以返回类似的信息。
    """
    known_string1 = r"C:\Program Files (x86)\Internet Explorer\iexplore.exe"
    known_string2 = r"C:\Windows\System32\notepad.exe"
    known_string3 = r"C:\Users\zhmh\honey\gaoyu"

    def split_file_path(full_file_path):
        r_position = full_file_path.rfind('\\')
        file_path = full_file_path[:r_position]
        file_name = full_file_path[-(len(full_file_path)-r_position-1):]
        d_position = file_name.rfind('.')
        if d_position != -1:
            ext_name = file_name[-(len(file_name)-d_position-1):]
        else:
            ext_name = ""
        drive_name = full_file_path[:1]
        return file_path, file_name, ext_name, drive_name
    # end def
    print(split_file_path(known_string1))
    print(split_file_path(known_string2))
    print(split_file_path(known_string3))
