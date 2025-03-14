from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.crud import db_operations

app = FastAPI()

@app.get("/databases/")
def list_databases():
    return {"databases": ["MySQL", "PostgreSQL", "SQLite", "MongoDB"]}

@app.get("/tables/{db_name}")
def get_tables(db_name: str, db: Session = Depends(get_db)):
    return db_operations.get_tables(db, db_name)
