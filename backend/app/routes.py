# backend/routes.py
from flask import request, jsonify, Blueprint
from sqlalchemy import select
from app.models import User, Transaction, db
import numpy as np
import base64
import cv2 # type: ignore

# Crie um Blueprint
bp = Blueprint('api', __name__)

# Endpoint para registrar um novo usuário
@bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')  # Obtém a senha do corpo da requisição

    if not username or not email or not password:
        return jsonify({"message": "Username, email, and password are required"}), 400

    # Verificar se o usuário já existe
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 409

    # Criar um novo usuário
    new_user = User(username=username, email=email)
    new_user.set_password(password)  # Define a senha criptografada
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "user_id": new_user.id}), 201

# Endpoint para fazer upload de uma imagem e gerar o embedding facial
@bp.route('/upload-face/<int:user_id>', methods=['POST'])
def upload_face(user_id):
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    # Ler a imagem enviada
    nparr = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Detectar rosto na imagem (exemplo básico com OpenCV)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
        return jsonify({"message": "No face detected"}), 400
    # Gerar um embedding facial (simulado como um array binário)
    _, buffer = cv2.imencode('.jpg', img)
    face_embedding = base64.b64encode(buffer).decode('utf-8')  # Codificar como base64
    # Atualizar o usuário com o embedding facial
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    user.face_embedding = face_embedding
    db.session.commit()
    return jsonify({"message": "Face uploaded successfully"}), 200

# Endpoint para criar uma nova transação
@bp.route('/create-transaction', methods=['POST'])
def create_transaction():
    data = request.json
    user_id = data.get('user_id')
    amount = data.get('amount')
    if not user_id or not amount:
        return jsonify({"message": "User ID and amount are required"}), 400
    # Verificar se o usuário existe
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    # Criar uma nova transação
    new_transaction = Transaction(user_id=user_id, amount=amount, status="pending")
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({"message": "Transaction created successfully", "transaction_id": new_transaction.id}), 201