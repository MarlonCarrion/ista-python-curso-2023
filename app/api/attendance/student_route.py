from flask import Blueprint

router_attendance = Blueprint('attendance', __name__)


@router_attendance.route('/all')
def read_attendance():
    return [{'item1': 1, 'item2': 2}]
