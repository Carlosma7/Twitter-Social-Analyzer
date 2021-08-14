import tweepy
import json
import os
from dotenv import load_dotenv
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import re
import matplotlib.pyplot as plt
import spacy

class TwitterAnalyzer():
	def __init__(self):
		# Obtener información de .env
		load_dotenv(dotenv_path = '.env')

		# Authentication tokens
		self.consumer_key = os.getenv('API_KEY')
		self.consumer_secret = os.getenv('API_SECRET_KEY')
		self.access_token = os.getenv('ACCESS_TOKEN')
		self.access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
		# Tweepy Authentication
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)

		self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	# Clean text from tweets to get main info
	def clean_txt(self, tweet: str):
		# Remove mentions
		tweet = re.sub(r'@[A-Za-z0-9_]+', '', tweet)
		# Remove hashtags
		tweet = re.sub(r'#', '', tweet)
		# Remove RTs
		tweet = re.sub(r'RT[\s]+:', '', tweet)
		# Remove hyper links
		tweet = re.sub(r'https?:\/\/\S+', '', tweet)

		return tweet

	# Get the subjectivity of tweet
	def get_subjectivity(self, tweet: str):
		return TextBlob(tweet).sentiment.subjectivity

	# Get the polarity of tweet
	def get_polarity(self, tweet: str):
		return TextBlob(tweet).sentiment.polarity

	# Get the positive, negative or neutral analysis
	def get_analysis(self, score: float):
		if score < 0:
			return 'Negative'
		elif score == 0:
			return 'Neutral'
		else:
			return 'Positive'

	def print_popular_tweet(self, topic: str, num_items: int):
		for tweet in tweepy.Cursor(self.api.search, q=topic, result_type="popular", tweet_mode="extended").items(num_items):
			print('------------------------------------------------')
			print("TWEET:" + tweet._json["full_text"])
			print("USER:" + tweet._json["user"]["name"] + ' - ' + tweet._json["user"]["screen_name"])
			print("RT:" + str(tweet._json["retweet_count"]))
			print("FAV:" + str(tweet._json["favorite_count"]))
			print('------------------------------------------------')
			print('\n\n\n\n')

	def get_tweets(self, topic: str, num_items: int):
		return [tweet._json["full_text"] for tweet in tweepy.Cursor(self.api.search, q=topic, tweet_mode="extended").items(num_items)]

	def get_lexical_tokens(self, tweet: str):
		doc = self.nlp(tweet)

		lexical_tokens = [t.orth_ for t in doc if not t.is_punct | t.is_stop]
		return ' '.join(lexical_tokens)

	def analyze(self, topic: str, num_items: int, lang: str):

		# Create nlp object
		if lang == 'English':
			self.nlp = spacy.load('en_core_web_sm')
		else:
			self.nlp = spacy.load('es_core_news_sm')

		# Create a dataframe with a column called Tweets
		df = pd.DataFrame(self.get_tweets(topic=topic,num_items=num_items), columns=['Tweets'])

		# Apply clean text
		df['Tweets'] = df['Tweets'].apply(self.clean_txt)

		# Define subjectivity and polarity of tweets
		df['Subjectivity'] = df['Tweets'].apply(self.get_subjectivity)
		df['Polarity'] = df['Tweets'].apply(self.get_polarity)

		# Apply NLP
		df['Lexical'] = df['Tweets'].apply(self.get_lexical_tokens)

		# Plot the word cloud
		allWords = ' '.join([tweets for tweets in df['Lexical']])
		wordCloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 119).generate(allWords)

		plt.imshow(wordCloud, interpolation = 'bilinear')
		plt.axis('off')
		plt.show()

		# Get the analysis value
		df['Analysis'] = df['Polarity'].apply(self.get_analysis)

		# Print positive and negative tweets
		positive_df = df.sort_values(by=['Polarity'], ascending=False)
		negative_df = df.sort_values(by=['Polarity'], ascending=True)

		# Plot the polarity and subjectivity
		plt.figure(figsize=(8,6))
		for i in range(0, df.shape[0]):
			plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color="blue")

		plt.title('Sentiment Analysis')
		plt.xlabel('Polarity')
		plt.ylabel('Subjectivity')
		plt.show()

		# Get the percentage of positive tweets
		ntweets = df[df.Analysis == 'Positive']
		ntweets = ntweets['Tweets']

		percentage_positive = round((ntweets.shape[0] / df.shape[0] * 100), 1)

		# Get the percentage of negative tweets
		ntweets = df[df.Analysis == 'Negative']
		ntweets = ntweets['Tweets']

		percentage_negative = round((ntweets.shape[0] / df.shape[0] * 100), 1)

		# Value counts
		print(df['Analysis'].value_counts())
		print('Positive percentage: ' + str(percentage_positive) + '%')
		print('Negative percentage: ' + str(percentage_negative) + '%')

		plt.title('Sentiment Analysis')
		plt.xlabel('Sentiment')
		plt.ylabel('Counts')
		df['Analysis'].value_counts().plot(kind='bar')
		plt.show()