from app import db  
from app.models import Purchase
from sqlalchemy.exc import IntegrityError, NoResultFound

class PurchasesRepository:  
    def save(self, purchase: Purchase) -> Purchase:  
        db.session.add(purchase)  
        try:  
            db.session.commit()  
            return purchase  
        except IntegrityError:  
            db.session.rollback()  
            return None  

    def find_by_id(self, id: int) -> Purchase:
        try:
            return db.session.query(Purchase).filter(Purchase.id_purchase == id).one()
        except NoResultFound:
            return None


    def find_all(self) -> list:  
        return db.session.query(Purchase).all()
    
    

            