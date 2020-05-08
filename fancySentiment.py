import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
def fancySentiment(comments):
	stopword = set(stopwords.words('english') + list(string.punctuation) + ['n\'t'])
	filtered_comments = []
	for i in comments:
		words = word_tokenize(i)
		temp_filter = ""
		for w in words:
			if w not in stopword:
				temp_filter += str(w)
				temp_filter += ' '
		filtered_comments.append(temp_filter)
	filtered_comments_str = ' '.join(filtered_comments)
	sentiment = WordCloud(background_color = 'orange', max_words=100)
	sentiment.generate(filtered_comments_str)

	# with open('cloud.txt','w',encoding='utf-8') as f:
	# 	f.write(str(sentiment.generate(filtered_comments_str)))
	plt.figure()
	plt.imshow(sentiment)
	plt.axis("off")
	plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
	plt.margins(0, 0)
	plt.savefig("final.png",dpi=300)
	plt.show()
