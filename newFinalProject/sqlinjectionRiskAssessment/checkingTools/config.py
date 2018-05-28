import requests
from bs4 import BeautifulSoup

def request(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    return soup
