from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    phone = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=True, nullable=False)

    def __init__(self, username, password, email, phone=None):
        if not username:
            raise ValueError('Invalid value for username')
        if not password:
            raise ValueError('Invalid value for password')
        self.username = username
        self.password = password
        self.email = email
        if phone:
            self.phone = phone

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone
        }
