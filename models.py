from flask_login import UserMixin
from ext import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    mail = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    feedback = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Feedback by {self.username}>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
