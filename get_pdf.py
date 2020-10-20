import os
import datetime
import sys
import urllib.request
import requests


month = {
    'Okt_2020': [10, 1, 19],
    'Sept_2020': [9, 1, 31],
    'Aug_2020': [8, 1, 32],
    'Jul_2020': [7, 1, 32],
    'Jun_2020': [6, 1, 31],
    'Mai_2020': [5, 1, 32],
    'Apr_2020': [4, 1, 31],
    'Mar_2020': [3, 4, 32]
}
print(month['Okt_2020'][1],month['Okt_2020'][2])
def get_file(FolderPath,startdate,enddate):
    if month[FolderPath] ==9 or month[FolderPath] ==10:
        path = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/'+FolderPath+'/'
        ending = '?__blob=publicationFile'
    else:
        path = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/'
        ending = '?__blob=publicationFile'
    if not os.path.exists('./'+FolderPath):
        print(FolderPath," not exist, try to create it.")
        os.makedirs('./'+FolderPath)

    for diff in range(startdate,enddate):
        date = datetime.date.today().replace(month=month[FolderPath][0],day=diff)
        pdfname = str(date)+'-de.pdf'
        url = path + pdfname +ending
        r = requests.get(url)
        with open(FolderPath +'\\' + pdfname, "wb") as code:
            code.write(r.content)

def downloadAllMonth():
    for folder in month.keys():
        get_file(folder,int(month[folder][1]),int(month[folder][2]))

downloadAllMonth()
