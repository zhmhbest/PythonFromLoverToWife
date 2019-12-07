"""
    字符串分析
    已知某配置文件的字符串（已给出）

    其中，以";"（半角）表示当前行为注释
    每个有效行为： 字段 = 值
    请尝试将以上内容翻译称Python的字典数据格式
"""

wait_parse_string = """
    ;【设置相关】
    SaveSettings=0
    SaveRecentFiles=0
    ;SaveFindReplace=0
    ;CloseFind=0
    ;CloseReplace=0
    ;NoFindWrap=0


    ;【自动换行】
    WordWrap=0
    ;WordWrapMode=1
    ;WordWrapIndent=0
    ;WordWrapSymbols=22
    ;ShowWordWrapSymbols=0
""".strip()


if __name__ == '__main__':
    # 以行分解字符串
    lines = wait_parse_string.split('\n')
    for line in lines:
        line = line.strip()  # 清除每行开头和结尾的空格
        print(line)
        # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
        # 判断开头是不是;
        # 如果不是就继续分解字符串
        # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑
    # end for(line)
