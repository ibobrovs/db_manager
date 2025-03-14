def get_tables(db, db_name):
    result = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in result]
