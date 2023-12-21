from datetime import datetime

from pydantic import BaseModel, validator, ValidationError, Field, field_validator
from pydantic import PositiveInt, constr, conint
from typing_extensions import Annotated


class UserModelValidator(BaseModel):
    username: str
    password: str
    email: str
    phone_number: str


class DepartamentValidator(BaseModel):
    id: PositiveInt
    name: str


class DepartamentSearchValidator(BaseModel):
    id: PositiveInt


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

    @validator('start_time', 'end_time')
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

    @validator('day_of_week')
    def validate_week_day(cls, v):
        if v.upper() not in ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']:
            raise ValidationError()
        return v

    @validator('is_numerator')
    def validate_is_numerator(cls, v):
        if v.lower() not in ['ч', 'з']:
            raise ValidationError()
        return v


class ClassroomOccupancyValidator(BaseModel):
    id: PositiveInt
    classroom_number: PositiveInt
    period_id: PositiveInt
    day_of_week: str
    is_numerator: str
    is_occupied: str

    @validator('day_of_week')
    def validate_week_day(cls, v):
        if v.upper() not in ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']:
            raise ValidationError()
        return v

    @validator('is_occupied')
    def validate_is_occupied(cls, v):
        if v.lower() not in ['да', 'нет']:
            raise ValidationError()
        return v

    @validator('is_numerator')
    def validate_is_numerator(cls, v):
        if v.lower() not in ['ч', 'з']:
            raise ValidationError()
        return v


class TeacherOccupancyValidator(BaseModel):
    id: PositiveInt
    teacher_id: PositiveInt
    period_id: PositiveInt
    day_of_week: str
    is_numerator: str
    is_occupied: str

    @validator('day_of_week')
    def validate_week_day(cls, v):
        if v.upper() not in ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']:
            raise ValidationError()
        return v

    @validator('is_occupied')
    def validate_is_occupied(cls, v):
        if v.lower() not in ['да', 'нет']:
            raise ValidationError()
        return v

    @validator('is_numerator')
    def validate_is_numerator(cls, v):
        if v.lower() not in ['ч', 'з']:
            raise ValidationError()
        return v


class GroupOccupancyValidator(BaseModel):
    id: PositiveInt
    group_id: PositiveInt
    period_id: PositiveInt
    day_of_week: str
    is_numerator: str
    is_occupied: str

    @validator('day_of_week')
    def validate_week_day(cls, v):
        if v.upper() not in ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']:
            raise ValidationError()
        return v

    @validator('is_occupied')
    def validate_is_occupied(cls, v):
        if v.lower() not in ['да', 'нет']:
            raise ValidationError()
        return v

    @validator('is_numerator')
    def validate_is_numerator(cls, v):
        if v.lower() not in ['ч', 'з']:
            raise ValidationError()
        return v
