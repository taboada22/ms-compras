from dataclasses import dataclass
from app import db  
from datetime import datetime  


@dataclass
class Purchase(db.Model):  
    __tablename__ = 'purchases'  

    id_purchase = db.Column(db.Integer, primary_key=True)  
    id_product = db.Column(db.Integer, nullable=False)     
    mailing_address= db.Column(db.String(120), nullable=False)  
    date_purchase = db.Column(db.DateTime, default=datetime.utcnow)  
    deleted_at: datetime = db.Column(db.DateTime, nullable=True)
