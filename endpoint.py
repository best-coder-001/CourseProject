from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from view.screens import screens
from kivy.resources import resource_add_path
from kivy.core.text import LabelBase

resource_add_path('assets/images/')


class CourseProjectConceptApp(MDApp):
    def __init__(self, **kw):
        self.load_all_kv_files('view/')
        super().__init__(**kw)
        self.screen_manager = MDScreenManager()

    def build(self):
        self.load_fonts()
        self.generate_app_screens()
        return self.screen_manager

    def generate_app_screens(self):
        for screen in screens.keys():
            model = screens[screen]['model']()
            controller = screens[screen]['controller'](model=model)
            view = controller.get_view()
            view.name = screen
            view.manager_screens = self.screen_manager
            self.screen_manager.add_widget(view)

    def change_screens(self, screen):
        if self.screen_manager.current == screen:
            ...
        else:
            self.screen_manager.current = screen

    def load_fonts(self):
        LabelBase.register(name='bubble_words',fn_regular='assets/fonts/Rubik_Bubbles/RubikBubbles-Regular.ttf')


if __name__ == '__main__':
    CourseProjectConceptApp().run()
