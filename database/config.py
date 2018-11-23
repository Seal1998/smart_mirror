import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_name = 'test'
cur_dir = os.getcwd()

Engine = create_engine('sqlite:///{}/{}.db'.format(cur_dir, db_name))

Base = declarative_base()

Session = sessionmaker(bind=Engine)