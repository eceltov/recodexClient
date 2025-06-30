from flask import Blueprint, jsonify, request

api_bp = Blueprint('groups', __name__)

@api_bp.route('/v1/groups', methods=['GET'])
def get_group():
    return jsonify(
        {
            "success": True,
            "code": 200,    
            "payload": [    
                {
                "id": "10000000-2000-4000-8000-160000000000",
                }
            ]
        }
    ), 200
