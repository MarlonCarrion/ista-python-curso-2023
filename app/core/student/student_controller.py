from app.models.student import Estudiante
from app.services.student_service import get_all_student, save_student


class StudentController:
    @staticmethod
    def get_all():
        students = get_all_student()
        return students

    @staticmethod
    def save(student):
        save_student(student)
