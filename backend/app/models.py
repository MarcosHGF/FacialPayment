from . import db  # Import the shared SQLAlchemy instance from __init__.py
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    face_embedding = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"

class Transaction(db.Model):
    """
    Model for storing transaction information.
    """
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each transaction
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to link to the user
    amount = db.Column(db.Float, nullable=False)  # Transaction amount
    status = db.Column(db.String(20), default='pending')  # Status of the transaction (e.g., pending, completed)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp for when the transaction occurred

    # Define a relationship with the User model
    user = db.relationship('User', backref=db.backref('transactions', lazy=True))

    def __repr__(self):
        return f"<Transaction {self.id} by User {self.user_id}>"