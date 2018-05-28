import requests
from bs4 import BeautifulSoup

url = "http://localhost/football%20boot/cart/view.php?product=1"

def checkimg(soup):
    codelist = []
    for img in soup:
        path = img.get('src').split("/")
        imgpath = path[len(path) - 1].split(".")[0]
        if imgpath.strip(" ") is None or imgpath.strip(" ") == "":
            codelist.append("404")
        else :
            codelist.append("200")

    return codelist

def checka(soup):
    codelist = []
    for a in soup:
        path = a.get('href')
        if path.strip(" ") is None or path.strip(" ") == "":
            codelist.append("404")
        else :
            codelist.append("200")

    return codelist

def checkContent(soup):
    codelist = []
    for c in soup:
        content = c.string
        if content.strip(" ") is None or content.strip(" ") == "":
            codelist.append("404")
        else :
            codelist.append("200")

    return codelist


def addtestcase(url):
    url = url + " 'and 1=0"
    return url

def request(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    return soup

def compare(list1, list2):
    isError = False
    for index in range(len(list1)):
        if list1[index] != list2[index]:
            isError = True
    return isError

# Tag Image
soup = request(url)
imglist1 = checkimg(soup.find_all('img'))
url = addtestcase(url)
soup = request(url)
imglist2 = checkimg(soup.find_all('img'))
isErrorimg = compare(imglist1, imglist2)

print(isErrorimg)

# Tag a
# soup = request(url)
# alist1 = checka(soup.find_all('a'))
# url = addtestcase(url)
# soup = request(url)
# alist2 = checka(soup.find_all('a'))
# isErrora = compare(alist1, alist2)


# Tag span
# soup = request(url)
# spanlist1 = checkContent(soup.find_all('span'))
# url = addtestcase(url)
# soup = request(url)
# spanlist2 = checkContent(soup.find_all('span'))
# isErrorspan = compare(spanlist1, spanlist2)


# Tag h1-7
# for i in range(1, 7):
#     soup = request(url)
#     hlist1 = checkContent(soup.find_all('h' + i))
#     url2 = addtestcase(url)
#     soup = request(url2)
#     hlist2 = checkContent(soup.find_all('h' + i))
#     isErrorh = compare(hlist1, hlist2)


# Tag td
# soup = request(url)
# tdlist1 = checkContent(soup.find_all('td'))
# url = addtestcase(url)
# soup = request(url)
# tdlist2 = checkContent(soup.find_all('td'))
# isErrortd = compare(tdlist1, tdlist2)


# Tag li
# soup = request(url)
# lilist1 = checkContent(soup.find_all('li'))
# url = addtestcase(url)
# soup = request(url)
# lilist2 = checkContent(soup.find_all('li'))
# isErrorli = compare(lilist1, lilist2)





# print(soup.prettify())
