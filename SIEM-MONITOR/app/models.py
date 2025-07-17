from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    user_agent = Column(String)
    event = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    risk_level = Column(String)

