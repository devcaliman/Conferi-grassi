import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def conectar():
    return mysql.connector.connect(
        host=os.getenv("127.0.0.1"), 
        port=int(os.getenv("3306")),
        user=os.getenv("root"),
        password=os.getenv("1234"),
        database=os.getenv("conferigrassi")
    )