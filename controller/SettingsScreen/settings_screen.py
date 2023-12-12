from view.SettingsScreen.settings_screen import SettingsScreen


class SettingsScreenController:
    def __init__(self, model):
        self.model = model
        self.view = SettingsScreen(controller=self, model=self.model)

    def get_view(self):
        return self.view
