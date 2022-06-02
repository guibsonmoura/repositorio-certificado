from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/certificado'
    db = SQLAlchemy(app)
    return app



from app.controllers import default
