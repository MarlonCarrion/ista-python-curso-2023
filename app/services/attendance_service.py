from app.database.connection import get_db
from app.models.attendance import Asistencia


def get_all_attendance():
    attendances = []
    with get_db() as db:
        attendances = db.query(Asistencia).all()
    return attendances


def save_attendance(attendance):
    with get_db() as db:
        db.merge(attendance)
        db.commit()
        print('upsert attendance')


def get_attendance_by_student_course(cedula, course):
    attendances = []
    with get_db() as db:
        attendances = db.query(Asistencia).filter(Asistencia.cedula == {cedula}, Asistencia.materia == {course}).all()
    return attendances
