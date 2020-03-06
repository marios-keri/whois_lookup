import requests
from bs4 import BeautifulSoup as bs
import sys

__author__ = 'Marios keri'
__date__ = '06-02-2020'


domain = sys.argv[1]
url = f'https://www.whois.com/whois/{domain}'


res = requests.get(url)

if res.ok:
    bsobj = bs(res.content, 'html5lib')
    content = bsobj.find('pre', {'class': 'df-raw'}).text
    print(content[: content.find('>>>')])
