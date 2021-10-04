import sys
import requests
from bs4 import BeautifulSoup
import lxml
def query_date(u):
    try:
        url = "https://www.youtube.com/watch?v=" + u
        pars = requests.get(url)
        soup = BeautifulSoup(pars.text, 'lxml')

        if "isLiveNow\":true," in str(soup):
            return "True"
        else:
            return "False"
    except:
        e = sys.exc_info()[1]
        return e

def link_check(start):
    try:
        if not start.strip():
            return

        source = start.replace("\n", '')
        ind = source.index("'")
        link = source[ind:].replace("'",'')
        res = source +" : " + query_date(link)
        return res
    except:
        return "Error: "+ str(sys.exc_info()[1])

f = open('C:\\Users\\Vlad\\Desktop\\Data_Streams.txt')
f = f.readlines()
for i in range(len(f)):
    result = link_check(f[i])
    if result != None:
        print(result)
