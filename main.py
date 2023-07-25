from flask import Flask
from app.database.connection import SessionLocal

app = Flask(__name__)


@app.route("/")
def hello_world():
    db = SessionLocal()
    print('db  '+str(db))
    return '<p>Response</p>'


if __name__ == "__main__":
    app.run()
