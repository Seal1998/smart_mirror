from database.config import Engine, Base, Session
from database.models.WifiConfig import WifiConfig
from database.models.Tasks import Task

class Database():

    session = Session()

    def __init__(self):
        Base.metadata.create_all(Engine)

    def add_wifi_config(self, SSID, PASS):
        config = WifiConfig(ssid=SSID, password=PASS)
        self.session.add(config)
        self.session.commit()

    def get_wifi_config(self):
        config = self.session.query(WifiConfig).first()
        return config.ssid, config.password


db = Database()


