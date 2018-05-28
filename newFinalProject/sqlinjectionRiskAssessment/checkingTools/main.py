import requests
from bs4 import BeautifulSoup
from sqlinjectionRiskAssessment.checkingTools import checkboolean
from sqlinjectionRiskAssessment.checkingTools import checkerrorbased

def scan(url):

    # url = "http://www.cs.tu.ac.th/articleview-inner.php?id=573&type=3"
# url = "http://4bearz.com/test.php?dt=1"
# url = "http://www.rgcms.edu.in/announcement.php?id=6'"
# url = "http://testasp.vulnweb.com/showforum.asp?id=0"
    # return taglist
    boolean = checkboolean.checkboolean(url)
    # return boolean
    errorbased = checkerrorbased.checkerrorbased(url)

    return (boolean,errorbased)
