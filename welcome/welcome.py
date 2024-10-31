from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Load the KV file
Builder.load_file('welcome/welcome.kv')

class WelcomeScreen(Screen):
    pass
