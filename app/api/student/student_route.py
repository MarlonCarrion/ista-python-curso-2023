import json

from flask import Blueprint, render_template

from app.core.student.student_controller import StudentController
from app.models.student import EstudianteEncoder

router_student = Blueprint('student', __name__)


@router_student.route('/all')
def read_student():
    students = StudentController.get_all()
    json_str = json.dumps(students, cls=EstudianteEncoder, ensure_ascii=True)
    return render_template('get_all.html', data=json.loads(json_str))


@router_student.route('/create')
def create_student():
    return render_template('student/create.html')

