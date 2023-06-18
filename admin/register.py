from contracts.users import UserSignUp
from flask import Blueprint, request, jsonify
from models.utils import coll_users
from project_utils import setup_logging
from project_utils import get_user_id
from datetime import datetime

log = setup_logging('current_log')

admin_blueprint = Blueprint('model1', __name__)


@admin_blueprint.route('/admin/sign_up', methods=['POST'])
def sign_up():
    try:
        req: UserSignUp = None
        req, error = UserSignUp.load_from_json(request.get_json())
        if not req:
            return jsonify({'error': 'Invalid request data'}), 400
        if not req.email or not req.password or not req.username:
            error = f"You need to provide mandatory fields like: Email, Password, Username"
            log.info(f"{error}")
            return jsonify({'error': error}), 422
        user = coll_users.find_one({"user_id": req.user_id})
        if user:
            error = f"User already present with this Id: {req.user_id}"
            log.info(f"{error}")
            return jsonify({'error': error}), 422
        email_user = coll_users.find_one({"email": req.email})
        if email_user:
            error = f"User already present with this Email: {req.email}"
            log.info(f"{error}")
            return jsonify({'error': error}), 422
        username_user = coll_users.find_one({"username": req.username})
        if username_user:
            error = f"User already present with this Username: {req.username}"
            log.info(f"{error}")
            return jsonify({'error': error}), 422
        email = req.email
        password = req.password
        username = req.username
        user_id = req.user_id if req.user_id else get_user_id()
        gender = req.gender if req.gender else ''
        created_on = req.created_on if req.created_on else datetime.utcnow()
        first_name = req.first_name if req.first_name else ''
        last_name = req.last_name if req.last_name else ''
        phone_no = req.phone_no if req.phone_no else ''
        data = {"email": email, "password": password, "username": username, "user_id": user_id, "gender": gender,
                "created_on": created_on, "first_name": first_name, "lastname": last_name, "phone_no": phone_no}
        coll_users.insert_one(data)
        return jsonify({'message': 'User signed up successfully'}), 200
    except Exception as ex:
        log.error(ex)
        return jsonify({"message": f"User can not be created ex: {ex}"}), 500


#   sign in
#   username/email, password
#
#
