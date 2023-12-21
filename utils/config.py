DRIVER = "ODBC+Driver+17+for+SQL+Server"
SERVER_NAME = "LAPTOP-NBAFMOVQ"
DB_NAME = "TimeTable"
UID = f'LAPTOP-NBAFMOVQ\\User'
PWD = ""
HOST = 'localhost'

DB_URL = f"mssql+pyodbc://{HOST}/{DB_NAME}?driver={DRIVER}"