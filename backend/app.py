from flask import Flask, request, jsonify
from flask_cors import CORS
from app import create_app  # Import the shared SQLAlchemy instance
from app.extension import db
from app.models import User, Transaction  # Import your models

app = create_app()
CORS(app)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)