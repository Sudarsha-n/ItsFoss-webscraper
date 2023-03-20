import get_link
import requests
from bs4 import BeautifulSoup

x = get_link.get_link()
for i in str(x[1][0]).split():
    if "href" in i:
        l = str(x[1][0]).split().index(i)

def get_title():
    title = []
    for i in range(len(x[1])):
        title.append(str(str(x[1][i]).split()[3:l]).replace("aria-label=\"", "").replace("[", "").replace("]", "").replace(",", " ").replace("'", ""))
    return title

def clean_title(title):
    clean = []
    for i in title:
        if "href" in i:
            i = i.replace(i[i.index("href"):], "")
        clean.append(i)
    return clean

def clean_url(url_holder):
    clean_urll = []
    for i in url_holder:
        if ">Te" in i:
            i = i.replace(">Te", "")
        xl = list(i)
        if xl[-1] == "\"":
            xl.remove(xl[-1])
        if xl[-1] != "/":      
            xl.append("/")
        clean_urll.append(''.join(xl))
    return clean_urll

def description(url):
    final = {}
    for i in range(len(url)):
        conn = requests.get(url[i])
        soup = BeautifulSoup(conn.content)
        f = soup.find("div", class_='col-xs-12 col-lg-6')
        para = f.find("article").find_all("p")
        final[clean_title(get_title())[i]] = para[0:4]
    return final

def give_des():
    return description(clean_url(x[0])), clean_url(x[0])