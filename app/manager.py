from app.core.AccessPoint import AccessPoint
from app.core.Wifi import Wifi
from database.db import db
import requests, json


#Класс, который воплощает в себе полное отделение логики от представления. Он будет делать запросы к бд, к API и тд

class Manager():
    status = ''
    ap_SSID = "SmartMirror"
    ap_PASS = "771018888"
    weather_appid = "dbdaef6ff380721afe343cf0543f9e82"
    exchange_rates_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    exchange_rates_currency = ['USD', 'RUB']

    def __init__(self):
        self.ap = AccessPoint(interface='wlp3s0', ssid=self.ap_SSID, wpa_passphrase=self.ap_PASS)
        self.wifi = Wifi(interface='wlp3s0')#todo: интерфейс берётся из класса wifi (ifconfig)
        self.has_internet_connection = self.wifi.check_connection()
        db.set_pid()
        print(db.get_pid())

    def get_connection_status(self):
        self.wifi_ssid, self.wifi_pass = db.get_wifi_config()
        if self.wifi_ssid == 0:
            #self.ap.start()
            self.status = 0
            return self.status
        else:
            self.status = 'succesfully get an wifi config, connecting...'
            self.wifi = Wifi(interface='wlp3s0', ssid=self.wifi_ssid, password=self.wifi_pass)
            self.wifi.connect()
            #todo: если к точке не получилось подключиться, то вернёт False
            self.status = 1
            return self.status

#SETTINGS

    def set_pid(self):
        db.set_pid()

    def get_pid(self):
        return db.get_pid()

#EXCHANGERATES

    def parse_rates(self):
        res = requests.get(self.exchange_rates_url)
        return str(res.json())

    def update_rates(self):
        db.update_rates(self.parse_rates())

    def get_rates(self): #return type - DICT
        ex_rates_return = {}
        ex_ratex = db.get_rates()
        for rate in ex_ratex:
            if rate['cc'] in self.exchange_rates_currency:
                ex_rates_return[rate['cc']] = rate['rate']
        return ex_rates_return

#WEATHER

    def get_weater(self):
        return db.get_weather()

    def update_weather(self):
        weather_temp, weather_description, weather_id = self.parse_weather()
        db.update_weather(weather_temp, weather_description, weather_id)

    def parse_weather(self):
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={
                               'q': 'Kharkiv',
                               'type': 'like',
                               'units': 'metric',
                               'APPID': self.weather_appid})

        json_response = res.json()
        weather_temp = '{:+.0f}{}'.format(json_response['list'][0]['main']['temp'], "°C")#todo:убрать знак градуса, в базу сухое значение
        weather_description = ' {}'.format(json_response['list'][0]['weather'][0]['description'])
        weather_id = json_response['list'][0]['weather'][0]['id']
        return weather_temp, weather_description, weather_id


manager = Manager()
