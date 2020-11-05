
import urllib
import random

#today = datetime.date.today()

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"

    ]
#yesterday = today - datetime.timedelta(days=1)

#print(yesterday)
url1= 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/Okt_2020/2020-10-21-de.pdf;jsessionid=52A059A5CF1DAFEEDA96D6B7E9331705.internet062?__blob=publicationFile'
url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/Okt_2020/2020-10-21-de.pdf;jsessionid=52A059A5CF1DAFEEDA96D6B7E9331705.internet062?__blob=publicationFile'
#wget.download(url,'2020-10-21-de.pdf')
randdom_header=random.choice(my_headers)
#randdom_header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
req = urllib.request.Request(url)
req.add_header("User-Agent", randdom_header)
req.add_header("Host", "www.rki.de")
req.add_header("Referer", "https://www.rki.de")
req.add_header("GET", url)

#r = urllib.request.urlopen(url)
data = urllib.request.urlopen(req).read()
print(data)
#result = data.read()

#with open('2020-10-21-de.pdf', "wb") as code:
    #code.write(data)
'''

#url = 'http://papers.xtremepapers.com/CIE/Cambridge%20IGCSE/Mathematics%20(0580)/0580_s03_qp_1.pdf'
r = requests.get(url)
with open('2020-10-21-de.pdf', "wb") as code:
    code.write(r.content)
    code.close()
'''