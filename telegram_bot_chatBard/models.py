# MODELS

from database import Base
from sqlalchemy import Column,String,Integer



# Tabla USUARIO
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer,primary_key=True)
    id_usuario = Column(String(300),nullable=False,unique=True)
    nombre_usuario = Column(String(300),nullable=False)

    def __init__(self,
                 id_usuario,
                 nombre_usuario):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario





# Tabla NUEVO USUARIO
class Nuevo_Usuario(Base):
    __tablename__ = "nuevoUsuario"
    id = Column(Integer,primary_key=True)
    id_usuario = Column(String(300),nullable=False,unique=True)
    nombre_usuario = Column(String(300),nullable=False)
    fecha = Column(String(300),nullable=False)
    hora = Column(String(300),nullable=False)
    mensaje = Column(String(1000),nullable=False)

    def __init__(self,
                 id_usuario,
                 nombre_usuario,
                 fecha,
                 hora,
                 mensaje):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.fecha = fecha
        self.hora = hora
        self.mensaje = mensaje





# Tabla REGISTRO ERRORES
class Registro_Errores(Base):
    __tablename__ = "registro_errores"
    id = Column(Integer,primary_key=True)
    id_usuario = Column(String(300),nullable=False,unique=True)
    error = Column(String(300),nullable=False)
    mensaje_error = Column(String(700),nullable=False)
    fecha = Column(String(300),nullable=False)
    hora = Column(String(300),nullable=False)

    def __init__(self,
                 id_usuario,
                 error,
                 mensaje_error,
                 fecha,
                 hora):
        self.id_usuario = id_usuario
        self.error = error
        self.mensaje_error = mensaje_error
        self.fecha = fecha
        self.hora = hora





# Tabla COOKIES
class Cookies(Base):
    __tablename__ = "cookies"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(300),nullable=False,unique=True)
    valor = Column(String(300),nullable=False)

    def __init__(self,
                 nombre,
                 valor):
        self.nombre = nombre
        self.valor = valor
