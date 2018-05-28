import requests
from bs4 import BeautifulSoup

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

# 
# def print(isError):
#     if isError is True:
#         print ""
