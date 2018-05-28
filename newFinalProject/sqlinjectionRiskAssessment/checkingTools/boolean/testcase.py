def addtestcase(url):
    url = url + " 'and 1=0"
    return url


def compare(list1, list2):
    isError = False
    for i in range(len(list1)):
        try:
            if list1[i] != list2[i]:
                isError = True
        except Exception as e:
            # driver = webdriver.Chrome()
            # print(driver.current_url)
            # if redirect
            isError = True
    return isError

def package(tag,isError):
    if isError is True:
        return tag
