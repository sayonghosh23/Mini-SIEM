from sqlalchemy import Column, Integer, String
from database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    source = Column(String)
    event = Column(String)
    severity = Column(String)
