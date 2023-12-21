from controller.DatabaseEditScreen.components.controllers import *
from model.tables.base import *
from view.DatabaseEditScreen.components.model_screens import *

screens = {
    'Кафедры': {
        'model': Department,
        'controller': DepartamentScreenController,
        'view': DepartamentScreen
    },
    'Группы': {
        'model': Group,
        'controller': GroupScreenController,
        'view': GroupScreen
    },
    'Преподаватели': {
        'model': Teacher,
        'controller': TeacherScreenController,
        'view': TeacherScreen
    },
    'Предметы': {
        'model': Subject,
        'controller': SubjectScreenController,
        'view': SubjectScreen
    },
    'Тип занятии': {
        'model': ClassType,
        'controller': ClassTypeScreenController,
        'view': ClassTypeScreen
    },
    'Период проведения пар': {
        'model': ClassPeriod,
        'controller': ClassPeriodScreenController,
        'view': ClassPeriodScreen
    },
    'Аудитории': {
        'model': Classroom,
        'controller': ClassroomScreenController,
        'view': ClassroomScreen
    },
    'Расписание': {
        'model': Schedule,
        'controller': ScheduleScreenController,
        'view': ScheduleScreen
    },
    'Занятось аудитории': {
        'model': ClassroomOccupancy,
        'controller': ClassroomOccupancyScreenController,
        'view': ClassroomOccupancyScreen
    },
    'Занятость учителей': {
        'model': TeacherOccupancy,
        'controller': TeacherOccupancyScreenController,
        'view': TeacherOccupancyScreen
    },
    'Занятость группы': {
        'model': GroupOccupancy,
        'controller': GroupOccupancyScreenController,
        'view': GroupOccupancyScreen
    },
}
