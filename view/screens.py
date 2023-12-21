from controller.MainScreen.main_screen import MainScreenController
from model.default import DefaultNonModelObject
from controller.LandingScreen.landing_screen import LandingScreenController


screens = {
    'LandingScreen': {
        'model': DefaultNonModelObject,
        'controller': LandingScreenController,
    },
    'MainScreen': {
        'model': DefaultNonModelObject,
        'controller': MainScreenController,
    },
}
