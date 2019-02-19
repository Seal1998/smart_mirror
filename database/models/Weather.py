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

    def parse_weather(self, city, appid):
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={
                               'q': city,
                               'type': 'like',
                               'units': 'metric',
                               'APPID': appid})

        json_response = res.json()
        self.weather_temp = '{:+.0f}{}'.format(json_response['list'][0]['main']['temp'], "°C")
        self.weather_description = ' {}'.format(json_response['list'][0]['weather'][0]['description'])
        self.weather_id = json_response['list'][0]['weather'][0]['id']