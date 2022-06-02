from flask import Flask
from flask_cors import CORS




app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/certificado'


def create_app():
    frameWork = Flask(__name__)
    CORS(frameWork)
    frameWork.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/certificado'
    from app.controllers import default
    return frameWork
    



