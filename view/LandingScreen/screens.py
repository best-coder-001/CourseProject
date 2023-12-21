from controller.SettingsScreen.settings_screen import SettingsScreenController
from controller.DatabaseEditScreen.database_edit_screen import DatabaseEditScreenController
from controller.AccountProfileScreen.account_profile_screen import AccountProfileScreenController
from model.default import DefaultNonModelObject

screens = {
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