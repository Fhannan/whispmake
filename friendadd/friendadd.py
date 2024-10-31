from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from database import add_friend
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField


# Load the KV file
Builder.load_file('friendadd/friendadd.kv')
Window.clearcolor = (1, 0, 1, 1)

class LineWidget(BoxLayout):
    pass
class FriendAddScreen(Screen):
    friend_name = StringProperty('')  # Property for the name input

    def add_friend_to_db(self):
        name = self.ids.friend_name.text  # Assuming this is your input field for name

        if name:  # Check if the name field is not empty
            add_friend(name, '', '', '', '', '')  # Insert only name; other fields are left blank
            print(f"Added friend with Name: {name}")
            self.clear_fields()  # Clear the input field after adding
        else:
            print("Name field cannot be empty.")

    def clear_fields(self):
        self.ids.friend_name.text = ''



