from browsermobproxy import Server
from selenium.webdriver.common.by import By
import psutil
import time
import json
from selenium import webdriver
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def find_sitemap(url):
    for proc in psutil.process_iter():
        if proc.name() == "browsermob-proxy":
            proc.kill()

    dict = {'port': 8090}
    server = Server(path="C:/Users/SUPAWATSIRINTRANON/Desktop/browsermob-proxy-2.1.4/bin/browsermob-proxy", options=dict)

    server.start()
    time.sleep(1)
    proxy = server.create_proxy()
    time.sleep(1)

    profile = webdriver.FirefoxProfile()
    selenium_proxy = proxy.selenium_proxy()
    profile.set_proxy(selenium_proxy)
    driver = webdriver.Firefox(firefox_profile=profile)
    proxy.new_har("site")
    driver.get(url)
    elm = driver.find_elements_by_tag_name('a')
    links = []
    for i in range(len(elm)):
        links.append(elm[i].get_attribute('href'))
    newlinks = []
    for link in links:
        if link not in newlinks:
            newlinks.append(link)
    for link in newlinks:
        print ('navigating to: ' + link)
        driver.get(link)
    path = './'
    fileName = 'trafficCapture'
    writeToJSONFile(path, fileName, proxy.har)
    driver.quit()


