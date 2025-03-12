from app import ma
from marshmallow import fields, Schema, post_load
from app.Models.purchases import Purchase

class PurchaseSchema(ma.Schema):
    class Meta:
        fields = ('id_purchase', 'id_product', 'purchase_date', 'shipping_address', 'active', 'deleted')

purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)