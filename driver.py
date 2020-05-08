import comment_downloader as CD
import fancySentiment as FS
# import sys
# sys.path.append('E:/爬取utube评论/YouTube-Sentiment-Analysis/CommentSentiment/')
import sentimentYouTube as SYT
import requests
import json
# import ssl
from obtain_url import *

def main():
	# EXAMPLE videoID = 'tCXGJQYZ9JA'
	# videoId = input("Enter the videoID : ")
	# videoId_all = ['aIT39A0dVXM','5b7ykEtAXZI','u99F5Bcylrk','MxTS5Y4o8dk','46A8zicGkbQ','dtuLOSqnJTk','-5WjHRyMX04','vSqB3vb-Cq0','0kpHKaSeVVE','NVJYNUOC57U','359b8MPfnhY','s1HHTF4mKbI','5b7ykEtAXZI&t=1s','h0V_HR1UBBg','QuqlhzxRLMs','yG13Gs_8xGc','B9rplmy5R00','FhHCznU-2Uc','IiOTXvvI5DI','0uyv-9TafCo','UuL3HTG0WH0','kZ0W7Q5d284','D1agD29flgw','Hvrvl9JpPjE','Ag0-2LdEq8Q']
	# Fetch the number of comments   
	# if count = -1, fetch all comments
	# count = int(input("Enter the no. of comment to extract : "))
	# pages = 15
	# requests.adapters.DEFAULT_RETRIES = 20
	# s = requests.session()
	# s.keep_alive = False
	# s.proxies = {'https':"122.15.131.65:57873"}
	for pages in range(1,100,6):
		print('已经爬到第%d页'%pages)
		videoId_all = []
		for i in range(pages, pages+6):
			html = getHtml("https://www.youtube.com/results?search_query="+"疫情"+"&lclk=short&filters=short&page=%s" % i)
			# print(html)
			# print(html)
			# print(i)
			# print(getUrl(html))
			videoId_all=videoId_all+getUrl(html)
			i += 1
		# videoId_all = ['aIT39A0dVXM']
		print(videoId_all)
		print('地址获取完毕')

		count = 500
		comments = []

		with open('verified_proxies.json', encoding='utf-8') as f:
			# for line in f:
			a = json.load(f)
		# final[a['type']] = a['host']+':'+a['port']

		for videoId in videoId_all:
			requests.adapters.DEFAULT_RETRIES = 20
			s = requests.session()
			flag = 0
			# s.proxies = {"http": "27.152.8.152:9999", "https": "117.57.91.131:24978"}
			s.keep_alive = False
			s.proxies = {a[flag]['type']:str(a[flag]['host'])+':'+str(a[flag]['port'])}
			flag = flag+1
			#时间的输入值  2020-02-16
			# date = '2020-02-16'
			comments = comments + CD.commentExtract(videoId, count)
		# print(comments)
		with open('data1.txt','a',encoding='utf-8') as f:
			for i in comments:
				f.write(i+'\n')
		print(comments)
		# SYT.sentiment(comments)
		# FS.fancySentiment(comments)



if __name__ == '__main__':
	main()
