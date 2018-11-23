from database.config import Engine, Base, Session
from database.models.WifiConfig import WifiConfig
from database.models.Tasks import Task
import datetime

Base.metadata.create_all(Engine)
session = Session()

#task = Task(name='test shit', description='12345')
#session.add(task)
#session.commit()
#session.close()

res = session.query(Task).first()
print(res.name)