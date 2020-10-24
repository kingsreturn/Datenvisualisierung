import os
import datetime
import sys
import urllib.request
import requests
import wget
import urllib
import urllib3
import random


my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

month = {
    'Okt_2020': [10, 1, 24],
    'Sept_2020': [9, 1, 31],
    'Aug_2020': [8, 1, 32],
    'Jul_2020': [7, 1, 32],
    'Jun_2020': [6, 1, 31],
    'Mai_2020': [5, 1, 32],
    'Apr_2020': [4, 1, 31],
    'Mar_2020': [3, 4, 32]
}
#print(month['Okt_2020'][1],month['Okt_2020'][2])
def get_file(FolderPath,startdate,enddate):
    print(FolderPath)
    print(month[FolderPath])
    if month[FolderPath][0] ==9 or month[FolderPath][0] ==10:
        path = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/'+FolderPath+'/'
        ending = ';jsessionid=52A059A5CF1DAFEEDA96D6B7E9331705.internet062?__blob=publicationFile'
    else:
        path = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/'
        ending = '?__blob=publicationFile'
    if not os.path.exists('./'+FolderPath):
        print(FolderPath," not exist, try to create it.")
        os.makedirs('./'+FolderPath)
    print(path)
    for diff in range(startdate,enddate):
        date = datetime.date.today().replace(month=month[FolderPath][0],day=diff)
        pdfname = str(date)+'-de.pdf'
        url = path + pdfname +ending
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'host': 'www.rki.de',
            'User-agent': random.choice(my_headers)
        }
        r = requests.get(url,headers = head)
        print(r.status_code)
        #r.encoding='ascii'
        print(pdfname)
        #r= urllib.request.urlopen(url)
        #data = r.read()
        #with open(FolderPath +'\\' + pdfname, "wb") as code:
            #code.write(data)
        #wget.download(url,FolderPath +'\\' + pdfname)
        if(r.status_code ==200):
            with open(FolderPath + '\\' + pdfname, "wb") as code:
                code.write(r.content)
            #code.close()
        #print(pdfname, " is downloaded!")
def downloadAllMonth():
    for folder in month.keys():
        get_file(folder,int(month[folder][1]),int(month[folder][2]))

downloadAllMonth()
#https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/Okt_2020/2020-10-18-en.pdf?__blob=publicationFile
#https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/2020-10-01-en.pdf?__blob=publicationFile
#https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/Okt_2020/2020-10-18-en.pdf?__blob=publicationFile
#https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/2020-06-01-en.pdf?__blob=publicationFile
#https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/2020-06-01-en.pdf?__blob=publicationFile