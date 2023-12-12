from view.LandingScreen.landing_screen import LandingScreen


class LandingScreenController:
    def __init__(self, model):
        self.model = model
        self.view = LandingScreen(controller=self, model=self.model)

    def get_view(self):
        return self.view
