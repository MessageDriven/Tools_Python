# coding:utf-8
import os
import sys
from PyPDF3 import PdfFileWriter, PdfFileReader


def add_encryption(path, encryptPath, fileDicts):
    pdf_writer = PdfFileWriter()
    for fileName in fileDicts:
        input_pdf = os.path.join(path, fileName)
        output_pdf = os.path.join(encryptPath, fileName)
        pdf_reader = PdfFileReader(input_pdf)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=fileDicts[fileName], owner_pwd=None,
                           use_128bit=True)

        #输出文件已存在便删除
        if os.path.exists(output_pdf):
            os.remove(output_pdf)

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)


def get_file(path, fileDicts):
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            password = file.split('_')[1]
            #print(file, password)
            fileDicts[file] = password


if __name__ == '__main__':
    fileDicts = {}
    encryptTemp = 'encrypt'
    #path = 'C://Users//劉成//Desktop//test'
    #print(sys.argv)
    if len(sys.argv) != 2:
        print('参数个数不正')
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print('加密文件路径不存在')
        sys.exit(1)

    encryptPath = os.path.join(path, encryptTemp)
    get_file(path, fileDicts)
    #print(fileDicts)

    if not os.path.exists(encryptPath):
        os.mkdir(encryptPath)

    add_encryption(path,  # 要加密的文件路径
                   encryptPath,  # 加密后要输出的文件路径
                   fileDicts)  # 文件名及密码
