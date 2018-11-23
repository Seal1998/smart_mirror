from database.config import Base
from sqlalchemy import Column, Integer, String

class WifiConfig(Base):
    __tablename__ = 'wificonfig'

    id = Column(Integer, primary_key=True)
    ssid = Column(String)
    password = Column(String)