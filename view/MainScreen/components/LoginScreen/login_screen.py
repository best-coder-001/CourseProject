from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty


class LoginScreen(MDScreen):
    model = ObjectProperty()
    controller = ObjectProperty()
    manager_screens = ObjectProperty()
    auth_screens_manager = ObjectProperty()
