from pydantic import BaseModel
from datetime import datetime

class LogCreate(BaseModel):
    ip: str
    user_agent: str
    event: str

class LogOut(LogCreate):
    timestamp: datetime
    risk_level: str
