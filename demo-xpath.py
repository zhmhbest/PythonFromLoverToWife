# chrome://extensions : XPath Helper

"""
    【XPATH】
    /        : 根节点开始
    //       : 当前节点下，任意位置开始
    node     : 节点
    *        : 任意节点
    node()   : 任意节点
    .        : 当前节点
    ..       : 当前节点父节点
    @        : 选择属性、获取属性
    @*       : 获取标签的所有属性
    node[@*] : 带有属性的节点
    node[?]  : 属性选择器，? = @attribute='content'
    node[?]  : 内容选择器，? = text()='content'
    node[?]  : 位置选择器，? = <number> | last() | position() | expression
    text()   : 获取文本
"""

# pip install lxml
from lxml import etree

tree = etree.HTML("""
<html>
<body>
    <div class='first' text-align='center'>
        <ul>
            <li>11</li>
            <li>12</li>
            <li>13</li>
        </ul>
    </div>
    <div class='second'>
        <ul>
            <li>21</li>
            <li>22</li>
            <li>23</li>
        </ul>
    </div>
</body>
</html>
""")


def test_xpath(_path):
    print("_" * 16)
    print("! ", end='')
    for it in tree.xpath(_path):
        print(it, end=', ')
    print()


if __name__ == '__main__':
    test_xpath("//div[@class='first']/@*")
    test_xpath("//div[@class='first']/@class")

    test_xpath("//div/ul//text()")
    test_xpath("//div/ul/li/text()")

    test_xpath("//div[@class='first']/ul/li/text()")
    test_xpath("//div[@class='first']/ul/li[1]/text()")
    test_xpath("//div[@class='first']/ul/li[last()]/text()")
    test_xpath("//div[@class='first']/ul/li[last()-1]/text()")
    test_xpath("//div[@class='first']/ul/li[position()<=2]/text()")

