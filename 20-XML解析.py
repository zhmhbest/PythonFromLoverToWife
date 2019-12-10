"""
    【XML解析】
    方式1：SAX解析
        通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。
    方式2：DOM解析
        将XML数据在内存中解析成一个树，通过对树的操作来操作XML。
    方式3：ElementTree
        轻量级的DOM解析方式
"""
import xml.sax


class PreXMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        super(PreXMLHandler, self).__init__()  # 调用父类构造方法
        self.location = []  # 记录当前标签的位置
        self.attribute = None  # 记录当前标签的属性 AttributesImpl
        self.invalid = True

    # 元素开始事件处理
    def startElement(self, tag, attrs):
        self.location.append(tag)
        self.attribute = attrs._attrs

    # 元素结束事件处理
    def endElement(self, tag):
        self.location.pop()

    # 内容事件处理
    def characters(self, content):
        print('\t', '.'.join(self.location), self.attribute, content.strip())

    @staticmethod
    def get_handler(filename, handle):
        xml.sax.parse(filename, handle)
        return handle


class MyXMLHandler(PreXMLHandler):
    def __init__(self):
        super(MyXMLHandler, self).__init__()
        self.result = []
        self.current = None

    def startElement(self, tag, attrs):
        super(MyXMLHandler, self).startElement(tag, attrs)
        location = '.'.join(self.location)
        if "gpx.wpt" == location or "gpx.trk.trkseg.trkpt" == location:
            self.current = {}
            # 添加属性
            self.current['lat'] = self.attribute['lat']
            self.current['lon'] = self.attribute['lon']

    def endElement(self, tag):
        location = '.'.join(self.location)
        if "gpx.wpt" == location or "gpx.trk.trkseg.trkpt" == location:
            self.result.append(self.current)
            self.current = None
        # end if
        super(MyXMLHandler, self).endElement(tag)

    # 内容事件处理
    def characters(self, content):
        content = content.strip()
        location = '.'.join(self.location)
        # gpx.wpt
        # gpx.trk.trkseg.trkpt
        if None is not self.current:
            if "gpx.wpt.ele" == location or "gpx.trk.trkseg.trkpt.ele" == location:
                self.current['ele'] = content
            elif "gpx.wpt.name" == location or "gpx.trk.trkseg.trkpt.name" == location:
                self.current['name'] = content
            elif "gpx.wpt.time" == location or "gpx.trk.trkseg.trkpt.time" == location:
                self.current['time'] = content
        # end if

    def print_result(self):
        for line in self.result:
            print(line)


if __name__ == '__main__':
    handle = MyXMLHandler.get_handler("20-XML解析.xml", MyXMLHandler())
    handle.print_result()
