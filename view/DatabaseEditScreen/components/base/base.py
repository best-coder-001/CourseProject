from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty


class BaseModelScreen(MDScreen):
    model = ObjectProperty()
    controller = ObjectProperty()
    manager_screens = ObjectProperty()

    def on_enter(self, *args):
        self.controller.on_enter()

