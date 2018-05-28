from bs4 import BeautifulSoup

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
