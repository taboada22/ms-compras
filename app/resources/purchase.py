import logging
from flask import Blueprint, request, jsonify
from app.services.purchase_services import PurchasesService
from app.schemas.schema_puchase import PurchaseSchema

purchase = Blueprint('compra', __name__, url_prefix='/api/compra')  
service = PurchasesService()
purchase_schema = PurchaseSchema()
@purchase.route('/addpurchase', methods=['POST'])  
def add_purchase():
    logging.info(f"purchase {request.json}")
    purchase_data = purchase_schema.load(request.json)
    purchase_data = service.add_purchase(purchase_data)  
    return purchase_schema.dump(purchase_data), 200

@purchase.route('/delete/<int:id>', methods=['PUT'])  
def delete_purchase(id):
    service.delete_purchase(id)
    return '', 200

@purchase.route('/find_by_id/<int:id>', methods=['GET'])  
def get_purchase(id):
    purchase = purchase_schema.dump(service.get_purchase(id))
    if purchase is None:
        return jsonify({'message': 'Not found'}), 404
    return purchase

