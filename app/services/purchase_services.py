from datetime import datetime

import logging
from app.models import Purchase
from app.repositories.purchase_repository import PurchasesRepository
from app import cache

class PurchasesService:
    def __init__(self):
        self.repository = PurchasesRepository()

    def add_purchase(self, purchase_data: Purchase) -> Purchase:
        return self.repository.save(purchase_data)

    def delete_purchase(self, purchase_id: int) -> None:
        purchase = self.repository.find_by_id(purchase_id)
        if purchase:
            try:
                purchase.deleted_at = datetime.now()
                result = self.repository.save(purchase)
                cache.delete(f'pago_{result.id_purchase}')
            except Exception as e:
                logging.error(f'cancelando pago: {e}')
            return result

    def get_purchase(self, purchase_id: int) -> Purchase:
        return self.repository.find_by_id(purchase_id)

    def get_all_purchases(self) -> list:
        return self.repository.find_all()