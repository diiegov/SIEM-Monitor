from sqlalchemy.orm import Session
from . import models, schemas, detector

def registrar_log(db: Session, log: schemas.LogCreate):
    risco = detector.avaliar_risco(log.event, log.user_agent)
    db_log = models.Log(
        ip=log.ip,
        user_agent=log.user_agent,
        event=log.event,
        risk_level=risco
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def listar_logs(db: Session):
    return db.query(models.Log).order_by(models.Log.timestamp.desc()).all()

# Buscar log por ID
def buscar_log_por_id(db: Session, log_id: int):
    return db.query(models.Log).filter(models.Log.id == log_id).first()

# Deletar log por ID
def deletar_log(db: Session, log_id: int):
    log = db.query(models.Log).filter(models.Log.id == log_id).first()
    if log:
        db.delete(log)
        db.commit()
        return True
    return False

# Filtrar logs por nível (INFO, WARNING, ERROR...)
def filtrar_logs_por_nivel(db: Session, nivel: str):
    return db.query(models.Log).filter(models.Log.nivel == nivel).all()
