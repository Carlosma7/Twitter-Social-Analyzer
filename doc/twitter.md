# Twitter module

> _class_ **twitter.TwitterAnalyzer**

Bases: ```object```

Twitter Sentiment Analyzer that contains a tweepy API. It can search most popular tweets, get subjectivity, polarity and a resume about any topic given.

| [analyze(topic: str, num_items: int, lang: str)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L129) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a topic, a number of tweets and language. Obtains n most recent tweets, applies NLP, generates a word cloud, computes subjectivity and polarity and creates several plots.

| [clean_txt(tweet: str)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L38) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a tweet text. Returns the tweet text without any mention, hashtag, RT or link.

| [get_analysis(score: float))](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L74) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a score from a tweet. Returns the analysis (positive, negative or neutral).

| [get_lexical_tokens(tweet: str)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L118) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a tweet text. Returns just the lexical tokens.

| [get_polarity(tweet: str)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L65) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a tweet text. Returns the polarity.

| [get_popular_tweets(topic: str)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L102) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a topic. Returns the 3 most popular tweets about that topic.

| [get_resume()](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L185) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Returns the value counts and percentages of the tweets analysis.

| [get_subjectivity(tweet: str)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L56) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a tweet text. Returns the subjectivity.

| [get_tweets(topic: str, num_items: int)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L110) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a topic and a number of tweets. Returns the n most recent tweets about that topic.

| [print_popular_tweet(topic: str, num_items: int)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/twitter.py#L87) |
| ------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes a topic and a number of tweets. Prints the n most popular tweets about the topic.


| [< Previous](https://carlosma7.github.io/Twitter-Social-Analyzer/doc/kivy) | [Next >](https://carlosma7.github.io/Twitter-Social-Analyzer/doc/wiki) |
|-----------------------------------|-------------------------------|