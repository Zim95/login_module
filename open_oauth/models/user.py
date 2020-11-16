from app import db
# from open_oauth.utils import commit_to_db


def create_user(password, username=None, email=None, phone=None):
    if not password:
        raise ValueError('Password required')
    if not username and not email:
        raise ValueError('Either username or email required')
    if not username:
        username = email
    return User(
        password, username=username,
        email=email, phone=phone
    )


def delete_user():
    pass


def update_user():
    pass


def get_user():
    pass


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, password, username=None, email=None, phone=None):
        self.username = username
        self.email = email
        self.phone = phone

    def get_user_id(self):
        return self.id
