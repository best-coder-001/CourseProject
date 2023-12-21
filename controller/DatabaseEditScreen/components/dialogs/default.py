from kivymd.uix.dialog.dialog import MDDialog


class ViewDialog:
    def __init__(self, title, msg):
        self.dialog = MDDialog(title=title, text=msg)

    def close(self):
        self.dialog.close()

    def open(self):
        self.dialog.open()
