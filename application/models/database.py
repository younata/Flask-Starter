from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def database_session():
    return db.session
