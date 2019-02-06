from app.core.AccessPoint import AccessPoint
from app.core.Wifi import Wifi
from database.db import db


#Класс, который воплощает в себе полное отделение логики от представления. Он будет делать запросы к бд, к API и тд

class Manager():
    status = ''
    ap_SSID = "SmartMirror"
    ap_PASS = "771018888"

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


manager = Manager()
