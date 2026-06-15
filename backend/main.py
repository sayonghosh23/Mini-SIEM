from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, Log, Alert
from detector import detect_threat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini SIEM Dashboard")


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

    if severity in ["HIGH", "CRITICAL"]:

        alert = Alert(
            event=event,
            severity=severity,
            status="OPEN"
        )

        db.add(alert)

    db.commit()

    return {
        "status": "stored",
        "severity": severity
    }


@app.get("/logs")
def get_logs():

    db = SessionLocal()

    return db.query(Log).all()


@app.get("/alerts")
def get_alerts():

    db = SessionLocal()

    return db.query(Alert).all()


@app.get("/search")
def search_logs(keyword: str):

    db = SessionLocal()

    logs = db.query(Log).filter(
        Log.event.contains(keyword)
    ).all()

    return logs
