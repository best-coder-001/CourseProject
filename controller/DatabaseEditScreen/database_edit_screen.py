from view.DatabaseEditScreen.database_edit_screen import DatabaseEditScreen


class DatabaseEditScreenController:
    def __init__(self, model):
        self.model = model
        self.view = DatabaseEditScreen(controller=self, model=self.model)

    def get_view(self):
        return self.view
