from db import db

class itemModel(db.Model):
    
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2),unique=False nullable=False)
    store_id = db.Column(db.Integer, unique=False, nullable= False)