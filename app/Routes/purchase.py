from flask import Blueprint, request
from app.Services.purchase import PurchaseServices
from app.Schemas.purchases import purchase_schema, purchases_schema

purchase = Blueprint('purchase', __name__, url_prefix='/api/purchase')
services = PurchaseServices()


@purchase.route('/add_purchase', methods=['POST'])
def add_purchase():
    purchase = purchase_schema.loads(request.json)
    try:
        status_code = 201
        return purchase_schema.dump(services.add_purchase(purchase)), status_code
    except:
        status_code = 400
        return purchase_schema.dumps(services.add_purchase(purchase)), status_code

@purchase.route('/delete/<int:id>', methods=['PUT'])  
def delete_purchase(id):
    try:
        status_code = 200
        return purchase_schema.dumps(services.delete_purchase(id)), status_code
    except:
        status_code = 404
        return purchase_schema.dumps(services.delete_purchase(id)), status_code

@purchase.route('/get_last/',methods=['GET'])
def get_last_record():
    try:
        status_code = 200
        return purchase_schema.dumps(services.get_last_record()), status_code
    except:
        status_code = 404
        return purchase_schema.dumps(services.get_last_record()), status_code