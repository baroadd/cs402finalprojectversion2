import requests
from bs4 import BeautifulSoup
from sqlinjectionRiskAssessment.checkingTools.errorbased import checkerror
from sqlinjectionRiskAssessment.checkingTools.boolean import config

def checkerrorbased(url):
    print("Error-Based Exploitation")
    soup = config.request(url)
    isError = checkerror.checkError(soup.find_all('font'))

    return isError
