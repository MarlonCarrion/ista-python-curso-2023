from app.models.student import Estudiante
from app.services.basic import get_db


def get_all_student():
    students = []
    with get_db() as db:
        students = db.query(Estudiante).all()
    return students
