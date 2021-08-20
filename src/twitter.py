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
	"""
	Twitter Sentiment Analyzer that contains a tweepy API. It can search most popular tweets, get subjectivity, polarity and a resume about any topic given.
	"""

	def __init__(self):
		"""
		Constructor. Defines the Tweepy API.
		"""

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
		"""
		Takes a tweet text.
		Returns the tweet text without any mention, hashtag, RT or link.
		"""

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
		"""
		Takes a tweet text.
		Returns the subjectivity.
		"""

		return TextBlob(tweet).sentiment.subjectivity

	# Get the polarity of tweet
	def get_polarity(self, tweet: str):
		"""
		Takes a tweet text.
		Returns the polarity.
		"""

		return TextBlob(tweet).sentiment.polarity

	# Get the positive, negative or neutral analysis
	def get_analysis(self, score: float):
		"""
		Takes a score from a tweet.
		Returns the analysis (positive, negative or neutral).
		"""

		if score < 0:
			return 'Negative'
		elif score == 0:
			return 'Neutral'
		else:
			return 'Positive'

	def print_popular_tweet(self, topic: str, num_items: int):
		"""
		Takes a topic and a number of tweets.
		Prints the n most popular tweets about the topic.
		"""

		for tweet in tweepy.Cursor(self.api.search, q=topic, result_type="popular", tweet_mode="extended").items(num_items):
			print('------------------------------------------------')
			print("TWEET:" + tweet._json["full_text"])
			print("USER:" + tweet._json["user"]["name"] + ' - ' + tweet._json["user"]["screen_name"])
			print("RT:" + str(tweet._json["retweet_count"]))
			print("FAV:" + str(tweet._json["favorite_count"]))
			print('------------------------------------------------')
			print('\n\n\n\n')

	def get_popular_tweets(self, topic: str):
		"""
		Takes a topic.
		Returns the 3 most popular tweets about that topic.
		"""

		return tweepy.Cursor(self.api.search, q=topic, result_type="popular", tweet_mode="extended").items(3)

	def get_tweets(self, topic: str, num_items: int):
		"""
		Takes a topic and a number of tweets.
		Returns the n most recent tweets about that topic.
		"""

		return [tweet._json["full_text"] for tweet in tweepy.Cursor(self.api.search, q=topic, tweet_mode="extended").items(num_items)]

	def get_lexical_tokens(self, tweet: str):
		"""
		Takes a tweet text.
		Returns just the lexical tokens.
		"""

		doc = self.nlp(tweet)

		lexical_tokens = [t.orth_ for t in doc if not t.is_punct | t.is_stop]
		return ' '.join(lexical_tokens)

	def analyze(self, topic: str, num_items: int, lang: str):
		"""
		Takes a topic, a number of tweets and language.
		Obtains n most recent tweets, applies NLP, generates a word cloud, computes subjectivity and polarity and creates several plots.
		"""

		# Create nlp object
		if lang == 'English':
			self.nlp = spacy.load('en_core_web_sm')
		else:
			self.nlp = spacy.load('es_core_news_sm')

		# Create a dataframe with a column called Tweets
		self.df = pd.DataFrame(self.get_tweets(topic=topic,num_items=num_items), columns=['Tweets'])

		# Apply clean text
		self.df['Tweets'] = self.df['Tweets'].apply(self.clean_txt)

		# Define subjectivity and polarity of tweets
		self.df['Subjectivity'] = self.df['Tweets'].apply(self.get_subjectivity)
		self.df['Polarity'] = self.df['Tweets'].apply(self.get_polarity)

		# Apply NLP
		self.df['Lexical'] = self.df['Tweets'].apply(self.get_lexical_tokens)

		# Plot the word cloud
		allWords = ' '.join([tweets for tweets in self.df['Lexical']])
		self.wordCloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 119).generate(allWords)

		# Save word cloud
		plt.imshow(self.wordCloud, interpolation = 'bilinear')
		plt.axis('off')
		plt.savefig('./report/wordcloud.png', bbox_inches='tight')
		plt.clf()

		# Get the analysis value
		self.df['Analysis'] = self.df['Polarity'].apply(self.get_analysis)

		# Plot the polarity and subjectivity
		plt.figure(figsize=(8,6))
		for i in range(0, self.df.shape[0]):
			plt.scatter(self.df['Polarity'][i], self.df['Subjectivity'][i], color="blue")

		plt.title('Sentiment Analysis')
		plt.xlabel('Polarity')
		plt.ylabel('Subjectivity')
		plt.savefig('./report/subjectivity.png', bbox_inches='tight')
		plt.clf()

		plt.title('Sentiment Analysis')
		plt.xlabel('Sentiment')
		plt.ylabel('Counts')
		self.df['Analysis'].value_counts().plot(kind='bar')
		plt.savefig('./report/analysis.png', bbox_inches='tight')
		plt.clf()

	def get_resume(self):
		"""
		Returns the value counts and percentages of the tweets analysis.
		"""

		# Get the percentage of positive tweets
		ntweets = self.df[self.df.Analysis == 'Positive']
		ntweets = ntweets['Tweets']

		percentage_positive = round((ntweets.shape[0] / self.df.shape[0] * 100), 1)

		# Get the percentage of negative tweets
		ntweets = self.df[self.df.Analysis == 'Negative']
		ntweets = ntweets['Tweets']

		percentage_negative = round((ntweets.shape[0] / self.df.shape[0] * 100), 1)

		# Value counts
		return(dict(self.df['Analysis'].value_counts()), percentage_positive, percentage_negative)