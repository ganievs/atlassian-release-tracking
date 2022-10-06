from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Application(Base):
    __tablename__ = "Application"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,)
    version = Column(String)
