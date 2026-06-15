from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, Log
from detector import detect_threat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini SIEM")

@app.get("/")
def root():
    return {"message": "Mini SIEM Running"}

@app.post("/log")
def add_log(source: str, event: str):

    db = SessionLocal()

    severity = detect_threat(event)

    log = Log(
        source=source,
        event=event,
        severity=severity
    )

    db.add(log)
    db.commit()

    return {
        "status": "stored",
        "severity": severity
    }

@app.get("/logs")
def get_logs():

    db = SessionLocal()

    return db.query(Log).all()
