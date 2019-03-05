import os, json

from sqlalchemy.orm import scoped_session, sessionmaker

from database.config import Engine, Base, Session
from database.models.WifiConfig import WifiConfig
from database.models.Task import Task
from database.models.Settings import Settings
from database.models.Weather import Weather
from database.models.ExchangeRates import ExchangeRates

class Database():

    session = scoped_session(sessionmaker(bind=Engine))


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

    def update_settings(self, follow_exchRates, city, weather_appid):
        settings = self.session.query(Settings).first()
        if settings is None:
            settings = Settings(pid=os.getpid(), follow_exchRates=follow_exchRates, city=city, weather_appid=weather_appid)
            self.session.add(settings)
            self.session.commit()
            return True
        settings.pid = os.getpid()
        settings.follow_exchRates = '0'
        settings.city = city
        settings.weather_appid = '0'
        db.session.add(settings)
        db.session.commit()



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
            print("settings is none")
            self.set_pid()
            return os.getpid()
        return settings.pid

    def get_city(self):
        settings = self.session.query(Settings).first()
        return settings.city

#ExchangeRates

    def get_rates(self): #return type - JSON array
        ex_rates = self.session.query(ExchangeRates).first()

        return json.loads(ex_rates.exchRates)

    def update_rates(self, ex_rates_json_string): #input type - JSON string
        ex_rates = self.session.query(ExchangeRates).first()
        if ex_rates is None:
            ex_rates = ExchangeRates(exchRates=ex_rates_json_string)
            self.session.add(ex_rates)
            self.session.commit()
            return True
        ex_rates.exchRates = ex_rates_json_string
        self.session.commit()

#WEATHER

    def get_weather_appid(self):
        settings = self.session.query(Settings).first()
        return settings.weather_appid

    def get_weather(self):
        weather = self.session.query(Weather).first()
        return weather.array()

    def update_weather(self, weather_temp, weather_description, weather_id):
        weather = self.session.query(Weather).first()
        if weather is None:
            weather = Weather(city=self.get_city(), weather_temp=weather_temp, weather_description=weather_description, weather_id=weather_id)
            self.session.add(weather)
            self.session.commit()
            return True
        weather.weather_temp = weather_temp
        weather.weather_description=weather_description
        weather.weather_id=weather_id
        #weather.city=self.get_city()
        self.session.commit()



db = Database()


