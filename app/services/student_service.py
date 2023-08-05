from app.database.connection import get_db
from app.models.student import Estudiante


def get_all_student():
    students = []
    with get_db() as db:
        students = db.query(Estudiante).all()
    return students


def save_student(student):
    with get_db() as db:
        db.merge(student)
        db.commit()
        print('upsert student....')
