from app.services.attendance_service import get_all_attendance, save_attendance, get_attendance_by_student_course


class AttendanceController:
    @staticmethod
    def get_all():
        attendances = get_all_attendance()
        return attendances

    @staticmethod
    def save(attendance):
        save_attendance(attendance)

    @staticmethod
    def get_attendance_by_student_course(cedula, course):
        attendances = get_attendance_by_student_course(cedula, course)
        return attendances
