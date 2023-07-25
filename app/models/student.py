# coding: utf-8
import json

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

    def __repr__(self):
        return 'cedula: %s, primer_apellido: %s, segundo_apellido: %s primer_nombre: %s' \
               % (self.cedula, self.primer_apellido, self.segundo_apellido, self.primer_nombre)


class EstudianteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Estudiante):
            return {'cedula': obj.cedula, 'primer_apellido': obj.primer_apellido, 'segundo_apellido': obj.segundo_apellido,
                    'primer_nombre': obj.primer_nombre, 'segundo_nombre': obj.segundo_nombre}
        return json.JSONEncoder.default(self, obj)
