from datetime import datetime
from marshmallow import fields, Schema, post_load
from app.models import Purchase

class PurchaseSchema(Schema):
    id_purchase = fields.Integer(dump_only=True)
    id_product = fields.Integer(required=True)
    mailing_address = fields.String(required=True)
    date_purchase = fields.DateTime(load_default=datetime.today())
    deleted_at = fields.DateTime(dump_only=True)

    @post_load
    def make_compra(self, data, **kwargs):
        return Purchase(**data)