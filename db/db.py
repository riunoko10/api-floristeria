from sqlmodel import create_engine

db_path = r"../flowers.db"
sqlite_url = f"sqlite:///{db_path}"
engine = create_engine(sqlite_url, echo=True)