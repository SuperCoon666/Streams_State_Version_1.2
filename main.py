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
        source = start.replace("\n", '')
        ind = source.index("'")
        link = source[ind:].replace("'",'')
        res = source +" : " + query_date(link)
        return res
    except:
        return "Error: "+ str(sys.exc_info()[1])

f = open('C:\\Users\\Vlad\\Desktop\\Data_Streams(1).txt')
f = f.readlines()
numbers = ""
for i in range(len(f)):
    if not f[i].strip():
            continue
    result = link_check(f[i])

    if "False" in result:
        ind = f[i].index("'")
        numb_i = f[i]
        numb_i = numb_i[:ind]
        numbers+= " "+numb_i

    print(result)
print(numbers)
