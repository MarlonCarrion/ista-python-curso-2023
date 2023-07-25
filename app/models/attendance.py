# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.models.student import Estudiante

Base = declarative_base()
metadata = Base.metadata


class Asistencia(Base):
    __tablename__ = 'asistencia'
    __table_args__ = {'comment': 'Registro de la asistencia de los estudiantes de la unidad educativa'}

    codigo = Column(Integer, primary_key=True)
    materia = Column(String(100), nullable=False)
    fecha = Column(Date, nullable=False)
    cedula = Column(ForeignKey('estudiante.cedula'), nullable=False, index=True)

    estudiante = relationship('Estudiante')
