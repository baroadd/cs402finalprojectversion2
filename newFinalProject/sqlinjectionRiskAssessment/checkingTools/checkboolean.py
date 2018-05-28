import requests
from bs4 import BeautifulSoup
from sqlinjectionRiskAssessment.checkingTools.boolean import config
from sqlinjectionRiskAssessment.checkingTools.boolean import checknull
from sqlinjectionRiskAssessment.checkingTools.boolean import checkcontent
from sqlinjectionRiskAssessment.checkingTools.boolean import testcase

def checkboolean(url):
    taglist = []
    print("Boolean Exploitation\n")
    soup = config.request(url)

    # Tag Image
    imglist1 = checknull.checkimg(soup.find_all('img'))

    # Tag a
    alist1 = checkcontent.checka(soup.find_all('a'))
    #
    # Tag span
    spanlist1 = checkcontent.checkContent(soup.find_all('span'))

    # Tag td
    tdlist1 = checkcontent.checkContent(soup.find_all('td'))

    # Tag li
    lilist1 = checkcontent.checkContent(soup.find_all('li'))

    # Tag ul
    ullist1 = checkcontent.checkContent(soup.find_all('ul'))

    # Tag h1-7
    isErrorh = [False, False, False, False, False, False, False]
    for i in range(0,7):
        hlist1 = checkcontent.checkContent(soup.find_all('h' + str(i+1)))
        url2 = testcase.addtestcase(url)
        soup = config.request(url2)
        hlist2 = checkcontent.checkContent(soup.find_all('h' + str(i+1)))
        isErrorh[i] = testcase.compare(hlist1, hlist2)
        taglist.append(testcase.package('h' + str(i+1),isErrorh[i]))

    url = testcase.addtestcase(url)
    soup = config.request(url)

    # Tag Image
    imglist2 = checknull.checkimg(soup.find_all('img'))
    isErrorimg = testcase.compare(imglist1, imglist2)
    taglist.append(testcase.package("img",isErrorimg))

    # Tag a
    alist2 = checkcontent.checka(soup.find_all('a'))
    isErrora = testcase.compare(alist1, alist2)
    taglist.append(testcase.package("a",isErrora))

    # Tag span
    spanlist2 = checkcontent.checkContent(soup.find_all('span'))
    isErrorspan = testcase.compare(spanlist1, spanlist2)
    taglist.append(testcase.package("span",isErrorspan))

    # Tag td
    tdlist2 = checkcontent.checkContent(soup.find_all('td'))
    isErrortd = testcase.compare(tdlist1, tdlist2)
    taglist.append(testcase.package("td",isErrortd))

    # Tag li
    lilist2 = checkcontent.checkContent(soup.find_all('li'))
    isErrorli = testcase.compare(lilist1, lilist2)
    taglist.append(testcase.package("li",isErrorli))

    # Tag ul
    ullist2 = checkcontent.checkContent(soup.find_all('ul'))
    isErrorul = testcase.compare(ullist1, ullist2)
    taglist.append(testcase.package("ul",isErrorul))

    return taglist
