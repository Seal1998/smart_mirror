from database.config import Base
from sqlalchemy import Column, Integer, String, Date
import datetime

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
#    deadline = Column(Date, default=None)
#    created = Column(Date, default=datetime.datetime.now().strftime("%d %B, %Y at %H:%M"))