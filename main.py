# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import get_pdf

import extract_data
import generate_path

import os
import urllib.request


def get_pdf_by_url(folder_path, lists):
    if not os.path.exists(folder_path):
        print("Selected folder not exist, try to create it.")
        os.makedirs(folder_path)
    for url in lists:
        print("Try downloading file: {}".format(url))
        #filename = url.split('/')[-1]
        dir = os.getcwd();  # 当前工作目录。
        name = url.replace('https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/Okt_2020/','')
        name = name.replace('?__blob=publicationFile','')
        #urllib.request.urlretrieve(url,dir +'\\' + name)  # 下载pdf
        filepath = dir +'\\' + name
        if os.path.exists(filepath):
            print("File have already exist. skip")
        else:
            try:
                urllib.request.urlretrieve(url, filename=filepath)
            except Exception as e:
                print("Error occurred when downloading file, error message:")
                print(e)


if __name__ == "__main__":
    root_path = './October'
    paths = get_pdf.get_file(root_path)
    print(paths)
    '''
    for filename, path in paths.items():
        print('reading file: {}'.format(filename))
        with open(path, 'r') as f:
            lines = f.readlines()
            url_list = []
            for line in lines:
                url_list.append(line.strip('\n'))
            foldername = "./picture_get_by_url/pic_download/{}".format(filename.split('.')[0])
            get_pdf_by_url(foldername, url_list)
    '''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
