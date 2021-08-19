# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class Wikipedia():

	def get_article(self, source: str):
		# Parse source for url
		source = '_'.join([word.capitalize() for word in source.split()])
		try:
			# Specify url of the web page
			source = urlopen(f'https://es.wikipedia.org/wiki/{source}').read()

			# Make a soup
			soup = BeautifulSoup(source,'lxml')
			soup

			# Extract the plain text content from paragraphs
			paras = []
			for paragraph in soup.find_all('p'):
			    paras.append(str(paragraph.text))

			# Extract text from paragraph headers
			heads = []
			for head in soup.find_all('span', attrs={'mw-headline'}):
			    heads.append(str(head.text))

			# Interleave paragraphs & headers
			text = [val for pair in zip(paras, heads) for val in pair]
			text = ' '.join(text)

			# Drop footnote superscripts in brackets
			text = re.sub(r"\[.*?\]+", '', text)

			# Replace '\n' (a new line) with '' and end the string at $1000.
			text = text.split('\n')
			if not text[0]:
				raise ValueError('Empty search')

			return text[0]
		except:
			return