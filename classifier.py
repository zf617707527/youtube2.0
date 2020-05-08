import comment_downloader as CD
import fancySentiment as FS
import sys
sys.path.append('E:/爬取utube评论/YouTube-Sentiment-Analysis/CommentSentiment/')
import sentimentYouTube as SYT
import requests
import json

comments = []
with open('data.txt','r',encoding='utf-8') as f:
    for line in f:
        comments.append(line.strip('\n'))

FS.fancySentiment(comments)