from contextlib import contextmanager

from app.database.connection import SessionLocal


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        db.rollback()
        raise
    finally:
        db.close()
