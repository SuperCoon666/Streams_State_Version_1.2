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

try:
    f = open('C:\\Users\\Vlad\\Desktop\\Data_Streams.txt')
    f = f.readlines()
    for i in range(len(f)):
        x = f[i].replace("\n", '')
        ind = x.index("'")
        numb = x[:ind]
        x = x[ind:].replace("'",'')

        if x=="\n" or x==" " or x=='':
            continue

        res = numb + "'" + x +"' : " + query_date(f[i])
        print(res)
except:
    print(sys.exc_info()[1])
