# coding:utf-8

import re
import urllib.request
from urllib.parse import quote
import string
import requests

def getHtml(url):
    url = quote(url, safe=string.printable)  #对中文进行识别
    page = urllib.request.urlopen(url)
    # page.close()
    html = page.read()
    return html


def getUrl(html):
    reg = r"(?<=a\shref=\"/watch).+?(?=\")"
    urlre = re.compile(reg)
    urllist = re.findall(urlre, html.decode('utf-8'))
    format = "https://www.youtube.com/watch%s\n"
    # f = open("output.txt", 'w')
    # for url in urllist:
    #     result = (format % url)
    #     f.write(result)
    # f.close()
    videoId_all = []
    for url in urllist:
        # print(url)
        # print(url.split('=')[1])
        videoId_all.append(url.split('=')[1])
    return videoId_all

if __name__ == '__main__':
    pages = 10
    for i in range(1, pages):
        html = getHtml("https://www.youtube.com/results?search_query="+"疫情"+"&lclk=short&filters=short&page=%s" % i)
        # print(getUrl(html))
        getUrl(html)
        i += 1