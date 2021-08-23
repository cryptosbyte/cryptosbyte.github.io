from app import db
# Essentially load in DB from app.py file

def load():
    db.create_all()
# Create DB instance