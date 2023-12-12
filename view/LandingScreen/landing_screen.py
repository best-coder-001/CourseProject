from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty


class LandingScreen(MDScreen):
    model = ObjectProperty()
    controller = ObjectProperty()
    manager_screens = ObjectProperty()
