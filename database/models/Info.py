from database.config import Base
from sqlalchemy import Column, String, Integer

class Info(Base):
    __tablename__ = "info"

    id = Column(Integer, primary_key=True)
    pid = Column(String)