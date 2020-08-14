import re
import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox


def open_pdf(pdf_path):
    fp = open(pdf_path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser, password=b'')
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    parser.set_document(doc)
    resmgr = PDFResourceManager()
    lap = LAParams()
    device = PDFPageAggregator(resmgr, laparams=lap)
    interpreter = PDFPageInterpreter(resmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
        layout = device.get_result()
        for x in layout:
            if isinstance(x, LTTextBox):
                yield x.get_text().strip()


def convert_pdf(read_path, save_path=None):
    assert os.path.exists(read_path)
    if save_path is None:
        (filepath, filename) = os.path.split(read_path)
        (name, extension) = os.path.splitext(filename)
        save_path = os.path.abspath(f"{filepath}/{name}.md")
    with open(save_path, 'w', encoding='utf-8') as fp:
        for p in open_pdf(read_path):
            if len(p) > 10:
                p = re.sub(r"-\n", (lambda item: ''), p)
                p = re.sub(r"\n", (lambda item: ' '), p).strip()
                if re.findall(r'Peer-to-Peer Netw. Appl.', p):
                    continue
                p_head = p.split(' ', 1)[0]
                if not re.findall(r'\(\d\d\d\d\)', p) and not re.findall(r'http://', p):
                    if re.match(r'\d(?![.)])', p_head):
                        fp.write("## ")
                    elif re.match(r'\d\.\d+(?![.)])', p_head):
                        fp.write("### ")
                fp.write(p)
                fp.write('\n\n')


def convert_pdf_text(read_path, save_path=None):
    assert os.path.exists(read_path)
    if save_path is None:
        (filepath, filename) = os.path.split(read_path)
        (name, extension) = os.path.splitext(filename)
        save_path = os.path.abspath(f"{filepath}/{name}.md")
    with open(read_path, 'r', encoding='utf-8') as fp:
        text = fp.read()
    with open(save_path, 'w', encoding='utf-8') as fp:
        paragraphs = re.split(r"(\s*\n){2,}", text)
        for p in paragraphs:
            p = re.sub(r"-\n", (lambda item: ''), p)
            p = re.sub(r"\n", (lambda item: ' '), p).strip()
            fp.write(p)
            fp.write('\n')


if __name__ == '__main__':
    convert_pdf(r"E:\Userprofile\Documents\态势感知\基金项目的核心文件\DL-ML算法部分\2018SurveyOnSDNBasedNetworkIntrusi.pdf")