from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from database import get_friends, get_total_friends, delete_all_friends
from kivy.uix.label import Label
# Load the KV file
Builder.load_file('friendlist/friendlist.kv')
Window.clearcolor = (1, 0, 1, 1)

class LineWidget(BoxLayout):
    pass

class FriendListScreen(Screen):
    total_friends = NumericProperty(45)
    def on_pre_enter(self):
        self.total_friends = get_total_friends()  # Set the property before entering the screen

    def on_enter(self):
        self.populate_friends()
    def now_delete(self):
        delete_all_friends()  # Call the function to delete all friends
        self.total_friends = get_total_friends()

    def populate_friends(self):
        friends = get_friends()
        self.ids.friends_container.clear_widgets()
        if friends:
            for friend in friends:
                friend_name = f"{friend[1]} (ID: {friend[0]:04})"
                # Create a LineWidget
                line_widget = LineWidget()
                # Create a Label for the friend's name
                name_label = Label(text=friend_name, color=(0,0,0,1),
                                   size_hint_y=None,
                                   height=50,
                                   font_size='12sp')
                # Add the LineWidget and Label to the container
                self.ids.friends_container.add_widget(line_widget)
                self.ids.friends_container.add_widget(name_label)
        else:
            self.ids.friends_container.add_widget(Label(text="No friends found."))

