from kivymd.uix.screenmanager import MDScreenManager

from view.DatabaseEditScreen.database_edit_screen import DatabaseEditScreen
from view.DatabaseEditScreen.screens import screens


class DatabaseEditScreenController:
    def __init__(self, model):
        self.model = model
        self.view = DatabaseEditScreen(controller=self, model=self.model)
        self.db_screen_manager = self.view.ids.database_tables

    def get_view(self):
        return self.view

    def generate_screen_slides(self):
        self.db_screen_manager.clear_widgets()
        for name in screens.keys():
            model = screens[name]['model']
            controller = screens[name]['controller'](model=model, view=screens[name]['view'])
            view = controller.get_view()
            view.name = name
            view.manager_screens = self.db_screen_manager
            self.db_screen_manager.add_widget(view)

    def current_screen_name(self):
        self.view.ids.title.text = self.view.ids.database_tables.current

    def screens(self):
        return self.view.ids.database_tables.screens

    def index(self, name):
        for i in range(len(self.screens())):
            if self.screens()[i].name == name:
                return i

    def load_first(self):
        first_screen_name = self.screens()[0].name
        self.view.ids.database_tables.current = first_screen_name

    def load_last(self):
        first_screen_name = self.screens()[::-1].name
        self.view.ids.database_tables.current = first_screen_name

    def load_next(self):
        current_screen_index = self.index(self.view.ids.database_tables.current)
        try:
            next_screen_name = self.screens()[current_screen_index + 1].name
            self.view.ids.database_tables.current = next_screen_name
        except:
            self.load_first()
        finally:
            self.current_screen_name()

    def load_previous(self):
        current_screen_index = self.index(self.view.ids.database_tables.current)
        try:
            previous_screen_name = self.screens()[current_screen_index - 1].name
            self.view.ids.database_tables.current = previous_screen_name
        except:
            self.load_last()
        finally:
            self.current_screen_name()
