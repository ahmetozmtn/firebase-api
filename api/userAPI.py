from idGen import id_gen
from flask import Blueprint, request, jsonify, abort
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection("user")

userAPI = Blueprint("userAPI", __name__)


@userAPI.route("/add", methods=["POST"])
def create():
    try:
        id = id_gen(10)
        user_Ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as error:
        return f"An Error Occured: {error}"


@userAPI.route("/list")
def read_data():
    try:
        docs = user_Ref.stream()
        docs_list = []
        for doc in docs:
            docs_list.append(doc.to_dict())
        return jsonify(docs_list), 200
    except Exception as error:
        return f"An Error Occured {error}"


@userAPI.route('/delete/<string:id>', methods=['DELETE'])
def delete_data(id):
    try:
        docs = user_Ref.list_documents()
        docs_list = []
        for doc in docs:
            docs_list.append(doc.id)
        if id in docs_list:
            document_ref = user_Ref.document(id)
            document_ref.delete()
            return jsonify({'message': f'{id} data has been deleted.'})
        else:
            return jsonify({'message': f'An error has occurred, please check the id.'})
    except Exception as error:
        return f"An Error Occured: {error}"


@userAPI.route("/doclist")
def read_doc():
    try:
        docs = user_Ref.list_documents()
        docs_list = []
        for doc in docs:
            docs_list.append(doc.id)
        return jsonify(docs_list)
    except Exception as error:
        return f"An Error Occured: {error}"


@userAPI.app_errorhandler(404)
def not_found(error):
    return jsonify({'errorCode': 404, 'message': 'Route not found'})
