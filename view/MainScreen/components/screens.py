from model.users.user_model import UserModel
from controller.SignUpScreen.sign_up_screen import SignUpScreenController
from controller.LoginScreen.login_screen import LoginScreenController

screens = {
    'LoginScreen': {
        'model': UserModel,
        'controller': LoginScreenController
    },
    'SignUpScreen': {
        'model': UserModel,
        'controller': SignUpScreenController
    }
}