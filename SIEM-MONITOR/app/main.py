from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI(title="SIEM Monitor")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/logs", response_model=schemas.LogOut)
def criar_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    return crud.registrar_log(db, log)

@app.get("/logs")
def ver_logs(db: Session = Depends(get_db)):
    return crud.listar_logs(db)

# ⬇️ COLE AQUI ABAIXO ⬇️
@app.get("/logs/{log_id}", response_model=schemas.LogOut)
def buscar_log(log_id: int, db: Session = Depends(get_db)):
    log = crud.buscar_log_por_id(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log não encontrado")
    return log
