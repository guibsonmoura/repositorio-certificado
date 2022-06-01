from app import db

class User(db.Model):
    __tablename__ = "login"

    id = db.Column(db.Integer, primary_key= True)
    usuario = db.Column(db.String(100))
    senha = db.Column(db.String(100))


    def __init__(self, usuario, password):
        self.usuario = usuario
        self.senha = password

    def __repr__(self):
        return "<User %r>" % self.usuario
        
