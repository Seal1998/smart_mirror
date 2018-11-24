from app.core.AccessPoint import AccessPoint
from app.core.Wifi import Wifi
from database.db import db

#Класс, который воплощает в себе полное отделение логики от представления. Он будет делать запросы к бд, к API и тд

class Manager():
    status = ''

    def __init__(self):
        self.ap = AccessPoint()
        self.wifi = Wifi(interface='wlp3s0')#todo: интерфейс берётся из класса wifi (ifconfig)
        self.has_internet_connection = self.wifi.check_connection()

    def set_up_connection(self):
        self.status = 'trying to get wifi config from database'
        self.wifi_ssid, self.wifi_pass = db.get_wifi_config()
        if self.wifi_ssid == 0:
            self.status = 2
        else:
            self.status = 'succesfully get an wifi config, connecting...'
            self.wifi = Wifi(interface='wlp3s0', ssid=self.wifi_ssid, password=self.wifi_pass)
            self.wifi.connect()
            #todo: если к точке не получилось подключиться, то вернёт False
            self.status = 1

manager = Manager()