import os

from database.config import Engine, Base, Session
from database.models.WifiConfig import WifiConfig
from database.models.Tasks import Task
from database.models.Info import Info

class Database():

    session = Session()

    def __init__(self):
        Base.metadata.create_all(Engine)

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

    def set_pid(self):
        self.session.query(Info).delete()
        info = Info(pid=str(os.getpid()))
        self.session.add(info)
        self.session.commit()

    def get_pid(self):
        info = self.session.query(Info).first()
        return info.pid

db = Database()


