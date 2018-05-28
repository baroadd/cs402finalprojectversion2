import requests
from bs4 import BeautifulSoup

# url = "http://localhost/football boot/cart/view.php?product=1 'and 1=0"
#
# url = "http://www.rgcms.edu.in/announcement.php?id=6'"
#
# req = requests.get(url)
# soup = BeautifulSoup(req.content, "html.parser")
#
# # img = soup.find_all('img')
# # a = soup.find_all('a')
# # span = soup.find_all('span')
# # for i in range(0,7):
# #     hlist = soup.find_all('h' + str(i+1))
# #     print(hlist)
# #     print("\n")
# #
# # td = soup.find_all('td')
# # li = soup.find_all('li')
# # ul = soup.find_all('ul')
# #
# # print(img)
# # print("\n")
# # print(a)
# # print("\n")
# # print(span)
# # print("\n")
# # print(td)
# # print("\n")
# # print(li)
# # print("\n")
# # print(ul)
#
# isError = soup.find_all('font')
# print(isError)


L = ['h1', None, None, None, None, None, None, None, 'a', None, None, 'li', 'ul']
i = 0
print(L)
for str in L:
    i = i +1
    print(i)
    if str is None:
        L.remove(str)
        print(L)
