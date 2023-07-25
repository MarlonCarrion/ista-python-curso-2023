from app.services.student_service import get_all_student


class StudentController:
    @staticmethod
    def get_all():
        students = get_all_student()
        return students
