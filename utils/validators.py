import re
from datetime import datetime
from pydantic import BaseModel, ValidationError, field_validator
from pydantic import PositiveInt


def base_check_is_numerator(v):
    if v.lower() not in ['ч', 'з']:
        raise ValidationError()


def base_check_day_week(v):
    if v.upper() not in ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']:
        raise ValidationError()


def base_check_is_occupied(v):
    if v.lower() not in ['да', 'нет']:
        raise ValidationError()


class UserModelValidator(BaseModel):
    username: str
    password: str
    email: str
    phone_number: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, v):
            raise ValueError('Неправильно введенная почта')
        return v

    @field_validator('password')
    @classmethod
    def validate_psw(cls, v: str):
        if len(v) < 8:
            raise ValueError('Длина пароля должны быть от 8 и более символов')

        if not any(char.isdigit() for char in v):
            raise ValueError('Пароль должен содержать цифры')

        if not any(char.isalpha() for char in v):
            raise ValueError('Пароль должен содержать буквенные символы')

        if not any(char.isupper() for char in v):
            raise ValueError('Пароль должен содержать хотя бы 1 заглавный символ')
        return v

    @field_validator('username')
    @classmethod
    def validate_username(cls, v: str):
        if len(v) < 5:
            raise ValueError('Длина никнейма должны быть от 5 и более символов')

        return v

    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, v):
        phone_pattern = re.compile(r'^(?:\+7|8)\d{10}$')

        if not re.match(phone_pattern, v):
            raise ValueError('Не правильно введен номер телефона!')
        return v


class DepartamentValidator(BaseModel):
    id: PositiveInt
    name: str


class GroupValidator(BaseModel):
    id: PositiveInt
    name: str
    department_id: PositiveInt
    size: PositiveInt


class TeacherValidator(BaseModel):
    id: PositiveInt
    name: str
    department_id: PositiveInt


class SubjectValidator(BaseModel):
    id: PositiveInt
    name: str


class ClassPeriodValidator(BaseModel):
    id: PositiveInt
    period_number: PositiveInt
    start_time: str
    end_time: str

    @field_validator('start_time', 'end_time')
    @classmethod
    def validate_time_format(cls, value):
        try:
            datetime.strptime(value, '%H:%M').time()
        except ValueError:
            raise ValidationError('Invalid time format. Use HH:MM:SS.')

        return value


class ClassTypeValidator(BaseModel):
    id: PositiveInt
    name: str


class ClassroomValidator(BaseModel):
    id: PositiveInt
    classroom_number: PositiveInt
    class_type_id: PositiveInt
    capacity: PositiveInt


class ScheduleValidator(BaseModel):
    id: PositiveInt
    is_numerator: str
    day_of_week: str
    period_id: PositiveInt
    group_id: PositiveInt
    subject_id: PositiveInt
    class_type_id: PositiveInt
    classroom_number: PositiveInt
    teacher_id: PositiveInt

    @field_validator('day_of_week')
    @classmethod
    def validate_week_day(cls, v):
        base_check_day_week(v)
        return v

    @field_validator('is_numerator')
    @classmethod
    def validate_is_numerator(cls, v):
        base_check_is_numerator(v)
        return v


class ClassroomOccupancyValidator(BaseModel):
    id: PositiveInt
    classroom_number: PositiveInt
    period_id: PositiveInt
    day_of_week: str
    is_numerator: str
    is_occupied: str

    @field_validator('day_of_week')
    @classmethod
    def validate_week_day(cls, v):
        base_check_day_week(v)
        return v

    @field_validator('is_occupied')
    @classmethod
    def validate_is_occupied(cls, v):
        base_check_is_occupied(v)
        return v

    @field_validator('is_numerator')
    @classmethod
    def validate_is_numerator(cls, v):
        base_check_is_numerator(v)
        return v


class TeacherOccupancyValidator(BaseModel):
    id: PositiveInt
    teacher_id: PositiveInt
    period_id: PositiveInt
    is_numerator: str
    day_of_week: str
    is_occupied: str

    @field_validator('day_of_week')
    @classmethod
    def validate_week_day(cls, v):
        base_check_day_week(v)
        return v

    @field_validator('is_occupied')
    @classmethod
    def validate_is_occupied(cls, v):
        base_check_is_occupied(v)
        return v

    @field_validator('is_numerator')
    @classmethod
    def validate_is_numerator(cls, v):
        base_check_is_numerator(v)
        return v


class GroupOccupancyValidator(BaseModel):
    id: PositiveInt
    group_id: PositiveInt
    period_id: PositiveInt
    day_of_week: str
    is_numerator: str
    is_occupied: str

    @field_validator('day_of_week')
    @classmethod
    def validate_week_day(cls, v):
        base_check_day_week(v)
        return v

    @field_validator('is_occupied')
    @classmethod
    def validate_is_occupied(cls, v):
        base_check_is_occupied(v)
        return v

    @field_validator('is_numerator')
    @classmethod
    def validate_is_numerator(cls, v):
        base_check_is_numerator(v)
        return v
