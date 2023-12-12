from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen


class SignUpScreen(MDScreen):
    model = ObjectProperty()
    controller = ObjectProperty()
    manager_screens = ObjectProperty()
    auth_screens_manager = ObjectProperty()