
# Twitter Social Analyzer
---

Hi! Welcome to Twitter Social Analyzer!

The main goal of the project is to analyze different tweets about a concrete topic and generate a sentiment analysis about it using NLP tools.

## Table of contents:
---

:medal_sports: [Badges](#badges)

:bird: [Description](#description)

:clapper: [Demo](#demo)

:notebook_with_decorative_cover: [User manual](#user-manual)

:gear: [Install](#install)

:couple: [How to contribute](#how-to-contribute)

:man: [Author](#author)

:copyright: [License](#license)

## Badges
---
**Project**.

[![Language](https://img.shields.io/badge/Language-Python-red.svg)](https://www.python.org/)  [![Twitter](https://img.shields.io/badge/API-Twitter-cyan.svg)](https://twitter.com) [![Tweepy](https://img.shields.io/badge/Framework-Tweepy-cyan.svg)](https://www.tweepy.org/) [![Kivy](https://img.shields.io/badge/GUI-Kivy-black.svg)](https://kivy.org/#home) 

## Description
---

### Project

Twitter Social Analyzer comes up as a personal project that aspires to define a useful and simple tool to extract sentiments about a certain topic on [Twitter](https://twitter.com) social media. It also wants to get (if possible) [Wikipedia](https://es.wikipedia.org) definition about that topic.

For an easy use, it defines a simple GUI using [Kivy](https://kivy.org/#home) for that purpose. The project is designed to contain all the different information and elements into differente and intuitive windows for a simple but comfortable experience.

The main tools used are:
- [Tweepy](https://www.tweepy.org/) for tweets parsing.
- [urllib](https://docs.python.org/3/library/urllib.html) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for Wikipedia info extraction.
- [matplotlib](https://matplotlib.org/) for graph plots.
- [TextBlob](https://textblob.readthedocs.io/en/dev/) for polarity and subjectivity analysis.
- [WordCloud](https://pypi.org/project/wordcloud/) for word cloud plot generation.
- [Spacy](https://spacy.io/) for NLP over tweets text.

### Features

-   Uses a Kivy GUI for an easy interface.
-   Parses most relevant tweets about the topic.
-   Generates a word cloud based on tweets about the topic.
-   Generates a polarity-subjectivity plot.
-   Generates a sentiment value bar plot.
-   Generates a resume with stats from tweets.

## Demo
---

<p align="center"><img src="https://raw.githubusercontent.com/Carlosma7/Twitter-Social-Analyzer/master/img/twitter.gif"/></p>

## User manual
---

Here you can view the official project :books: [docs](https://carlosma7.github.io/Twitter-Social-Analyzer/doc/home) and :notebook_with_decorative_cover: [wiki](https://github.com/Carlosma7/Twitter-Social-Analyzer/wiki) with technical info about the project.
 	
## Install
---

### Download
---

**With** Git.

```shell
git clone https://github.com/Carlosma7/Twitter-Social-Analyzer.git
```

**With** GitHub CLI.

```shell
gh repo clone Carlosma7/Twitter-Social-Analyzer
```

**Without** GitHub.

```shell
wget https://github.com/carlosma7/Twitter-Social-Analyzer/archive/main.zip
```

### Dependencies
---

To install all dependencies just execute:

```shell
pip3 install -r requirements.txt
```

## How to contribute
---
**Twitter Social Analyzer** is an open source project that is open for new contributions if you want to. To contribute to the project you can [contact me](#author) or just open a new *pull request*. Thanks in advance!

## Author
---

**Carlos Morales Aguilera**

![Carlos](https://avatars.githubusercontent.com/u/14914668?v=4)

:octocat: [GitHub](https://github.com/Carlosma7)
:email: [Email](carlos7ma@gmail.com)
:busts_in_silhouette: [LinkedIn](https://www.linkedin.com/in/carlos-morales-aguilera/)

## License 
---
[LICENSE](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/main/LICENSE)

**GPLv3**: The permissions under this strong copyleft license are conditional on making the full source code of the licensed works and modifications, including larger works using a licensed work, available under the same license. Copyright and licensing notices should be retained. Taxpayers provide an express grant of patent rights.

**Permissions**:

* Commercial use.
* Distribution.
* Modification.
* Use of patent.
* Private use.

**Conditions**:

* Reveal source.
* License and copyright notice.
* Same license.
* State changes.

**Limitations**:

* Responsibility.
* Warranty.
