from database.config import Base
from sqlalchemy import Column, Integer, String

class Exchangerates(Base):
    __tablename__ = 'exchangerates'

    id = Column(Integer, primary_key=True)
    exchRates = Column(String)# json string