from app.core.AccessPoint import AccessPoint
from app.core.Wifi import Wifi
from database.db import db

#Класс, который воплощает в себе полное отделение логики от представления. Он будет делать запросы к бд, к API и тд

class Manager():
    status = 'test_status'

    def __init__(self):
        self.ap = AccessPoint()
        self.wifi = Wifi(interface='wlp3s0')#todo: интерфейс берётся из класса wifi (ifconfig)
        self.has_internet_connection = self.wifi.check_connection()

manager = Manager()