"""
    字符串分析
    已知某配置文件的字符串（已给出）

    其中，以";"（半角）开头表示当前行为注释
    每个有效行为： 字段 = 值
    请尝试将以上内容翻译为Python的字典数据格式
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


def demo_add_to_dict():
    dict1 = {}
    str = 'SaveSettings'
    dict1[str] = 1
    dict1['WordWrap'] = 0
    print(dict1)
    print()  # 换行


if __name__ == '__main__':
    demo_add_to_dict()  # 演示如何向字典中添加内容
    
    parsed_result = {}  # 声明一个空字典等待向其中添加内容
    lines = wait_parse_string.split('\n')  # 以行分解字符串
    for line in lines:
        line = line.strip()  # 清除每行开头和结尾的空格
        # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
        if ";" == line[0:1] or 0 == len(line):
            continue
            # 当前行被注释或为空，进入下一轮循环
        # end if
        kv = line.split('=')
        parsed_result[kv[0].strip()] = kv[1].strip()
        # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑
    # end for(line)
    print(parsed_result)
