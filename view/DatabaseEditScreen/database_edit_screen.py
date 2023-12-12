from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty


class DatabaseEditScreen(MDScreen):
    model = ObjectProperty()
    controller = ObjectProperty()
    manager_screens = ObjectProperty()
