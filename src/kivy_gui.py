from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
import threading
import re
import json
from twitter import TwitterAnalyzer
from wiki import Wikipedia
from exceptions import *

class KivyApp(App):
    def build(self):
        self.language = 'English'
        #returns a window object with all it's widgets
        self.title = "Twitter Sentiment Analysis"
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # Welcome label
        self.welcome = Label(
                       text = "Welcome to Twitter Sentiment Analyzer!",
                       font_size = 18,
                       color = '#00FFCE')

        self.window.add_widget(self.welcome)

        # Image Widget
        self.window.add_widget(Image(source="../img/sentiment.jpeg", size_hint_y=3))

        # Question label
        self.question = Label(
                        text= "Are you ready to start with your new analysis?",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.question)

        # Button widget
        self.button = Button(
                      text= "LET'S GO!",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback_start_button)
        self.window.add_widget(self.button)

        return self.window

    def callback_start_button(self, instance):
        # Clear all previous widgets
        self.window.clear_widgets()

        # Image Widget
        self.window.add_widget(Image(source="../img/cloud.jpg", size_hint_x=1))

        # Topic label
        self.topic = Label(
                       text = "Please insert the topic to analyze",
                       font_size = 18,
                       color = '#00FFCE',
                       size_hint_y = 0.2)

        self.window.add_widget(self.topic)

        # Topic input widget
        self.topic_input = TextInput(
                     hint_text = "Topic",
                     multiline = False,
                     size_hint_y = 0.1
                     )

        self.window.add_widget(self.topic_input)

        # Button widget
        self.button = Button(
                      text= "TELL ME SOMETHING!",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback_analyze_button)
        self.window.add_widget(self.button)

    def callback_analyze_button(self, instance):
        try:
            # Check if topic is empty
            if not self.topic_input.text:
                raise EmptyTopicError('Topic cannot be empty')

            wiki = Wikipedia()
            article = wiki.get_article(self.topic_input.text)
            self.topic_query = self.topic_input.text

            # Clear all previous widgets
            self.window.clear_widgets()

            # Image Widget
            self.window.add_widget(Image(source="../img/wikipedia.png", size_hint_x=0.4))

            if not article:
                article = "Wikipedia couldn't find or redirect to the topic you are looking for."
            # Topic label
            self.topic = Label(
                           text = article,
                           text_size = (self.window.width, None),
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint_x = 0.8)

            self.window.add_widget(self.topic)

            # Button widget
            self.button = Button(
                          text= "LET'S GO ANALYZE!",
                          size_hint_y = 0.2,
                          bold= True,
                          background_color ='#00FFCE',
                          )
            self.button.bind(on_press=self.callback_settings)
            self.window.add_widget(self.button)
     
        except EmptyTopicError:
            # Mark topic hint in red
            self.topic_input.text = ""
            self.topic_input.hint_text = "Topic cannot be empty"
            self.topic_input.hint_text_color = "#FF0000"

    def callback_settings(self, instance):
        # Clear all previous widgets
        self.window.clear_widgets()

        # Show loading screen
        self.window.add_widget(Image(source="../img/gears.gif", anim_delay=0.1, size_hint_y = 0.4))

        # Number of items label
        self.num_items = Label(
                       text = "Please insert the number of tweets you want to analyze",
                       font_size = 18,
                       color = '#00FFCE',
                       size_hint_y = 0.1)

        self.window.add_widget(self.num_items)

        # Number of items input widget
        self.num_items_input = TextInput(
                     hint_text = "Number of tweets",
                     multiline = False,
                     size_hint_y = 0.1
                     )

        self.window.add_widget(self.num_items_input)

        # Language label
        self.lang = Label(
                       text = "Please select the language to use for the analysis",
                       font_size = 18,
                       color = '#00FFCE',
                       size_hint_y = 0.1)

        self.window.add_widget(self.lang)

        self.btn1 = ToggleButton(text='Spanish', group='lang', state='down', size_hint_y = 0.1)
        self.btn2 = ToggleButton(text='English', group='lang', size_hint_y = 0.1)

        self.btn1.bind(on_press=self.callback_language)
        self.btn2.bind(on_press=self.callback_language)

        self.window.add_widget(self.btn1)
        self.window.add_widget(self.btn2)

        # Button widget
        self.button = Button(
                      text= "ANALYZE!",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback_analyze_check)
        self.window.add_widget(self.button)


    def callback_language(self, value):
        self.language = value.text

    def callback_analyze_check(self, instance):
        try:
            # Check if topic is empty
            if not self.topic_input.text:
                raise EmptyTopicError('Topic cannot be empty')

            # Save number of tweets to analyze
            self.num_items = int(self.num_items_input.text)          

            # Clear all previous widgets
            self.window.clear_widgets()

            # Start analysis in another thread 2 seconds later
            threading.Timer(2, self.callback_analyze).start()

            # Show loading screen
            target=self.window.add_widget(Image(source="../img/loading.gif", anim_delay=0.12))
     
        except EmptyTopicError:
            # Mark topic hint in red
            self.topic_input.text = ""
            self.topic_input.hint_text = "Topic cannot be empty"
            self.topic_input.hint_text_color = "#FF0000"

        except ValueError:
            # Mark num_items hint in red
            self.num_items_input.text = ""
            self.num_items_input.hint_text = "Number of tweets must be an integer"
            self.num_items_input.hint_text_color = "#FF0000"

    def callback_analyze(self):
        # Start analyze
        self.analyzer = TwitterAnalyzer()
        self.analyzer.analyze(self.topic_query, self.num_items, self.language)

        self.callback_menu(None)

    def callback_menu(self, instance):

        # Clear all previous widgets
        self.window.clear_widgets()

        # Button widget
        self.button_popular = Button(
                      text= "Popular tweets",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button_popular.bind(on_press=self.callback_popular)
        self.window.add_widget(self.button_popular)

        # Button widget
        self.button_wordcloud = Button(
                      text= "Word Cloud",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button_wordcloud.bind(on_press=self.callback_wordcloud)
        self.window.add_widget(self.button_wordcloud)

        # Button widget
        self.button_subjectivity = Button(
                      text= "Polarity - Subjectivity",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button_subjectivity.bind(on_press=self.callback_subjectivity)
        self.window.add_widget(self.button_subjectivity)

        # Button widget
        self.button_analysis = Button(
                      text= "Polarity analysis",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button_analysis.bind(on_press=self.callback_analysis)
        self.window.add_widget(self.button_analysis)

        # Button widget
        self.button_results = Button(
                      text= "Results and stats",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button_results.bind(on_press=self.callback_results)
        self.window.add_widget(self.button_results)

    def callback_popular(self, instance):
        # Clear all previous widgets
        self.window.clear_widgets()

        # Get popular tweets
        popular_tweets = self.analyzer.get_popular_tweets(self.topic_query)

        count = 1

        popular_text = ''

        for tweet in popular_tweets:
            popular_text = popular_text + str(count) + '. ' + tweet._json["user"]["name"] + ' - ' + tweet._json["user"]["screen_name"] + ': ' + tweet._json["full_text"] + '.\nRT: ' + str(tweet._json["retweet_count"]) + '. FAV: ' + str(tweet._json["favorite_count"]) + '.\n\n'
            count += 1

        # Popular label
        self.popular = Label(
                       text = 'POPULAR TWEETS',
                       font_size = 18,
                       color = '#00FFCE',
                       size_hint_y = 0.2)

        self.window.add_widget(self.popular)

        # Count label
        self.popular_tweets = Label(
                       text = popular_text,
                       font_size = 15,
                       color = '#00FFCE',
                       text_size = (self.window.width, None),
                       size_hint_y = 0.7)

        self.window.add_widget(self.popular_tweets)

        # Button widget
        self.button = Button(
                      text= "Go Back",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback_menu)
        self.window.add_widget(self.button)

    def callback_wordcloud(self, instance):
        # Clear all previous widgets
        self.window.clear_widgets()
        # Image Widget
        self.window.add_widget(Image(source="../report/wordcloud.png", size_hint_x=1))

        # Button widget
        self.button = Button(
                      text= "Go Back",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback_menu)
        self.window.add_widget(self.button)

    def callback_subjectivity(self, instance):
        # Clear all previous widgets
        self.window.clear_widgets()
        # Image Widget
        self.window.add_widget(Image(source="../report/subjectivity.png", size_hint_x=1))

        # Button widget
        self.button = Button(
                      text= "Go Back",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback_menu)
        self.window.add_widget(self.button)

    def callback_analysis(self, instance):
        # Clear all previous widgets
        self.window.clear_widgets()
        # Image Widget
        self.window.add_widget(Image(source="../report/analysis.png", size_hint_x=1))

        # Button widget
        self.button = Button(
                      text= "Go Back",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback_menu)
        self.window.add_widget(self.button)

    def callback_results(self, instance):
        # Clear all previous widgets
        self.window.clear_widgets()
        # Image Widget
        #print('Positive percentage: ' + str(percentage_positive) + '%')
        #print('Negative percentage: ' + str(percentage_negative) + '%')

        counts, positive, negative = self.analyzer.get_resume()

        # Count label
        self.stats = Label(
                       text = 'STATS',
                       font_size = 18,
                       color = '#00FFCE',
                       size_hint_y = 0.1)

        self.window.add_widget(self.stats)

        counts_text = ''

        for key in counts:
            counts_text = counts_text + key + ': ' + str(counts[key]) + '\n'

        counts_text += f'\nPositive percentage: {str(positive)} %\nNegative percentage: {str(negative)} %'

        # Count label
        self.counts = Label(
                       text = counts_text,
                       font_size = 18,
                       color = '#00FFCE',
                       size_hint_y = 0.2)

        self.window.add_widget(self.counts)

        # Positive label
        self.positive = Label(
                       text = f'CONCLUSION',
                       font_size = 18,
                       color = '#00FFCE',
                       size_hint_y = 0.2)

        self.window.add_widget(self.positive)

        # Image Widget
        if (positive - negative) >= 15:
            # Positive opinion
            source = "../img/positive.png"
        elif (positive - negative) <= -15:
            # Negative opinion
            source = "../img/negative.png"
        else:
            # Neutral opinion
            source = "../img/neutral.png"

        self.window.add_widget(Image(source=source, size_hint_y=0.4))

        # Button widget
        self.button = Button(
                      text= "Go Back",
                      size_hint_y = 0.1,
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback_menu)
        self.window.add_widget(self.button)


# run Say Hello App Calss
if __name__ == "__main__":
    KivyApp().run()