import re
import os


def read_pdf_text_content(pdf_path: str):
    """
    ReadPdf
    :param pdf_path:
    :return:
    """
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfpage import PDFTextExtractionNotAllowed
    from pdfminer.pdfdocument import PDFNoOutlines
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.layout import LAParams, LTTextBox
    from pdfminer.converter import PDFPageAggregator
    from pdfminer.pdfpage import PDFPage

    assert os.path.exists(pdf_path)
    pdf_fp = open(pdf_path, 'rb')
    pdf_parser = PDFParser(pdf_fp)
    pdf_doc = PDFDocument(pdf_parser, password=b'')
    # 导航
    try:
        pdf_guide = [_guide[1] for _guide in pdf_doc.get_outlines()]
    except PDFNoOutlines:
        pdf_guide = []
    # 相关信息（作者等）
    pdf_info = pdf_doc.info
    if not pdf_doc.is_extractable:
        # 检查文档是否可以转成TXT
        raise PDFTextExtractionNotAllowed
    pdf_res_mgr = PDFResourceManager()
    pdf_lap_params = LAParams()
    pdf_device = PDFPageAggregator(rsrcmgr=pdf_res_mgr, laparams=pdf_lap_params)
    pdf_interpreter = PDFPageInterpreter(pdf_res_mgr, pdf_device)
    pdf_pages = PDFPage.create_pages(pdf_doc)
    # 文档信息
    doc_info = {
        'guide': pdf_guide,
        'info': pdf_info,
        'no': -1
    }
    for page in pdf_pages:
        pdf_interpreter.process_page(page)
        layout = pdf_device.get_result()
        for block in layout:
            if isinstance(block, LTTextBox):
                # 更新页数
                doc_info['no'] = pdf_device.pageno - 1
                yield {
                    'doc': doc_info,
                    'rect': (block.x0, block.y0, block.x1, block.y1),
                    'text': block.get_text()
                }


def convert_pdf_markdown(read_path, save_path=None):
    assert os.path.exists(read_path)
    if save_path is None:
        (filepath, filename) = os.path.split(read_path)
        (name, extension) = os.path.splitext(filename)
        save_path = os.path.abspath(f"{filepath}/{name}.md")

    def add_line(content):
        nonlocal fp
        fp.write(content)
        fp.write('\n\n')

    fp = open(save_path, 'w', encoding='utf-8')
    dump_guides = None
    is_headline = False
    # ■■■■■■■■ ■■■■■■■■ ■■■■■■■■ ■■■■■■■■
    for paragraph in read_pdf_text_content(read_path):
        # 初始参数
        is_headline = False
        # 整理段落
        text = paragraph['text'].strip()
        text = text.replace('-\n', '')
        text = text.replace('\n', ' ')
        text = re.sub(r'(?<!^)\[\d+\]', lambda _t: f'^{_t.group()}^', text)
        if len(text) < 6:
            continue
        # 检查导航
        if dump_guides is None:
            dump_guides = []
            for guide in paragraph['doc']['guide']:
                guide = guide.split(' ', 1)
                guide = guide[1] if guide.__len__() > 1 else guide[0]
                # print(guide)
                dump_guides.append(guide.strip().upper())
            if 0 == len(dump_guides):
                dump_guides = None
        if dump_guides:
            if len(text) < 50:
                for guide in dump_guides:
                    tmp = text.split(' ', 1)
                    tmp = (tmp[1] if tmp.__len__() > 1 else tmp[0]).upper().strip()
                    check_length = min(guide.__len__(), tmp.__len__())
                    if guide[:check_length] == tmp[:check_length]:
                        fp.write('## ')
                        is_headline = True
                        break
        else:
            # 提取段落信息
            if not is_headline:
                features = text.split(' ', 2)
                feature_first = features[0]
                feature_second = features[1] if features.__len__() > 1 else ''
                feature_first_word = (lambda __s: '' if __s is None else __s.group().upper())(
                    re.match(r'^\w+(?=(\W|$))', feature_first)
                )
                # print(f"({feature_first})[{feature_second}][{feature_first_word}]")
                # 摘要
                if 'ABSTRACT' == feature_first_word:
                    fp.write("## Abstract\n\n")
                    text = re.sub(r'^\w+\W+', '', text)
                # 标题识别
                if re.match(r'\d\.\d\.\d', feature_first):
                    fp.write("#### ")
                elif re.match(r'\d\.\d', feature_first):
                    fp.write("### ")
                elif (
                        re.match(r'\d(?![.%)\d\w])', feature_first) or
                        re.match(r'(I+|V|IV|VI)[.]', feature_first) or
                        'REFERENCES' == feature_first_word or
                        'INTRODUCTION' == feature_first_word
                ):

                    fp.write("## ")
        # 添加
        add_line(text)
    # ■■■■■■■■ ■■■■■■■■ ■■■■■■■■ ■■■■■■■■
    fp.close()


if __name__ == '__main__':
    file_path = r"E:\\UserProfile\Documents\\态势感知\\基金项目的核心文件\\核心文件"
    convert_pdf_markdown(f"{file_path}\\NDN_over_SDN_NFV.pdf")
