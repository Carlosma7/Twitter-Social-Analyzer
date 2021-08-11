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

# Obtener información de .env
load_dotenv(dotenv_path = '.env')

# Authentication tokens
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Tweepy Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Create nlp object
nlp = spacy.load('es_core_news_sm')

# Clean text from tweets to get main info
def clean_txt(tweet: str):
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
def get_subjectivity(tweet: str):
	return TextBlob(tweet).sentiment.subjectivity

# Get the polarity of tweet
def get_polarity(tweet: str):
	return TextBlob(tweet).sentiment.polarity

# Get the positive, negative or neutral analysis
def get_analysis(score: float):
	if score < 0:
		return 'Negative'
	elif score == 0:
		return 'Neutral'
	else:
		return 'Positive'

def print_popular_tweet(topic: str, num_items: int):
	for tweet in tweepy.Cursor(api.search, q=topic, result_type="popular", tweet_mode="extended").items(num_items):
		print('------------------------------------------------')
		print("TWEET:" + tweet._json["full_text"])
		print("USER:" + tweet._json["user"]["name"] + ' - ' + tweet._json["user"]["screen_name"])
		print("RT:" + str(tweet._json["retweet_count"]))
		print("FAV:" + str(tweet._json["favorite_count"]))
		print('------------------------------------------------')
		print('\n\n\n\n')

def get_tweets(topic: str, num_items: int):
	return [tweet._json["full_text"] for tweet in tweepy.Cursor(api.search, q=topic, tweet_mode="extended").items(num_items)]

def get_lexical_tokens(tweet: str):
	doc = nlp(tweet)

	lexical_tokens = [t.orth_ for t in doc if not t.is_punct | t.is_stop]
	return ' '.join(lexical_tokens)

# Create a dataframe with a column called Tweets
df = pd.DataFrame(get_tweets('vizkyconzeta', 10000), columns=['Tweets'])

# Apply clean text
df['Tweets'] = df['Tweets'].apply(clean_txt)

# Define subjectivity and polarity of tweets
df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
df['Polarity'] = df['Tweets'].apply(get_polarity)

# Apply NLP
df['Lexical'] = df['Tweets'].apply(get_lexical_tokens)

# Plot the word cloud
allWords = ' '.join([tweets for tweets in df['Lexical']])
wordCloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 119).generate(allWords)

plt.imshow(wordCloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()

# Get the analysis value
df['Analysis'] = df['Polarity'].apply(get_analysis)

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