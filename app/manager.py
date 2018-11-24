#from app.core.AccessPoint import AccessPoint
from app.core.Wifi import Wifi
from database.db import db

#Класс, который воплощает в себе полное отделение логики от представления. Он будет делать запросы к бд, к API и тд

class Manager():
    def __init__(self):
        ssid, passw = db.get_wifi_config()
        self.wifi = Wifi(ssid=ssid, password=passw, interface='wlp3s0')
#        self.ap = AccessPoint()

        self.internet_connection = self.wifi.check_connection()

manager = Manager()

manager.wifi.connect()