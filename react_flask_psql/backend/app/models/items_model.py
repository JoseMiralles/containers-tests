from app.config import db

class Item(db.Model):
    __tablename__="items"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    text = db.Column(db.String(128), nullable=False)
