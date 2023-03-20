import requests
from bs4 import BeautifulSoup

def get_link():   
    url = "https://itsfoss.com/"
    f = []
    source = requests.get(url)
    g = []
    soup = BeautifulSoup(source.content)
    results = soup.find(class_="container wrapper")
    pages = results.find_all(class_ = "post-card__title")
    for x in pages:
        f.append(x)
        pages_content = str(x)
        content_ = pages_content.split()
        l = 0
        for i in content_:
            if "href" in i:
                l = content_.index(i)
                g.append(content_[l][6:-6])
    return g, f