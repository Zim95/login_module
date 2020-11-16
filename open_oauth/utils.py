from app import db
from sqlalchemy.exc import DatabaseError


def commit_to_db(message):
    try:
        db.session.commit()
    except DatabaseError as de:
        db.session.rollback()
        print(de)
