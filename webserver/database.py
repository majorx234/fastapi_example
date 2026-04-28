from sqlmodel import Session, create_engine, select
from webserver.config import Config


class DatabaseInterface:
    def __init__(self):
        user = Config().db_user
        password = Config().db_password
        hostname = "127.0.0.1"
        port = 5432
        db_name = Config().db_name

        self.engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{db_name}')

        self.session = Session(self.engine)

    def query(self, sql_statement):
        rows = []
        for row in self.session.exec(sql_statement):
            rows.append(row)
        return rows
