from kivymd.material_resources import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.menu import MDDropdownMenu

from model.default import session
from view.DatabaseEditScreen.components.content.content import BaseInputDialog, BaseUpdateInputDialog
from .dialogs.default import ViewDialog
from sqlalchemy import (
    insert, select, delete, update
)
import openpyxl


class BaseModelScreenController:
    db_field_names = []
    prepared_field_names = []
    validator = None

    def __init__(self, model, view):
        self.model = model
        self.view = view(model=self.model, controller=self)
        self.view_dialog = None
        self.input_dialog = None
        self.input_dialog_update = None

    def get_view(self):
        return self.view

    def on_enter(self):
        self.load_table()

    def load_table(self,row_data=None):
        self.tbl = MDDataTable(
            use_pagination=True,
            check=True,
            row_data=self.row_data(),
            column_data=self.column_data(),
        )
        if row_data:
            self.tbl.row_data = row_data
        self.tbl.bind(on_row_press=self.on_row_press)
        self.view.ids.datatable.clear_widgets()
        self.view.ids.datatable.add_widget(self.tbl)

    def table_instance(self):
        for i in self.view.ids.datatable.children:
            if isinstance(i, MDDataTable):
                return i

    def run_dialog(self, **kw):
        self.view_dialog = ViewDialog(**kw)

    def run_input_dialog(self):
        self.input_dialog = BaseInputDialog(controller=self)

    def run_input_dialog_update(self, data):
        self.input_dialog_update = BaseUpdateInputDialog(controller=self, data=data)

    def row_data(self):
        return self.select()

    def column_data(self):
        return [(i, dp(60)) for i in self.prepared_field_names]

    def convert_data(self, data):
        result = []
        for item in data:
            row_data = [getattr(item, field) for field in self.db_field_names]
            result.append(row_data)
        return result

    def validate_data(self, data):
        return self.validator(**data).model_dump()

    def json_field_names(self):
        return dict(zip(self.db_field_names, self.prepared_field_names))

    def select(self):
        try:
            with session.begin():
                return self.convert_data(session.scalars(select(self.model)).all())
        except Exception as e:
            print(e)
            self.run_dialog(title='Предупреждение', msg=f'Ошибка загрузки данных из базы данных')
            self.view_dialog.open()
            return []

    def insert(self, data):
        try:
            validated_data = self.validate_data(data)
            print(validated_data)
            with session.begin():
                session.execute(insert(self.model).values(**validated_data))
            self.load_table()
        except:
            self.run_dialog(title='Предупреждение', msg=f'Не удалось добавить данные,повторите снова')
            self.view_dialog.open()
        else:
            self.run_dialog(title='Информация', msg='Данные успешно добавлены')
            self.view_dialog.open()

    def update(self, row):
        try:
            validated_data = self.validate_data(dict(reversed(row.items())))
            data = dict([(key, value) for key, value in validated_data.items()][1:])
            with session.begin():
                session.execute(update(self.model).where(self.model.id == validated_data['id']).values(**data))
            self.load_table()
        except:
            self.run_dialog(title='Предупреждение', msg=f'Не удалось обновить данные,повторите снова')
            self.view_dialog.open()
        else:
            self.run_dialog(title='Информация', msg='Данные успешно обновлены')
            self.view_dialog.open()

    def delete(self, row_queryset):
        try:
            with session.begin():
                for i in row_queryset:
                    session.execute(delete(self.model).where(self.model.id == i[0]))
            self.load_table()
        except Exception as e:
            self.run_dialog(title='Предупреждение', msg=f'Не удалось удалить данные,повторите снова')
            self.view_dialog.open()
        else:
            self.run_dialog(title='Информация', msg='Данные успешно удалены')
            self.view_dialog.open()

    def on_press_insert(self):
        self.run_input_dialog()
        self.input_dialog.open()

    def on_press_reload(self):
        self.load_table()

    def on_press_delete(self):
        checked_rows = self.table_instance().get_row_checks()
        print(checked_rows)
        if not checked_rows:
            self.run_dialog(title='Информация', msg='Выберите записи которые хотите удалить')
            self.view_dialog.open()
        else:
            self.delete(row_queryset=checked_rows)

    def on_press_dots_vertical(self):
        menu_items = [
            {
                "text": f"Экспорт",
                "viewclass": "OneLineListItem",
                "on_release": lambda: self.export_xlsx(),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.view.ids.export_btn,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def export_xlsx(self):
        file_name = self.view.name
        folder = f'C:\\Users\\User\\OneDrive\\Рабочий стол\\Файлы эксель\\{file_name}.xlsx'
        headers = self.prepared_field_names
        data = self.select()
        try:
            book = openpyxl.Workbook()
            sheet = book.active
            sheet.append(headers)
            for row in data:
                sheet.append(row)
            book.save(folder)
        except:
            self.run_dialog(title='Ошибка', msg='Ошибка экспорта,повторите попытку')
            self.view_dialog.open()
        else:
            self.run_dialog(title='Информация', msg='Данные успешно экспортированы')
            self.view_dialog.open()

    def on_row_press(self, instance_table, instance_row):
        row_num = int(instance_row.index / len(instance_table.column_data))
        row_data = instance_table.row_data[row_num]
        self.run_input_dialog_update(data=row_data)
        self.input_dialog_update.open()

    def search(self, row_id):
        try:
            row_id = int(row_id)
            with session.begin():
                return self.convert_data(session.scalars(select(self.model).where(self.model.id == row_id)))

        except:
            self.run_dialog(title='Информация', msg='Ничего не найдено по данному идентификатору')
            self.view_dialog.open()

    def on_search(self):
        row_id = self.view.ids.search.text
        self.load_table(self.search(row_id))


