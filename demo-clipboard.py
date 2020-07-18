import pyperclip


def listen_clipboard(callback, speed=0.5):
    """
    实时监测剪切板
    """
    import pyperclip
    import time
    _recent = None
    while True:
        time.sleep(speed)
        _text = pyperclip.paste()
        if _text == _recent:
            continue
        # <do-sth>
        callback(_text)
        # </do-sth>
        _recent = _text


if __name__ == '__main__':
    # 设置剪切板内容
    pyperclip.copy("刚设置的内容")

    # 读取剪切板内容
    text = pyperclip.paste()
    print(text)

    # 侦听
    listen_clipboard(
        (lambda t: print(t))
    )
