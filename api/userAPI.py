import uuid
from flask import Blueprint, request, jsonify, render_template
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('user')

userAPI = Blueprint('userAPI', __name__)

@userAPI.route('/add', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        try:
            id = uuid.uuid4()
            user_Ref.document(id.hex).set(request.json)
            return jsonify({'success': True}), 200
        except Exception as e:
            return f"An error occurred: {e}"
    elif request.method == 'GET':
        return render_template('add_user.html')

@userAPI.route('/list', methods=['GET'])
def read():
    try:
        all_users = [doc.to_dict() for doc in user_Ref.stream()]
        return render_template('list_users.html', users=all_users)
    except Exception as e:
        return f"An error occurred: {e}"
    