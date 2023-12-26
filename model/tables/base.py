from model.default import session, engine
from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    id = Column(Integer,primary_key=True)

    @declared_attr
    @classmethod
    def __tablename__(cls):
        return cls.__name__


class Department(Base):
    name = Column(String)


class Group(Base):
    name = Column(String)
    department_id = Column(Integer, ForeignKey(Department.id))
    size = Column(Integer)

class Teacher(Base):
    name = Column(String)
    department_id = Column(Integer, ForeignKey(Department.id))


class Subject(Base):
    name = Column(String)

class ClassType(Base):
    name = Column(String)
class Classroom(Base):
    classroom_number = Column(Integer,unique=True)
    class_type_id = Column(Integer, ForeignKey(ClassType.id))
    capacity = Column(Integer)


class ClassPeriod(Base):
    period_number = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)

class Schedule(Base):
    is_numerator = Column(String)
    day_of_week = Column(String)
    period_id = Column(Integer, ForeignKey(ClassPeriod.id))
    group_id = Column(Integer, ForeignKey(Group.id))
    subject_id = Column(Integer, ForeignKey(Subject.id))
    class_type_id = Column(Integer, ForeignKey(ClassType.id))
    classroom_number = Column(ForeignKey(Classroom.classroom_number))
    teacher_id = Column(Integer, ForeignKey(Teacher.id))


class ClassroomOccupancy(Base):
    classroom_number = Column(Integer, ForeignKey(Classroom.classroom_number))
    period_id = Column(Integer, ForeignKey(ClassPeriod.id))
    is_numerator = Column(String)
    day_of_week = Column(String)
    is_occupied = Column(String)


class TeacherOccupancy(Base):
    teacher_id = Column(Integer, ForeignKey(Teacher.id))
    period_id = Column(Integer, ForeignKey(ClassPeriod.id))
    is_numerator = Column(String)
    day_of_week = Column(String)
    is_occupied = Column(String)


class GroupOccupancy(Base):
    group_id = Column(Integer, ForeignKey(Group.id))
    period_id = Column(Integer, ForeignKey(ClassPeriod.id))
    is_numerator = Column(String)
    day_of_week = Column(String)
    is_occupied = Column(String)


def make_all():
    with session.begin():
        Base.metadata.create_all(engine)

def delete_all():
    with session.begin():
        Base.metadata.drop_all(engine)
