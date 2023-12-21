from sqlalchemy.orm import Session
from sqlalchemy.engine import create_engine
from utils.config import *

engine = create_engine(DB_URL, echo=True)
session = Session(engine)


class DefaultNonModelObject:
    pass
