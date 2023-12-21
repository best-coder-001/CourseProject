from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty, StringProperty


class DatabaseEditScreen(MDScreen):
    model = ObjectProperty()
    controller = ObjectProperty()
    manager_screens = ObjectProperty()
    title = StringProperty()

    def on_enter(self, *args):
        self.controller.generate_screen_slides()
        self.controller.current_screen_name()
