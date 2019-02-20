from database.config import Base
from sqlalchemy import Column, Integer, String
import requests, json

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    weather_temp = Column(String)
    weather_description = Column(String)
    weather_id = Column(String)

    def array(self):
        weather = {'city': self.city, 'temp': self.weather_temp,
                   'description': self.weather_description, 'id': self.weather_id}
        return weather