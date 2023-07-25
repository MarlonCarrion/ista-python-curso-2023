# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Estudiante(Base):
    __tablename__ = 'estudiante'
    __table_args__ = {'comment': 'Registro de los estudiantes de la unidad educativa'}

    cedula = Column(String(10), primary_key=True)
    primer_apellido = Column(String(100), nullable=False)
    segundo_apellido = Column(String(100), nullable=False)
    primer_nombre = Column(String(100), nullable=False)
    segundo_nombre = Column(String(100), nullable=False)
