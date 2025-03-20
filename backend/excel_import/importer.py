import pandas as pd
from sqlalchemy.orm import Session
from backend.db.database import engine
from backend.models.models import User

def import_excel_to_db(file_path: str):
    df = pd.read_excel(file_path)  # Читаем Excel
    session = Session(engine)

    for _, row in df.iterrows():
        user = User(name=row["name"], email=row["email"])
        session.add(user)

    session.commit()
    session.close()
