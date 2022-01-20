from . import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    watchlist = db.relationship("WatchList", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.email}>"

class WatchList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.Integer)
    show = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
