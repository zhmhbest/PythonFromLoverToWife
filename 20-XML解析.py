"""
    【XML解析】
    方式1：SAX解析（因数内存容量限制，数据量过大时只能使用这种方式）
        通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。
    方式2：DOM解析
        将XML数据在内存中解析成一个树，通过对树的操作来操作XML。
    方式3：ElementTree
        轻量级的DOM解析方式
"""
import xml.sax
import pandas as pd


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
            self.current['lat'] = float(self.attribute['lat'])
            self.current['lon'] = float(self.attribute['lon'])

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
                self.current['ele'] = float(content)
            elif "gpx.wpt.name" == location or "gpx.trk.trkseg.trkpt.name" == location:
                self.current['name'] = content
            elif "gpx.wpt.time" == location or "gpx.trk.trkseg.trkpt.time" == location:
                try:
                    tmp = content.split('T')
                    self.current['text_date'] = tmp[0]
                    self.current['text_time'] = tmp[1].split('Z')[0]
                    tmp = (self.current['text_time']).split(':')
                    self.current['t'] = int(tmp[0]) * 3600 + int(tmp[1]) * 60 + int(tmp[2])
                except IndexError as e:
                    print(self.current, e, content)
            # end if

    def get_result(self):
        return self.result


if __name__ == '__main__':
    result = MyXMLHandler.get_handler("20-XML解析.xml", MyXMLHandler()).get_result()
    # 将文件存为CSV文件
    pd.DataFrame(result).to_csv("21-数据分析.csv", index=False, index_label=False)
