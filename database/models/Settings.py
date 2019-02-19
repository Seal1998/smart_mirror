from database.config import Base
from sqlalchemy import Column, String, Integer

class Settings(Base):
    __tablename__ = "info"

    id = Column(Integer, primary_key=True)
    pid = Column(Integer)

    follow_exchRates = Column(String)#json string
    weather_city = Column(String)
    weather_appid = Column(String)