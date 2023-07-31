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
        print('upsert attendance')
