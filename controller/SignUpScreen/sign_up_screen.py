from kivymd.uix.dialog import MDDialog
from view.MainScreen.components.SignUpScreen.sign_up_screen import SignUpScreen
from pydantic import ValidationError
import re


class SignUpScreenController:
    def __init__(self, model):
        self.model = model
        self.view = SignUpScreen(controller=self, model=self.model)
        self.dialog = None

    def get_view(self):
        return self.view

    def sign_in_user(self):
        data = {'username': self.view.ids.username.text,
                'password': self.view.ids.password.text,
                'email': self.view.ids.email.text,
                'phone_number': self.view.ids.phone_number.text}
        is_logged = self.model.check_logged(**data)

        if is_logged:
            self.show_dialog(title='Ошибка регистрации', msg='Пользователь с таким аккаунтом уже существует '
                                                             'попробуйте подобрать другие данные!')
        else:
            try:
                self.validate_fields(**data)
            except ValidationError as e:
                text = ','.join([i['msg'].replace('Value error,','') for i in e.errors()]).capitalize()
                self.show_dialog(title='Ошибка валидации', msg=str(text))
            else:
                self.model.append_user(**data)
                self.show_dialog(title='Успешная регистрация', msg='Добро пожаловать!')
                self.view.manager_screens.current = 'LandingScreen'

    def show_dialog(self, title, msg):
        if not self.dialog:
            self.dialog = MDDialog(title=title,
                                   text=msg
                                   )
        self.dialog.open()

    def validate_fields(self, **kw):
        self.model.validate_user_data(**kw)
