from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.extension import db
from app.routes import bp
from flask_migrate import Migrate # type: ignore

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mf2004@localhost/facial_payment'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(bp, url_prefix='/api')

    
    return app