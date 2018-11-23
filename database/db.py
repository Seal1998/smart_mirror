from database.config import Engine, Base, Session

Base.metadata.create_all(Engine)