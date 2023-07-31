import json

from flask import Blueprint

from app.core.attendance.attendance_controller import AttendanceController
from app.models.attendance import AsistenciaEncoder

router_attendance = Blueprint('attendance', __name__)


@router_attendance.route('/all')
def read_attendance():
    attendances = AttendanceController.get_all()
    json_str = json.dumps(attendances, cls=AsistenciaEncoder, ensure_ascii=True)
    print(json_str)
    return [{'item1': 1, 'item2': 2}]
