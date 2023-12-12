from controller.MainScreen.main_screen import MainScreenController
from model.default import DefaultNonModelObject

from controller.LandingScreen.landing_screen import LandingScreenController
from controller.SettingsScreen.settings_screen import SettingsScreenController
from controller.DatabaseEditScreen.database_edit_screen import DatabaseEditScreenController
from controller.AccountProfileScreen.account_profile_screen import AccountProfileScreenController

screens = {
    'LandingScreen': {
        'model': DefaultNonModelObject,
        'controller': LandingScreenController
    },
    'MainScreen': {
        'model': DefaultNonModelObject,
        'controller': MainScreenController,
    },
    'AccountProfileScreen': {
        'model': DefaultNonModelObject,
        'controller': AccountProfileScreenController
    },
    'DatabaseEditScreen': {
        'model': DefaultNonModelObject,
        'controller': DatabaseEditScreenController
    },
    'SettingsScreen': {
        'model': DefaultNonModelObject,
        'controller': SettingsScreenController
    }
}
