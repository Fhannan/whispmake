from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from welcome.welcome import WelcomeScreen
from friendadd.friendadd import FriendAddScreen
from friendlist.friendlist import FriendListScreen
from kivy.core.window import Window
from database import create_table
#from database import delete_all_friends # Import the database function
Window.size = (310,580)
Window.clearcolor =  (1,0,0,1)
Window.left = 1
class MyScreenManager(ScreenManager):
    pass
class MyApp(MDApp):
    def build(self):
        create_table()
        #delete_all_friends()
        sm = MyScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(FriendAddScreen(name='friendadd'))
        sm.add_widget(FriendListScreen(name='friendlist'))
        return sm

if __name__ == '__main__':
    MyApp().run()
