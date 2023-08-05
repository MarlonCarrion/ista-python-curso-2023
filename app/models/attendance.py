# coding: utf-8
import json

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
    cedula = Column(String(10))

    # estudiante = relationship('Estudiante')


class AsistenciaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Asistencia):
            return {'codigo': obj.codigo, 'materia': obj.materia, 'fecha': obj.fecha.isoformat(), 'cedula': obj.cedula}
        return json.JSONEncoder.default(self, obj)
