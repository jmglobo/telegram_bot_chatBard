# DATABASE

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# CANAL DE COMUNICACIÓN SQLALCHEMY - DB
# Creación del engine para estabecer comunicación entre SQLAlchemy y la DB
engine = create_engine("sqlite:///volumen/bot_telegram_chatgpt_BBDD.db", connect_args={"check_same_thread":False})

# SESIÓN
# Creación de la sesión para poder operar con la DB
Session = sessionmaker(bind=engine)
session = Session()

# MAPEO DE LAS CLASES
# Creación de la instrucción que mapeará las clases para vincularlas a la DB
Base = declarative_base()