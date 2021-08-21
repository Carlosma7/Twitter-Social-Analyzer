# Kivy_gui module

> _class_ **kivy_gui.KivyApp**_(**kwargs)_

Bases: ```kivy.app.App```

GUI App that contains all the Twitter Analyzer service.

| [build()](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L21) |
| --------------------------------------------------------------------------------------------------------------------------------- |

> [build()](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L21)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Creates the initial window and print a welcome message. Returns the apps window.

| [callback_analysis(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L422) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Defines a new window with the sentiments bar plot.

| [callback_analyze()](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L260) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set the parameters and start the analysis. Calls the menu window.

| [callback_analyze_button(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L105) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Checks the previous topic is not empty. Defines a new window with Wikipedia info about the topic.

| [callback_analyze_check(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L224) |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Checks if settings inputs aren’t empty and if number of tweets is an integer. Defines a new window with a loading screen and throws a thread with the Twitter Analysis.

| [callback_language(value)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L216) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes value of the new language. Sets the new language.

| [callback_menu(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L272) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Defines a new window with a button menu for the different parts of the analysis.

| [callback_popular(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L331) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Defines a new window with most popular tweets about the topic.

| [callback_results(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L443) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Defines a new window with the stats and conclusion.

| [callback_settings(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L157) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Defines a new window with the analysis settings inputs.

| [callback_start_button(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L65) |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Defines a new window with a topic input.

| [callback_subjectivity(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L401) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Defines a new window with the tweets subjectivity-polarity graph.

| [callback_wordcloud(instance)](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/263815707f330b05dce8b60841b8a55fcc1d6495/src/kivy_gui.py#L380) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Takes the button callback instance. Defines a new window with a word cloud associated to the topic.


| [< Previous](https://carlosma7.github.io/Twitter-Social-Analyzer/doc/exceptions) | [Next >](https://carlosma7.github.io/Twitter-Social-Analyzer/doc/twitter) |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------|