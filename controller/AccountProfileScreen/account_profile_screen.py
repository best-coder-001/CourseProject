from view.AccountProfileScreen.account_profile_screen import AccountProfileScreen


class AccountProfileScreenController:
    def __init__(self,model):
        self.model = model
        self.view = AccountProfileScreen(controller=self,model=self.model)

    def get_view(self):
        return self.view