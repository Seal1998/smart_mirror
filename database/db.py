import os

from database.config import Engine, Base, Session
from database.models.WifiConfig import WifiConfig
from database.models.Task import Task
from database.models.Settings import Settings
from database.models.Weather import Weather

class Database():

    session = Session()

    def __init__(self):
        Base.metadata.create_all(Engine)

#WIFI

    def set_wifi_config(self, SSID, PASS):
        self.session.query(WifiConfig).delete()
        config = WifiConfig(ssid=SSID, password=PASS)
        self.session.add(config)
        self.session.commit()

    def get_wifi_config(self):
        config = self.session.query(WifiConfig).first()
        if config is None:
            return 0, 0
        return config.ssid, config.password

#SETTINGS

    def set_settings(self, follow_exchRates, weather_city, weather_appid):
        settings = Settings(pid=os.getpid(), follow_exchRates=follow_exchRates, weather_city=weather_city, weather_appid=weather_appid)
        self.session.add(settings)
        self.session.commit()


    def set_pid(self):
        settings = self.session.query(Settings).first()
        if settings is None:
            settings = Settings()
            settings.pid = os.getpid()
            self.session.add(settings)
        else:
            settings.pid = os.getpid()

        self.session.commit()

    def get_pid(self):
        settings = self.session.query(Settings).first()
        if settings is None:
            self.set_pid()
            return os.getpid()
        return settings.pid

    def get_city(self):
        settings = self.session.query(Settings).first()
        return settings.city

    def get_weather_appid(self):
        settings = self.session.query(Settings).first()
        return settings.weather_appid

#WEATHER

    def get_weather(self):
        weather = self.session.query(Weather).first()
        return weather.array()

    def update_weather(self, appid):
        weather = self.session.query(Weather).first()
        if weather is None:
            weather = Weather()
        weather.parse_weather(self.get_city(), self.get_weather_appid())



db = Database()


