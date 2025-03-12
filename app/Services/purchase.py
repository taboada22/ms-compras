import logging
from app import cache
from app.Models.purchases import Purchase
from app.Repositories.purchases import PurchaseRepository
from .format_logs import format_logs
from dataclasses import dataclass

logging = format_logs('PurchaseServices')

@dataclass
class PurchaseServices():
    repository = PurchaseRepository()

    def add_purchase(self, args: dict) -> Purchase:

        purchase = Purchase()

        for key, value in args.items():
            setattr(purchase, key, value) if hasattr(purchase, key) else logging.warning("Unknown attr in add_purchase")

        new_purchase = self.repository.add_purchase(purchase)

        cache.set(f'purchase_{new_purchase.id_purchase}', purchase, timeout=60)
        logging.info(f'Purchase_{new_purchase.id_purchase} added to cache') 

        return new_purchase

    def delete_purchase(self, id_purchase: int) -> None:

        purchase = self.repository.find_by_id(id_purchase)

        if purchase:
            cache.delete(f'purchase_{id_purchase}')
            logging.info(f'purchase_{id_purchase} deleted to cache')
            self.repository.delete(purchase)
            return None
            
        logging.error("Unknown purchase to delete")
        return purchase

    def get_last_record(self) -> Purchase:
        purchase = self.repository.get_last_record()
        if purchase:
            logging.info('Last record found')
            return purchase
        else:
            logging.error('No records found')
            raise BaseException('Last record not found')
