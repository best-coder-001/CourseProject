from controller.DatabaseEditScreen.components.base import BaseModelScreenController
from utils.validators import *


class DepartamentScreenController(BaseModelScreenController):
    db_field_names = ['id', 'name']
    prepared_field_names = ['Идентификатор', 'Наименование']
    validator = DepartamentValidator


class GroupScreenController(BaseModelScreenController):
    db_field_names = ['id', 'name', 'department_id', 'size']
    prepared_field_names = ['Идентификатор', 'Наименование', 'Код кафедры', 'Количество']
    validator = GroupValidator


class TeacherScreenController(BaseModelScreenController):
    db_field_names = ['id', 'name', 'department_id']
    prepared_field_names = ['Идентификатор', 'ФИО', 'Код кафедры']
    validator = TeacherValidator


class SubjectScreenController(BaseModelScreenController):
    db_field_names = ['id', 'name']
    prepared_field_names = ['Идентификатор', 'Наименование']
    validator = SubjectValidator


class ClassPeriodScreenController(BaseModelScreenController):
    db_field_names = ['id', 'period_number', 'start_time', 'end_time']
    prepared_field_names = ['Идентификатор', 'Номер пары', 'Время начала', 'Время окончания']
    validator = ClassPeriodValidator


class ClassTypeScreenController(BaseModelScreenController):
    db_field_names = ['id', 'name']
    prepared_field_names = ['Идентификатор', 'Наименование']
    validator = ClassTypeValidator


class ClassroomScreenController(BaseModelScreenController):
    db_field_names = ['id', 'classroom_number', 'class_type_id', 'capacity']
    prepared_field_names = ['Идентификатор', 'Номер аудитории','Код типа занятости','Количество мест']
    validator = ClassroomValidator


class ScheduleScreenController(BaseModelScreenController):
    db_field_names = ['id', 'is_numerator', 'day_of_week', 'period_id', 'group_id',
                      'subject_id', 'class_type_id', 'classroom_number', 'teacher_id']
    prepared_field_names = ['Идентификатор', 'Числ/Знам', 'День недели', 'Код времени проведения', 'Код группы',
                            'Код предмета', 'Код типа занятия', 'Номер аудитории', 'Код учителя']
    validator = ScheduleValidator


class ClassroomOccupancyScreenController(BaseModelScreenController):
    db_field_names = ['id', 'classroom_number', 'period_id', 'day_of_week', 'is_numerator','is_occupied']
    prepared_field_names = ['Идентификатор', 'Номер аудитории', 'Код времени проведения', 'День недели', 'Числ/Знам',
                            'Занято']
    validator = ClassroomOccupancyValidator


class TeacherOccupancyScreenController(BaseModelScreenController):
    db_field_names = ['id', 'teacher_id', 'period_id', 'day_of_week',  'day_of_week','is_numerator','is_occupied']
    prepared_field_names = ['Идентификатор', 'Код учителя', 'Код времени проведения', 'День недели', 'Числ/Знам',
                            'Занято']
    validator = TeacherOccupancyValidator


class GroupOccupancyScreenController(BaseModelScreenController):
    db_field_names = ['id', 'group_id', 'period_id', 'day_of_week','is_numerator','is_occupied']
    prepared_field_names = ['Идентификатор', 'Код группы', 'Код времени проведения', 'День недели', 'Числ/Знам',
                            'Занято']
    validator = GroupOccupancyValidator
