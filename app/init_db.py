import os
import sys
# Ensure app is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import app
from app.models import db, User
from werkzeug.security import generate_password_hash

def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized.")
        
        # Check if admin exists
        admin = User.query.filter_by(username="admin").first()
        if not admin:
            hashed_pw = generate_password_hash("password", method='pbkdf2:sha256')
            new_admin = User(username="admin", password_hash=hashed_pw)
            db.session.add(new_admin)
            db.session.commit()
            print("Default admin user created. (Username: admin, Password: password)")
        else:
            print("Admin user already exists.")

if __name__ == "__main__":
    init_db()
