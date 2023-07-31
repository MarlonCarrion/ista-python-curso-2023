from flask import Flask, render_template
from flask_restx import Api

from app.api.attendance.attendance_route import router_attendance
from app.api.student.student_route import router_student
from app.database.connection import SessionLocal

app = Flask(__name__)

app.register_blueprint(router_student, url_prefix='/api/student')
app.register_blueprint(router_attendance, url_prefix='/api/attendance')


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
