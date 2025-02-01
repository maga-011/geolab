from ext import app, db
from models import User, Feedback

# Create all database tables
with app.app_context():
    db.create_all()
