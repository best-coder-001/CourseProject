from view.LandingScreen.landing_screen import LandingScreen
from view.LandingScreen.screens import screens


class LandingScreenController:
    def __init__(self, model):
        self.model = model
        self.view = LandingScreen(controller=self, model=self.model)
        self.manager_landing_screens = self.view.ids.landing_screen_manager

    def get_view(self):
        return self.view

    def generate_landing_screens(self):
        self.manager_landing_screens.clear_widgets()
        for screen in screens.keys():
            model = screens[screen]['model']()
            controller = screens[screen]['controller'](model=model)
            view = controller.get_view()
            view.name = screen
            view.manager_screens = self.view.manager_screens
            view.landing_screens_manager = self.manager_landing_screens
            self.manager_landing_screens.add_widget(view)

    def change_screens(self,name):
        self.manager_landing_screens.current = name
