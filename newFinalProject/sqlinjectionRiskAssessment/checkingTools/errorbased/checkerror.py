from bs4 import BeautifulSoup


def checkError(soup):
    isError = False
    for c in soup:
        content = c.get_text()
        if content is not None:
            if content.find("TEP_DB_ERROR") >= 0:
                isError = True
    return isError
