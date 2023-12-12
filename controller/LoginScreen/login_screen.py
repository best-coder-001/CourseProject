from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog.dialog import MDDialog
from view.MainScreen.components.LoginScreen.login_screen import LoginScreen


class LoginScreenController:
    def __init__(self, model):
        self.model = model
        self.view = LoginScreen(controller=self, model=self.model)
        self.dialog = None

    def get_view(self):
        return self.view

    def show_fail_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Ошибка логина',
                text='произошла ошибка авторизации, возможно были введены неправильные данные',
            )
        self.dialog.open()

    def login(self):
        data = {'username': self.view.ids.username.text, 'password': self.view.ids.password.text}
        print(data)
        flag = self.model.check_logged(**data)
        if flag:
            self.view.manager_screens.current = 'LandingScreen'
        else:
            self.show_fail_dialog()

