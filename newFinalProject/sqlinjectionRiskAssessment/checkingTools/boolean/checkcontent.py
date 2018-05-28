import re
from bs4 import BeautifulSoup

def checka(soup):
    codelist = []
    for a in soup:
        path = a.get('href')
        if path is not None:
            if path.replace(" ","") is None or path.replace(" ","") == "":
                codelist.append("404")
            else :
                codelist.append("200")

    return codelist

def checkContent(soup):
    codelist = []
    for c in soup:
        content = re.sub('\s+', '', c.get_text().replace(" ",""))
        if content is None or content.replace(" ","").upper().find("NULL") >= 0 or content.replace(" ","").upper().find("NONE") >= 0 or content.replace(" ","") == "":
            codelist.append("404")
        else :
            codelist.append("200")

    return codelist


