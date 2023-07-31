import json

from flask import Blueprint, render_template, request

from app.core.student.student_controller import StudentController
from app.models.student import EstudianteEncoder, Estudiante

router_student = Blueprint('student', __name__)


@router_student.route('/all')
def read_student():
    students = StudentController.get_all()
    json_str = json.dumps(students, cls=EstudianteEncoder, ensure_ascii=True)
    return render_template('student/get_all.html', data=json.loads(json_str))


@router_student.route('/create')
def create_student():
    return render_template('student/create.html')


@router_student.route('/saveStudent', methods=['POST'])
def save_student():
    student = Estudiante()
    student.cedula = request.form['cedula']
    student.primer_nombre = request.form['first_name']
    student.segundo_nombre = request.form['second_name']
    student.primer_apellido = request.form['first_lastname']
    student.segundo_apellido = request.form['second_lastname']
    StudentController.save(student)
    return read_student()
