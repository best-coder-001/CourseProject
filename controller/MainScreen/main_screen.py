from view.MainScreen.components.screens import screens
from view.MainScreen.main_screen import MainScreen


class MainScreenController:
    def __init__(self,model):
        self.model = model
        self.view = MainScreen(controller=self,model=self.model)
        self.auth_screens = self.view.ids.auth_screens

    def get_view(self):
        return self.view

    def generate_auth_screens(self):
        self.auth_screens.clear_widgets()
        for screen in screens.keys():
            model = screens[screen]['model']()
            controller = screens[screen]['controller'](model=model)
            view = controller.get_view()
            view.name = screen
            view.manager_screens = self.view.manager_screens
            view.auth_screens_manager = self.auth_screens
            self.auth_screens.add_widget(view)

