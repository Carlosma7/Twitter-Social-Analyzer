from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
import threading
from twitter import TwitterAnalyzer
from exceptions import *

class KivyApp(App):
    def build(self):
        self.language = 'English'
        #returns a window object with all it's widgets
        self.title = "Twitter Sentiment Analysis"
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # Welcome label
        self.welcome = Label(
                       text = "Welcome to Twitter Sentiment Analyzer!",
                       font_size = 18,
                       color = '#00FFCE')

        self.window.add_widget(self.welcome)

        # Image Widget
        self.window.add_widget(Image(source="../img/sentiment.jpeg"))

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

        # Topic label
        self.topic = Label(
                       text = "Topic",
                       font_size = 18,
                       color = '#00FFCE')

        self.window.add_widget(self.topic)

        # Topic input widget
        self.topic_input = TextInput(
                     hint_text = "Topic",
                     multiline = False,
                     size_hint = (1, 0.5)
                     )

        self.window.add_widget(self.topic_input)

        # Number of items label
        self.num_items = Label(
                       text = "Tweets",
                       font_size = 18,
                       color = '#00FFCE')

        self.window.add_widget(self.num_items)

        # Number of items input widget
        self.num_items_input = TextInput(
                     hint_text = "Number of tweets",
                     multiline = False,
                     size_hint = (1, 0.5)
                     )

        self.window.add_widget(self.num_items_input)

        # Language label
        self.lang = Label(
                       text = "Language",
                       font_size = 18,
                       color = '#00FFCE')

        self.window.add_widget(self.lang)

        self.btn1 = ToggleButton(text='Spanish', group='lang', size_hint= (1,0.5))
        self.btn2 = ToggleButton(text='English', group='lang', state='down', size_hint= (1,0.5))

        self.btn1.bind(on_press=self.callback_language)
        self.btn2.bind(on_press=self.callback_language)

        self.window.add_widget(self.btn1)
        self.window.add_widget(self.btn2)

        # Button widget
        self.button = Button(
                      text= "ANALYZE!",
                      size_hint= (1,0.5),
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
                raise EmptyError('Topic cannot be empty')

            # Save number of tweets to analyze
            self.num_items = int(self.num_items_input.text)          

            # Clear all previous widgets
            self.window.clear_widgets()

            # Start analysis in another thread 2 seconds later
            threading.Timer(2, self.callback_analyze).start()

            # Show loading screen
            target=self.window.add_widget(Image(source="../img/loading.gif", anim_delay=0.05))
     
        except EmptyError:
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
        analyzer = TwitterAnalyzer()
        analyzer.analyze(self.topic_input.text, self.num_items, self.language)

        # Clear all previous widgets
        self.window.clear_widgets()

        # Finished label
        self.finished = Label(
                       text = "Finished",
                       font_size = 18,
                       color = '#00FFCE')

        self.window.add_widget(self.finished)


# run Say Hello App Calss
if __name__ == "__main__":
    KivyApp().run()