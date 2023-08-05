import json

from flask import Blueprint, render_template, request

from app.core.attendance.attendance_controller import AttendanceController
from app.core.student.student_controller import StudentController
from app.models.attendance import AsistenciaEncoder, Asistencia

router_attendance = Blueprint('attendance', __name__)


@router_attendance.route('/all')
def read_attendance():
    attendances = AttendanceController.get_all()
    json_str = json.dumps(attendances, cls=AsistenciaEncoder, ensure_ascii=True)
    return render_template('attendance/get_all.html', data=json.loads(json_str))


@router_attendance.route('/create')
def create_attendance():
    attendances = AttendanceController.get_all()
    students = StudentController.get_all()
    return render_template('attendance/create.html', data=students)


@router_attendance.route('/saveAttendance', methods=['POST'])
def save_attendance():
    attendance = Asistencia()
    attendance.cedula = request.form['cedula']
    attendance.fecha = request.form['date']
    attendance.materia = request.form['course']
    AttendanceController.save(attendance)
    return read_attendance()
