from kivymd.uix.dialog import MDDialog
from view.MainScreen.components.SignUpScreen.sign_up_screen import SignUpScreen
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
        flag = self.model.check_logged(**data)

        if flag:
            self.show_dialog_fail()
        else:
            try:
                callback = self.validate_fields(**data)
                for name in callback.keys():
                    if not callback[name]:
                        raise Exception()
            except:
                self.validation_fail_dialog()
            else:
                self.model.append_user(**data)
                self.show_dialog_success()
                self.view.manager_screens.current = 'LandingScreen'

    def show_dialog_success(self):
        if not self.dialog:
            self.dialog = MDDialog(title='Успешная регистрация',
                                   text='Регистрация была успешно произведена!'
                                   )
        self.dialog.open()

    def show_dialog_fail(self):
        if not self.dialog:
            self.dialog = MDDialog(title='Ошибка регистрации',
                                   text='Что то пошло не так,такой пользователь уже существует!'
                                   )
        self.dialog.open()

    def validate_fields(self, **kw):
        callback = {
            'username': False,
            'password': False,
            'email': False,
            'phone_number': False
        }
        if len(kw['username']) >= 5:
            callback['username'] = True

        if len(kw['password']) >= 8:
            callback['password'] = True

        if self.validate_email(kw['email']):
            callback['email'] = True

        if self.validate_phone_number(kw['phone_number']):
            callback['phone_number'] = True

        return callback

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        else:
            return False

    def validate_phone_number(self, phone_number):
        pattern = r'^(?:\+7|8)-\d{3}-\d{3}-\d{4}$'
        if re.match(pattern, phone_number):
            return True
        else:
            return False

    def validation_fail_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(title='Неправильно введеные данные',
                                   text='Что то пошло не так,в какое то поле были введены неправильные данные!'
                                   )
        self.dialog.open()
