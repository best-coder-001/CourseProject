from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class BaseInputBox(MDBoxLayout):
    controller = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_fields()

    def load_fields(self):
        self.ids.field_wrapper.clear_widgets()
        for key, value in self.controller.json_field_names().items():
            self.ids.field_wrapper.add_widget(MDTextField(id=key, hint_text=value, mode='rectangle'))

    def get_data(self):
        return dict([(i.id, i.text) for i in self.ids.field_wrapper.children])


class BaseInputDialog:
    def __init__(self, controller, title=None, text=None):
        self.controller = controller
        self.dialog = MDDialog(
            type='custom',
            content_cls=BaseInputBox(controller=self.controller),
            buttons=[
                MDFlatButton(text='ЗАКРЫТЬ', on_release=self.close),
                MDFlatButton(text='ДОБАВИТЬ', on_release=self.on_release_add)
            ]
        )

    def open(self):
        self.dialog.open()

    def close(self, obj):
        self.dialog.dismiss()

    def on_release_add(self, obj):
        self.controller.insert(self.dialog.content_cls.get_data())


class BaseUpdateInputBox(MDBoxLayout):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller


class BaseInputScreen(MDBoxLayout):
    def __init__(self,controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller
        

class BaseUpdateInputDialog:
    def __init__(self, controller, title=None, text=None):
        self.controller = controller
        self.dialog = MDDialog(
            type='custom',
            content_cls=BaseUpdateInputBox(controller=self.controller),
            buttons=[
                MDFlatButton(text='ЗАКРЫТЬ', on_release=self.close),
            ]
        )

    def open(self):
        self.dialog.open()

    def close(self, obj):
        self.dialog.dismiss()