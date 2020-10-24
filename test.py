import os
import datetime
import sys
import urllib.request
import requests

url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/Okt_2020/2020-10-21-de.pdf;jsessionid=52A059A5CF1DAFEEDA96D6B7E9331705.internet062?__blob=publicationFile'

r = requests.get(url, stream=True)
with open('2020-10-21-de.pdf', "wb") as Pypdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            Pypdf.write(chunk)
print('done!')