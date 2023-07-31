from app.services.attendance_service import get_all_attendance, save_attendance


class AttendanceController:
    @staticmethod
    def get_all():
        attendances = get_all_attendance()
        return attendances

    @staticmethod
    def save(attendance):
        save_attendance(attendance)
