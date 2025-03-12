import unittest
from app.Services.purchase import PurchaseServices
from . import BaseTestClass

class PurchaseTestCase(BaseTestClass):

    service = PurchaseServices()

    def test_add_purchase(self):
        purchase = self.service.add_purchase(self.purchase_4)

        for key in self.purchase_4.keys():
            self.assertEqual(self.purchase_4[key], getattr(purchase, key))
    
    def test_update_purchase(self):
        purchase = self.service.update_purchase(2, self.purchase_4)
        for key in self.purchase_4.keys():
            self.assertEqual(self.purchase_4[key], getattr(purchase, key))

    def test_delete_purchase(self):
        purchase = self.service.delete_purchase(1)
        self.assertIsNone(purchase)


if __name__ == '__main__':
    unittest.main()
    