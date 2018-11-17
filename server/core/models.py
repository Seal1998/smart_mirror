from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Config(Base):
    __tablename__ = 'config'

    id = Column(Integer, primary_key=True)
    ssid = Column(String(256))
    password = Column(String(256))
